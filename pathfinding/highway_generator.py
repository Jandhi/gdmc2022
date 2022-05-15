from progress.bar import Bar
from gdpc.interface import Interface

import heapq
from generator import Generator
from directions import Direction
from palette.material import Material
from terrain.buildmap import NOTHING, ROAD
from util.point_utils import three_by_three
from vector import sum_vectors

RED_POINTS = False

def taxi_dist2(p1, p2):
    return abs(p2[0] - p1[0]) + abs(p2[1] - p1[1])

def taxi_dist3(p1, p2):
    return abs(p2[0] - p1[0]) + abs(p2[1] - p1[1]) + abs(p2[2] - p1[2])

class HighwayGenerator(Generator):
    name = 'Highway Generator'
    road_material : Material
    slab_material : Material

    def __init__(self, **kwargs) -> None:
        super().__init__(**kwargs)

        self.x1, self.z1 = self.p1
        self.x2, self.z2 = self.p2
        self.y1 = self.hmap[self.x1][self.z1] - 1
        self.y2 = self.hmap[self.x2][self.z2] - 1

        self.existing_tiles = {}

    def set_points(self, p1, p2):
        self.p1 = p1
        self.p2 = p2
        self.x1, self.z1 = self.p1
        self.x2, self.z2 = self.p2
        self.y1 = self.hmap[self.x1][self.z1] - 1
        self.y2 = self.hmap[self.x2][self.z2] - 1

    def __get_work_amount__(self) -> int:
        return None
    #    return taxi_dist(self.p1, self.p2)

    def generate(self, interface: Interface):
        path = self.find_path()

        if path is None:
            print('Could not find path :(')
            return

        self.build_path(path, interface)
    
    def find_path(self) -> list[tuple[int, int, int]]:
        visited = set()
        first_path = [(self.x1, self.y1, self.z1)]
        queue = [(self.get_priority(first_path), first_path)]
        heapq.heapify(queue)

        while len(queue) > 0:
            priority, path = heapq.heappop(queue)
            
            if path[-1] == (self.x2, self.y2, self.z2):
                for px, py, pz in path:
                    self.existing_tiles[(px, pz)] = py

                return path
            
            for node in self.get_neighbours(path[-1], path, visited):
                visited.add((node[0], node[2]))
                new_path = path.copy()
                new_path.append(node)
                heapq.heappush(queue, (self.get_priority(new_path), new_path))

    def get_priority(self, path):
        return self.get_cost(path) + self.get_heuristic(path)

    def get_cost(self, path):
        cost = 0.0

        for index, (x, y, z) in enumerate(path):
            if index != len(path) - 1:
                nx, ny, nz = path[index + 1]

                if nx != x and nz != z:
                    cost += 0.41

                cost += 2 * abs(y - ny) # cost to going up or down

            cost += 1 # base cost

            if (x, z) in self.existing_tiles:
                cost -= 2 # reuse discount!
            
            if self.wmap[x][y]:
                cost += 3 # bridge cost
            
            ground = self.hmap[x][z] - 1
            cost += 3 * abs(y - ground) # carving cost

        return cost

    def get_heuristic(self, path):
        return taxi_dist3((self.x2, self.y2, self.z2), path[-1])

    def is_out_of_bounds(self, node):
        return node[0] < 0 or node[2] < 0 or node[0] >= self.width or node[2] >= self.depth
            
    def get_neighbours(self, node, path, visited):
        neighbours = set()
        x, y, z = node
        
        # straight
        for dir in Direction.cardinal:
            for dy in (-1, 0, 1): # some carving
                vec = Direction.vectors[dir]
                
                px, py, pz = sum_vectors(node, vec, vec)
                
                if self.is_out_of_bounds((px, py, pz)):
                    continue

                py = self.hmap[px][pz] - 1 + dy

                if (px, pz) in visited:
                    continue

                if abs(py - y) > 1:
                    continue

                if (px, pz) in self.existing_tiles and py != self.existing_tiles[(px, pz)]:
                    continue

                if self.bmap is not None:
                    if any(self.bmap[bx][bz] != NOTHING for bx, bz in three_by_three((px, pz))):
                        continue
                
                neighbours.add((px, py, pz))

        # diagonals
        for dir in Direction.cardinal:
            for dy in (-1, 0, 1): # some carving
                vec = Direction.vectors[dir]
                left_vec = Direction.vectors[Direction.left[dir]]

                px, py, pz = sum_vectors(node, vec, vec, left_vec, left_vec)
                vx, vy, vz = sum_vectors(node, vec, vec)
                lx, ly, lz = sum_vectors(node, left_vec, left_vec)
                
                if self.is_out_of_bounds((px, py, pz)):
                    continue

                py = self.hmap[px][pz] - 1 + dy

                if (px, pz) in visited or (vx, vz) in visited or (lx, lz) in visited:
                    continue

                if abs(py - y) > 1:
                    continue

                if (px, pz) in self.existing_tiles and py != self.existing_tiles[(px, pz)]:
                    continue

                if self.bmap is not None:
                    if any(self.bmap[bx][bz] != NOTHING for bx, bz in three_by_three((px, pz))):
                        continue
                
                neighbours.add((px, py, pz))
        
        return neighbours

    # build path based on average height of surrounding points on the path
    def build_path(self, path, interface):
        heights = {(x, z) : y for x, y, z in path}
        visited = set()

        self.bar = Bar(f'Building Highway!', max=len(path))

        for index, (px, py, pz) in enumerate(path):
            self.bar.next()
            road_points = three_by_three((px, pz))

            if index != len(path) - 1:
                nx, ny, nz = path[index + 1]

                # if it is diagonal we add some points
                if nx != px and nz != pz:
                    road_points.add((px, nz))
                    road_points.add((nx, pz))

            for x, z in road_points:
                if (x, z) in visited or self.is_out_of_bounds((x, 0, z)):
                    continue

                visited.add((x, z))

                slab_material = self.slab_material if not self.wmap[x][z] else self.bridge_slab_material
                road_material = self.road_material if not self.wmap[x][z] else self.bridge_material
                
                if (x, z) in heights:
                    if RED_POINTS:
                        interface.placeBlock(x, heights[(x, z)], z, 'red_wool')
                    else:
                        road_material.place_block(interface, x, heights[(x, z)], z)

                    if self.bmap is not None:
                        self.bmap[x][z] = ROAD

                    # remove above
                    for i in range(1, 4):
                        interface.placeBlock(x, heights[(x, z)] + i, z, 'air')
                    
                    # fill bellow
                    ground = self.hmap[x][z]
                    if ground < heights[(x, z)] and heights[(x, z)] - ground < 5:
                        for gy in range(ground, heights[(x, z)]):
                            road_material.place_block(interface, x, gy, z)

                else:
                    if self.bmap is not None and self.bmap[x][z] != NOTHING:
                        continue

                    neighbours = []

                    for (nx, nz) in three_by_three((x, z)):
                        if (nx, nz) in heights:
                            neighbours.append((nx, nz))

                    # special case for diagonal fill-ins, which don't have neighbours
                    # we consider the path points they fill in for neighbours
                    if len(neighbours) == 0:
                        nx, ny, nz = path[index + 1]
                        neighbours.append((px, pz))
                        neighbours.append((nx, nz))
                    
                    total = sum([heights[(nx, nz)] for nx, nz in neighbours])
                    avg = float(total) / len(neighbours)
                    decimal = avg - int(avg)
                    y = int(avg)
                    use_slab = False

                    if decimal > 0.75:
                        y += 1
                    elif decimal > 0.25:
                        y += 1
                        use_slab = True
                    
                    material = slab_material if use_slab else road_material
                    material.place_block(interface, x, y, z)

                    if self.bmap is not None:
                        self.bmap[x][z] = ROAD

                    # clear above
                    for i in range(1, 4):
                        interface.placeBlock(x, y + i, z, 'air')

                    # fill bellow
                    ground = self.hmap[x][z]
                    if ground < y  and y - ground < 5:
                        for gy in range(ground, y):
                            road_material.place_block(interface, x, gy, z)

    # deprecated!            
    def build_path2(self, path, interface : Interface):
        for index, (x, y, z) in enumerate(path):
            if index == len(path) - 1:
                return

            nx, ny, nz = path[index + 1] # next point

            x_delta = (nx - x) / 2
            z_delta = (nz - z) / 2
            y_delta = (ny - y)
            
            if abs(x_delta) + abs(z_delta) == 1:
                dir = {
                    (1, 0)  : Direction.x_plus,
                    (-1, 0) : Direction.x_minus,
                    (0, 1)  : Direction.z_plus,
                    (0, -1) : Direction.z_minus
                }[(x_delta, z_delta)]

                # self.road_material.place_block(interface, x, y, z)
                interface.placeBlock(x, y, z, 'red_wool')
                left_point = sum_vectors((x, y, z), Direction.vectors[Direction.left[dir]])
                self.road_material.place_block(interface, *left_point)
                right_point = sum_vectors((x, y, z), Direction.vectors[Direction.right[dir]])
                self.road_material.place_block(interface, *right_point)

                # the blocks in between should be slabs if going up or down
                # the slabs will be a block higher if going up
                between_material = self.road_material if y_delta == 0 else self.slab_material
                dy = 1 if y_delta == 1 else 0

                point = sum_vectors((x, y + dy, z), Direction.vectors[dir])
                between_material.place_block(interface, *point)
                left_point = sum_vectors(point, Direction.vectors[Direction.left[dir]])
                between_material.place_block(interface, *left_point)
                right_point = sum_vectors(point, Direction.vectors[Direction.right[dir]])
                between_material.place_block(interface, *right_point)
            else:
                # diagonal
                pass
            


