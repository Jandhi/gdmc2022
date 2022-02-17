from matplotlib.pyplot import sca
from tools import setBlock
from noise.random import hash_vector, recursive_hash
from vector import product, product_vectors
from directions import Direction

class Block:
    weight = 0.0
    scaling = (1.0, 1.0, 1.0)
    direction_scaling = {}

    def __init__(self, name, weight, scaling = None, direction_scaling = None) -> None:
        self.name = name
        self.weight = weight

        if scaling:
            self.scaling = scaling
        
        if direction_scaling:
            self.direction_scaling = direction_scaling

    def get_odds(self, x, y, z, direction) -> float:
        location_scaling = product(product_vectors((x, y, z), self.scaling))
        direction_scaling = self.direction_scaling[direction] if direction in self.direction_scaling else 1.0
        return self.weight * location_scaling * direction_scaling

class Material:
    __contents : list[Block] = []

    def __init__(self, contents : list[tuple[str, float]] = None) -> None:
        if contents:
            self.__contents = contents

    def with_block(self, block, weight):
        self.__contents.append((weight, block))
        return self
    
    def get_block(self, seed, x, y, z, direction) -> str:
        total_weight = 0
        blocks = []

        for block in self.__contents:
            odds = block.get_odds(x, y, z, direction)
            total_weight += odds
            blocks.append((block, odds))

        index = seed % total_weight

        for block, weight in blocks:
            index -= weight

            if index < 0:
                return block
    
    def fill(self, coords, size, direction) -> None:
        x0, y0, z0 = coords
        
        
    
    