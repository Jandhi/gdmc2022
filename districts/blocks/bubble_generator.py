from operator import ge
from generator import Generator
from districts.bubble import Bubble
from districts.bubble_layout import BubbleLayout
from gdpc.interface import Interface
from palette.block import Block
from palette.material import MixedMaterial
from pathfinding.highway_generator import HighwayGenerator
from pathfinding.pathfinder import get_web
from structures.structure_placer import StructurePlacer
from util.point_utils import distance_2d, neighbours_2d

from noise.random import recursive_hash

class BubbleGenerator(Generator):
    name = 'bubble generator'
    point_density = 20 / (256 ** 2)
    bubble_colors = [
        'red_wool',
        'light_blue_wool',
        'yellow_wool',
        'orange_wool',
        'lime_wool',
        'cyan_wool',
        'pink_wool',
        'blue_wool',
        'magenta_wool',
        'green_wool',
        'purple_wool',
        'brown_wool'
    ]
    outer_distance_minimum = 8
    inner_distance_minimum = 5
    bubble_map = None

    def get_bubble_wool(self, district):
        if district is None:
            return 'air'
        
        return self.bubble_colors[district % len(self.bubble_colors)].replace('wool', 'stained_glass')

    def __init__(self, **kwargs) -> None:
        super().__init__(**kwargs)

        self.bubbles : list[Bubble] = None
        self.bubble_layout : BubbleLayout = None

        self.placer = StructurePlacer(
            area=self.area, 
            slice=self.slice, 
            hmap=self.hmap, 
            omap=self.omap, 
            wmap=self.wmap, 
            bmap=self.bmap
        )

        self.point_amount = int(self.point_density * self.width * self.height)

    def __generate__(self, interface : Interface):
        self.bubble_map = [[None for z in range(self.depth)] for x in range(self.width)]

        self.flood()
        self.create_road_network(interface)
    
    def generate_start_points(self):
        start_points = []
        attempts = 0

        # outer points
        for p in range(self.point_amount // 2):
            seed = recursive_hash(hash('bubble_generator_points'), attempts)
            x = recursive_hash(seed, 0) % self.width
            z = recursive_hash(seed, 1) % self.depth
            attempts += 1

            while attempts < 100 and any([distance_2d((x, z), point) < self.outer_distance_minimum for point in start_points] + [self.wmap[x][z]]):
                seed = recursive_hash(hash('bubble_generator_points'), attempts)
                x = recursive_hash(seed, 0) % self.width
                z = recursive_hash(seed, 1) % self.depth
                attempts += 1

            if attempts >= 100:
                break

            start_points.append((x, z))

        # inner points
        for p in range(self.point_amount - (self.point_amount // 2)):
            seed = recursive_hash(hash('bubble_generator_points'), attempts)
            x = recursive_hash(seed, 0) % (self.width // 2) + self.width // 4
            z = recursive_hash(seed, 1) % (self.depth // 2) + self.depth // 4
            attempts += 1

            while attempts < 200 and any([distance_2d((x, z), point) < self.inner_distance_minimum for point in start_points] + [self.wmap[x][z]]):
                seed = recursive_hash(hash('bubble_generator_points'), attempts)
                x = recursive_hash(seed, 0) % self.width
                z = recursive_hash(seed, 1) % self.depth
                attempts += 1

            if attempts >= 200:
                break

            start_points.append((x, z))
        
        return start_points

    def flood(self):
        print('Beginning flood')
        start_points = self.generate_start_points()
        self.bubbles = []

        for index, point in enumerate(start_points):
            x, z = point
            self.bubble_map[x][z] = index
            self.bubbles.append(Bubble(point))

        self.bubble_layout = BubbleLayout(self.bubbles)

        queue = start_points.copy()
        leftover_queue = []
        visited = set()

        while len(queue) > 0:
            x, z = queue.pop(0)
            current_bubble_index = self.bubble_map[x][z]

            for px, pz in neighbours_2d((x, z)):
                # bounds
                if px < 0 or pz < 0 or px >= self.width or pz >= self.depth:
                    continue

                if (px, pz) in neighbours_2d((x, z), self.hmap, self.wmap):
                    # is accessible
                    if self.bubble_map[px][pz] != None:
                        if self.bubble_map[px][pz] != current_bubble_index:
                            # establish neighbours
                            d1, d2 = self.bubbles[current_bubble_index], self.bubbles[self.bubble_map[px][pz]]
                            self.bubble_layout.set_neighbours(d1, d2)

                        # already claimed
                        continue
                    else:
                        visited.add((px, pz))
                        self.bubble_map[px][pz] = current_bubble_index
                        self.bubbles[current_bubble_index].add_point((px, pz))
                        queue.append((px, pz))
                else:
                    # not accessible
                    visited.add((px, pz))
                    self.bubble_map[px][pz] = current_bubble_index
                    self.bubbles[current_bubble_index].add_point((px, pz))
                    leftover_queue.append((px, pz))

        '''
        The leftover queue ensures that all tiles in the map are claimed by a district
        However, they are only expanded into once all normal tiles are expanded into
        The leftovers include holes, mountains, and water
        This ensures our neighbour relationships make sense (e.g. a river may divide neighbouring districts)
        '''
        while len(leftover_queue) > 0:
            x, z = leftover_queue.pop(0)
            current_bubble_index = self.bubble_map[x][z]

            for px, pz in neighbours_2d((x, z)):
                # bounds
                if px < 0 or pz < 0 or px >= self.width or pz >= self.depth:
                    continue

                if self.bubble_map[px][pz] != None:
                    if self.bubble_map[px][pz] != current_bubble_index:
                        # establish neighbours
                        d1, d2 = self.bubbles[current_bubble_index], self.bubbles[self.bubble_map[px][pz]]
                        self.bubble_layout.set_neighbours(d1, d2)

                    # already claimed
                    continue
                elif (px, pz) not in visited:
                    visited.add((px, pz))
                    self.bubble_map[px][pz] = current_bubble_index
                    self.bubbles[current_bubble_index].add_point((px, pz))
                    leftover_queue.append((px, pz))
    
    def find_paths(self):
        def shift(point):
            x, z = point
            return (int(x) // 2) * 2, (int(z) // 2) * 2

        points = [shift(bubble.average_point) for bubble in self.bubbles]

        generator = HighwayGenerator(
            area=self.area, 
            hmap=self.hmap, 
            wmap=self.wmap, 
            bmap=self.bmap,
            road_material = self.road_material,
            slab_material = self.slab_material,
            bridge_material = MixedMaterial(
                [Block('oak_planks').material()]
            ),
            bridge_slab_material = Block('oak_slab').material(),
            p1=(0,0),
            p2=(0,0)
        )

        paths = [[None for j in range(len(points))] for i in range(len(points))]

        for i in range(len(points)):
            for j in range(i + 1, len(points)):
                if not self.bubble_layout.are_neighbours_list[i][j] and distance_2d(points[i], points[j]) > 100:
                    continue

                print(f'Finding path from {i} to {j}')
                generator.set_points(points[i], points[j])
                path = generator.find_path()
                paths[i][j] = path
                paths[j][i] = path
        
        return paths

    def get_minimum_spanning_tree(self, paths):
        connected = []
        disconnected = list(range(len(self.bubbles)))
        confirmed_paths = []

        connected.append(disconnected.pop(0))

        while len(disconnected) > 0:
            minimum_connection = None
            minimum_distance = None

            # we find the minimum connection between connected and disconnected points
            for c in connected:
                for d in disconnected:
                    path = paths[c][d]

                    if not path:
                        continue

                    if not minimum_distance or len(path) < minimum_distance:
                        minimum_connection = c, d
                        minimum_distance = len(path)

            if not minimum_connection: 
                print(f'Could not find connections for {disconnected}')
                break

            c, d = minimum_connection

            if c != None and d != None:
                print(f'Adding path from {c} to {d}')
                confirmed_paths.append(paths[c][d])
                self.bubble_layout.connection_length[c][d] = len(paths[c][d])
                self.bubble_layout.connection_length[d][c] = len(paths[d][c])
            
            connected.append(d)
            disconnected.remove(d)
        
        return confirmed_paths

    # fills out the minimum spanning tree with paths that make sense
    def fill_out_road_graph(self, paths, confirmed_paths):
        bubble_indices = list(range(len(self.bubbles)))
        
        while True:
            worst_connection = None
            worst_connection_ratio = 0

            def get_neighbours(bubble_index):
                neighbours = []
                for other in bubble_indices:
                    if other == bubble_index:
                        continue

                    if self.bubble_layout.connection_length[bubble_index][other] != -1:
                        neighbours.append(other)
                
                return neighbours

            def get_cost(path, end_node):
                cost = 0
                
                for index, bubble in enumerate(path):
                    if index == len(path) - 1:
                        return cost

                    next = path[index + 1]
                    cost += self.bubble_layout.connection_length[bubble][next]

            
            web = get_web(bubble_indices, get_neighbours, get_cost)

            for a in bubble_indices:
                for b in bubble_indices:
                    if a <= b: # don't check path to self or backwards duplicates
                        continue

                    if paths[a][b] is None or web[a][b] is None:
                        continue

                    current_distance = get_cost(web[a][b], None)
                    ideal_distance = len(paths[a][b])
                    ratio = float(current_distance) / ideal_distance
                        
                    if ratio > worst_connection_ratio and current_distance > 25:
                        worst_connection = (a, b)
                        worst_connection_ratio = ratio
            
            if worst_connection_ratio > 1.9:
                a, b = worst_connection
                path = paths[a][b]
                length = len(path)
                confirmed_paths.append(path)
                self.bubble_layout.connection_length[a][b] = length
                self.bubble_layout.connection_length[b][a] = length
            else:
                return
    
    def create_road_network(self, interface):
        paths = self.find_paths()
        confirmed_paths = self.get_minimum_spanning_tree(paths)
        self.fill_out_road_graph(paths, confirmed_paths)

        generator = HighwayGenerator(
            area=self.area, 
            hmap=self.hmap, 
            wmap=self.wmap,
            bmap=self.bmap, 
            road_material = self.road_material,
            slab_material = self.slab_material,
            bridge_material = MixedMaterial(
                [Block('oak_planks').material()]
            ),
            bridge_slab_material = Block('oak_slab').material(),
            p1=(0,0),
            p2=(0,0)
        )

        for path in confirmed_paths:
            generator.build_path(path, interface)



        

        
