from generator import Generator
from house.grid import Grid
from house.house import House
from house.house_generator import HouseGenerator
from gdpc.interface import Interface

from noise.noise import shuffle
from noise.random import recursive_hash

class BlockGenerator(Generator):
    name = 'BlockGenerator'
    passable_map : list[list[bool]]
    width : int
    depth : int

    def __generate__(self, interface : Interface):
        self.width = len(self.passable_map)
        self.depth = len(self.passable_map[0])

        edges = self.find_edges()

        for x, z in edges:
            interface.placeBlock(x, 3, z, 'orange_wool')

        inner = self.find_inner_edge(edges)
        for x, z, in inner:
            interface.placeBlock(x, 3, z, 'yellow_wool')

        while len(edges) > 0:
            x, z = edges.pop(0)

            self.attempt_placement(x, z, interface)
            

    def attempt_placement(self, x, z, interface):
        grid_width = 5
        grid_depth = 5
        
        for args in shuffle(recursive_hash(x, z), [
            (x, z, grid_width, grid_depth),
            (x - grid_width + 1, z, grid_width, grid_depth),
            (x, z - grid_depth + 1, grid_width, grid_depth),
            (x - grid_width + 1, z - grid_depth + 1, grid_width, grid_depth)
        ]):
            if self.is_clear(*args):
                self.place(*args, interface)
                return True
        
        return False

    def place(self, x, z, width, depth, interface : Interface):
        if recursive_hash(hash(self.name), x, z) % 3 == 0:
            return

        for dx in range(width):
            for dz in range(depth):
                self.passable_map[x + dx][z + dz] = False
                interface.placeBlock(x + dx, 4, z + dz, 'red_stained_glass')

                grid = Grid((x, 3, z), (width, 5, depth))
                grid.add_node(0, 0, 0)
                grid.add_node(0, 1, 0)

                house = House(grid)
                house.receded_ground_floor = False

                HouseGenerator(house=house).generate(interface)

    def is_clear(self, x, z, width, depth):
        # check bounds
        if x < 0 or z < 0 or x + width > self.width or z + depth > self.depth:
            return False

        for dx in range(width):
            for dz in range(depth):
                if not self.passable_map[x + dx][z + dz]:
                    return False
        
        return True

    def find_edges(self) -> list:
        edges = []

        for x in range(len(self.passable_map)):
            for z in range(len(self.passable_map[0])):
                if self.passable_map[x][z] and self.is_edge(x, z):
                    edges.append((x, z))
                    
        
        return edges

    def find_inner_edge(self, edges) -> list:
        inner_edges = []
        
        for x, z in edges:
            for px, pz in [(x - 1, z), (x + 1, z), (x, z - 1), (x, z + 1)]:
                # bounds
                if px < 0 or pz < 0 or px >= self.width or pz >= self.depth:
                    continue

                if self.passable_map[px][pz] and not (px, pz) in edges:
                    inner_edges.append((px, pz))
        
        return inner_edges

    def is_edge(self, x, z):
        p = self.passable_map
        on_side = x == 0 or x == self.width - 1 or z == 0 or z == self.depth - 1
        return on_side or (not p[x + 1][z]) or (not p[x - 1][z]) or (not p[x][z + 1]) or (not p[x][z - 1])