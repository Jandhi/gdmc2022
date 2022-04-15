from house.grid import Grid, node_to_world_coords
from noise.noise import shuffle
from noise.random import hash_vector, odds, recursive_hash as rhash
from gdpc.interface import Interface


class NodePlacer:
    def __init__(self, grid : Grid, passable_map, interface : Interface) -> None:
        self.grid = grid
        self.passable_map = passable_map
        self.width = len(self.passable_map)
        self.depth = len(self.passable_map[0])
        self.interface = interface

    def run(self) -> None:
        node_queue = [(0, 0, 0)]

        while len(node_queue) > 0:
            x, y, z = node_queue.pop(0)

            seed = rhash(
                hash('node_placer'), 
                hash_vector(self.grid.origin), 
                x, y, z
            )

            if not self.tile_is_clear(x, y, z):
                continue

            if odds(rhash(seed, 0), len(self.grid.nodes), 7):
                continue

            height = 2

            if odds(rhash(seed, 2), 1, 5):
                height += 1
            elif height > 1 and odds(rhash(seed, 3), 1, 3):
                height -= 1
            
            for py in range(height):
                self.grid.add_node(x, py, z)
            
            for p in shuffle(rhash(seed, 4), [
                (x + 1, y, z),
                (x, y, z + 1),
                (x - 1, y, z),
                (x, y, z - 1)
            ]):
                if not p in self.grid.nodes:
                    node_queue.append(p)
        
        for x, y, z in self.grid.nodes:
            self.mark_impassable(x, z)


    def tile_is_clear(self, x, y, z):
        x0, y0, z0 = node_to_world_coords(self.grid, x, y, z)
        return self.is_clear(x0, z0)
    
    def is_clear(self, x, z):
        # check bounds
        if x < 0 or z < 0 or x + self.grid.width > self.width or z + self.grid.depth > self.depth:
            return False

        for dx in range(self.grid.width):
            for dz in range(self.grid.depth):
                if not self.passable_map[x + dx][z + dz]:
                    return False
        
        return True

    def mark_impassable(self, x, z):
        px, py, pz = node_to_world_coords(self.grid, x, 0, z)
        for dx in range(self.grid.width):
            for dz in range(self.grid.depth):
                self.passable_map[px + dx][pz + dz] = False