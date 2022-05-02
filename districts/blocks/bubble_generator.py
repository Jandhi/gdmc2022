from tkinter import E
from districts.bubble import Bubble
from districts.bubble_layout import BubbleLayout
from generator import Generator
from gdpc.interface import Interface
from noise.random import recursive_hash as rhash
from pathfinding.pathfinder import get_web
from pathfinding.roadpaths import ROAD, create_get_neighbours_function, get_cost
from util.point_utils import distance_2d, neighbours_2d, neighbours_2d_diagonal
from math import cos, log, pi, sin

class BubbleGenerator(Generator):
    name = 'bubble generator'
    point_amount = 20
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

    def get_bubble_color(self, district):
        return self.bubble_colors[district % len(self.bubble_colors)]

    def __init__(self, **kwargs) -> None:
        super().__init__(**kwargs)

        self.bubbles : list[Bubble] = None
        self.bubble_layout : BubbleLayout = None

    def __get_work_amount__(self) -> int:
        return self.width * self.depth

    def __generate__(self, interface : Interface):
        bubble_map = [[None for z in range(self.depth)] for x in range(self.width)]

        self.flood(bubble_map)

        for x in range(self.width):
            for z in range(self.depth):
                interface.placeBlock(x, 3, z, self.get_bubble_color(bubble_map[x][z]))
        
        self.generate_roads(interface)
        
    def build_path(self, path, interface):
        for point in path:
            interface.placeBlock(point[0], 3, point[1], 'cobblestone')

            for x, z in neighbours_2d(point):
                interface.placeBlock(x, 3, z, 'cobblestone')

    def get_random_start_point(self, seed):
        x = rhash(seed, 0) % self.width
        z = rhash(seed, 1) % self.depth
        return (x, z)

    def generate_start_points(self):
        start_points = []
        attempts = 0

        for p in range(self.point_amount):
            seed = rhash(hash('bubble_generator_points'), attempts)
            attempts += 1
            x, z = self.get_random_start_point(seed)

            for px, pz in start_points:
                is_out_of_bounds = x < 0 or x >= self.width or z < 0 or z >= self.depth
                while is_out_of_bounds or abs(px - x) + abs(pz - z) < 6:
                    seed = rhash(hash('bubble_generator_points'), attempts)
                    attempts += 1
                    x, z = self.get_random_start_point(seed)

                    if attempts > 100:
                        break
                
            start_points.append((x, z))
        
        return start_points

    def flood(self, bubble_map):
        start_points = self.generate_start_points()
        self.bubbles = []

        for index, point in enumerate(start_points):
            x, z = point
            bubble_map[x][z] = index
            self.bubbles.append(Bubble(point))

        self.bubble_layout = BubbleLayout(self.bubbles)

        queue = start_points.copy()
        visited = set()

        while len(queue) > 0:
            x, z = queue.pop(0)
            current_bubble_index = bubble_map[x][z]

            for px, pz in neighbours_2d((x, z)):
                # bounds
                if px < 0 or pz < 0 or px >= self.width or pz >= self.depth:
                    continue
                
                if bubble_map[px][pz] != None:
                    if bubble_map[px][pz] != current_bubble_index:
                        # establish neighbours
                        d1, d2 = self.bubbles[current_bubble_index], self.bubbles[bubble_map[px][pz]]
                        self.bubble_layout.set_neighbours(d1, d2)

                    # already claimed
                    continue
                else:
                    visited.add((px, pz))
                    bubble_map[px][pz] = current_bubble_index
                    self.bubbles[current_bubble_index].add_point((px, pz))
                    queue.append((px, pz))

    def generate_roads(self, interface):
        points = []
        
        for bubble in self.bubbles:
            x, z = bubble.average_point
            y = self.slice.heightmaps['MOTION_BLOCKING_NO_LEAVES'][int(x)][int(z)]
            points.append((int(x), y, int(z), ROAD, 0))

        web = get_web(
            points, 
            create_get_neighbours_function(self.width, self.depth, self.slice, interface), 
            get_cost
        )

        connected = []
        disconnected = list(range(len(points)))
        paths = []

        connected.append(disconnected.pop(0))

        while len(disconnected) > 0:
            minimum_connection = None
            minimum_distance = None

            for c in connected:
                for d in disconnected:
                    path = web[c][d]

                    if not path:
                        continue

                    if not minimum_distance or len(path) < minimum_distance:
                        minimum_connection = c, d
                        minimum_distance = len(path)

            c, d = minimum_connection

            if c != None and d != None:
                print(f'Adding path from {self.get_bubble_color(c)} to {self.get_bubble_color(d)}')
                paths.append(web[c][d])
                self.bubble_layout.connection_length[c][d] = len(web[c][d])
                self.bubble_layout.connection_length[d][c] = len(web[d][c])
            
            connected.append(d)
            disconnected.remove(d)
        
        self.fill_out_road_graph(paths, web, list(range(len(connected))))

        for path in paths:
            self.build_path(path, interface)
        
    def fill_out_road_graph(self, paths, terrain_web, bubble_indices):
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

                    current_distance = get_cost(web[a][b], None)
                    ideal_distance = len(terrain_web[a][b])
                    ratio = float(current_distance) / ideal_distance
                        
                    if ratio > worst_connection_ratio and current_distance > 25:
                        worst_connection = (a, b)
                        worst_connection_ratio = ratio
            
            if worst_connection_ratio > 1.9:
                a, b = worst_connection
                path = terrain_web[a][b]
                length = len(path)
                paths.append(path)
                self.bubble_layout.connection_length[a][b] = length
                self.bubble_layout.connection_length[b][a] = length
            else:
                return

        
