from gdpc.interface import Interface
from noise.random import hash_vector
from noise.noise import choose, choose_weighted
from palette.block import Block

class Material:
    def place_block(self, interface: Interface, seed: int, x: int, y: int, z: int, direction=None):
        pass

class BasicMaterial(Material):
    def __init__(self, block : Block) -> None:
        self.block = block

    def place_block(self, interface: Interface, x: int, y: int, z: int, direction=None, seed: int=None):
        block = self.block.get_facing(direction)
        interface.placeBlock(x, y, z, block)

# Extension function for Block to turn it into a basic material
def material(self) -> Material:
    return BasicMaterial(self)
Block.material = material

class MixedMaterial(Material):
    def __init__(self, materials : list[Material]) -> None:
        self.materials = materials

    def place_block(self, interface: Interface, x: int, y: int, z: int, direction=None, seed: int=None):
        if not seed:
            seed = hash_vector(x, y, z)

        choose(seed, self.materials).place_block(interface, x, y, z, direction, seed)

class WeightedMaterial(Material):
    def __init__(self, materials : list[tuple[Material, int]]) -> None:
        self.materials = materials

    def place_block(self, interface: Interface, x: int, y: int, z: int, direction=None, seed: int=None):
        choose_weighted(seed, self.materials).place_block(interface, x, y, z, direction, seed)