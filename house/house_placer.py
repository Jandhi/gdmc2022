
from generator import Generator
from gdpc.interface import Interface
from house.grid import BUILDING, Grid, GridNode, node_to_world_coords
from house.house_generator import HouseGenerator
from house.house import House

from noise.random import recursive_hash as rhash, hash_vector, odds
from noise.noise import shuffle

from terrain.buildmap import NOTHING, HOUSE

class HousePlacer(Generator):
    grid_size = (7, 5, 7)

    def attempt_placement(self, point, interface):
        x, y, z = point

        for px, pz in shuffle(rhash(x, z), [
            (x, z),
            (x - self.grid_size[0] + 1, z),
            (x, z - self.grid_size[2] + 1),
            (x - self.grid_size[0] + 1, z - self.grid_size[2] + 1)
        ]):
            if self.is_clear((px, pz)):
                grid = self.create_grid((px, y, pz)) 
                self.mark_grid(grid)
                HouseGenerator(area=self.area, house=House(grid)).generate(interface)
                return

    def mark_grid(self, grid : Grid):
        for node_coords in grid.nodes:
            x, y, z = node_to_world_coords(grid, *node_coords)

            for dx in range(self.grid_size[0]):
                for dz in range(self.grid_size[2]):
                    self.bmap[x + dx][z + dz] = HOUSE

    def is_clear(self, point):
        x, z = point
        for dx in range(self.grid_size[0]):
            for dz in range(self.grid_size[2]):
                # out of bounds
                if 0 > x + dx or x + dx >= self.width or 0 > z + dz or z + dz >= self.depth:
                    return False

                # has water
                if self.wmap[x + dx][z + dz]:
                    return False
                
                # is occupied
                if self.bmap[x + dx][z + dz] != NOTHING:
                    return False

        return True

    def create_grid(self, point):
        px, py, pz = point
        grid = Grid((px, py, pz), self.grid_size)

        node_queue = [(0, 0, 0)]

        while len(node_queue) > 0:
            x, y, z = node_queue.pop(0)

            seed = rhash(
                hash('node_placer'), 
                hash_vector(grid.origin), 
                x, y, z
            )

            wx, wy, wz = node_to_world_coords(grid, x, y, z)
            if not self.is_clear((wx, wz)):
                continue

            if odds(rhash(seed, 0), len(grid.nodes), 7):
                continue

            height = 2

            if odds(rhash(seed, 2), 1, 5): # 1/5 chance of higher
                height += 1
            elif height > 1 and odds(rhash(seed, 3), 1, 3): # 4/15 chance of lower
                height -= 1
            
            for py in range(height):
                grid.add_node(x, py, z, BUILDING)
            
            for p in shuffle(rhash(seed, 4), [
                (x + 1, y, z),
                (x, y, z + 1),
                (x - 1, y, z),
                (x, y, z - 1)
            ]):
                if not p in grid.nodes:
                    node_queue.append(p)

        return grid