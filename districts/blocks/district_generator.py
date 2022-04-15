from tkinter import E
from districts.district import District
from districts.district_layout import DistrictLayout
from generator import Generator
from gdpc.interface import Interface
from noise.random import recursive_hash as rhash
from pathfinding.pathfinder import get_web
from util.point_utils import distance_2d, neighbours_2d, neighbours_2d_diagonal

class DistrictGenerator(Generator):
    name = 'district generator'
    point_amount = 20
    district_colors = [
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

    def get_district_color(self, district):
        return self.district_colors[district % len(self.district_colors)]

    def __init__(self, **kwargs) -> None:
        super().__init__(**kwargs)

        self.districts : list[District] = None
        self.district_layout : DistrictLayout = None

    def __get_work_amount__(self) -> int:
        return self.width * self.depth

    def __generate__(self, interface : Interface):
        district_map = [[None for z in range(self.depth)] for x in range(self.width)]

        self.flood(district_map)

        for x in range(self.width):
            for z in range(self.depth):
                interface.placeBlock(x, 3, z, self.get_district_color(district_map[x][z]))
        
        self.generate_roads(interface)
        
    def build_path(self, path, interface):
        for point in path:
            interface.placeBlock(point[0], 3, point[1], 'cobblestone')

            for x, z in neighbours_2d(point):
                interface.placeBlock(x, 3, z, 'cobblestone')

    def generate_start_points(self):
        start_points = []
        attempts = 0

        for p in range(self.point_amount):
            seed = rhash(hash('district_generator_points'), attempts)
            attempts += 1
            x = rhash(seed, 0) % self.width
            z = rhash(seed, 1) % self.depth

            for px, pz in start_points:
                while abs(px - x) + abs(pz - z) < 6:
                    seed = rhash(hash('district_generator_points'), attempts)
                    attempts += 1
                    x = rhash(seed, 0) % self.width
                    z = rhash(seed, 1) % self.height

                    if attempts > 100:
                        break
                
            start_points.append((x, z))
        
        return start_points

    def flood(self, district_map):
        start_points = self.generate_start_points()
        self.districts = []

        for index, point in enumerate(start_points):
            x, z = point
            district_map[x][z] = index
            self.districts.append(District(point))

        self.district_layout = DistrictLayout(self.districts)

        queue = start_points.copy()
        visited = set()

        while len(queue) > 0:
            x, z = queue.pop(0)
            current_district_index = district_map[x][z]

            for px, pz in neighbours_2d((x, z)):
                # bounds
                if px < 0 or pz < 0 or px >= self.width or pz >= self.depth:
                    continue
                
                if district_map[px][pz] != None:
                    if district_map[px][pz] != current_district_index:
                        # establish neighbours
                        d1, d2 = self.districts[current_district_index], self.districts[district_map[px][pz]]
                        self.district_layout.set_neighbours(d1, d2)

                    # already claimed
                    continue
                else:
                    visited.add((px, pz))
                    district_map[px][pz] = current_district_index
                    self.districts[current_district_index].add_point((px, pz))
                    queue.append((px, pz))

    def generate_roads(self, interface):
        points = []
        
        for district in self.districts:
            x, z = district.average_point
            points.append((int(x), int(z)))
        
        # points.append((0, rhash(hash('trade_route'), 0) % self.depth))
        # points.append((self.width - 1, rhash(hash('trade_route'), 1) % self.depth))
        # points.append((rhash(hash('trade_route'), 2) % self.width, 0))
        # points.append((rhash(hash('trade_route'), 3) % self.width, self.depth - 1))

        def get_neighbours(node):
            neighbours = []
            for x, z in neighbours_2d_diagonal(node):
                if 0 <= x < self.width and 0 <= z < self.depth:
                    neighbours.append((x, z))
            return neighbours

        def get_cost(path, end_node):
            return len(path) + distance_2d(path[-1], end_node)

        web = get_web(points, get_neighbours, get_cost)

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
                print(f'Adding path from {self.get_district_color(c)} to {self.get_district_color(d)}')
                paths.append(web[c][d])
                self.district_layout.connection_length[c][d] = len(web[c][d])
                self.district_layout.connection_length[d][c] = len(web[d][c])
            
            connected.append(d)
            disconnected.remove(d)
        
        self.fill_out_road_graph(paths, web, list(range(len(connected))))

        for path in paths:
            self.build_path(path, interface)
        
    def fill_out_road_graph(self, paths, terrain_web, district_indices):
        while True:
            worst_connection = None
            worst_connection_ratio = 0

            def get_neighbours(district_index):
                neighbours = []
                for other in district_indices:
                    if other == district_index:
                        continue

                    if self.district_layout.connection_length[district_index][other] != -1:
                        neighbours.append(other)
                
                return neighbours

            def get_cost(path, end_node):
                cost = 0
                
                for index, district in enumerate(path):
                    if index == len(path) - 1:
                        return cost

                    next = path[index + 1]
                    cost += self.district_layout.connection_length[district][next]

            web = get_web(district_indices, get_neighbours, get_cost)

            for a in district_indices:
                for b in district_indices:
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
                self.district_layout.connection_length[a][b] = length
                self.district_layout.connection_length[b][a] = length
            else:
                return

        
