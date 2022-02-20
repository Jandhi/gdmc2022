from gdpc.interface import Interface
from noise.noise import choose, choose_weighted
from palette.block import Block

class Material:
    def place_block(self, interface: Interface, seed: int, x: int, y: int, z: int, direction=None):
        pass

class BasicMaterial(Material):
    def __init__(self, block : Block) -> None:
        self.block = block

    def place_block(self, interface: Interface, seed: int, x: int, y: int, z: int, direction=None):
        block = self.block.get_facing(direction)
        interface.placeBlock(x, y, z, block)

class MixedMaterial(Material):
    def __init__(self, materials : list[Material]) -> None:
        self.materials = materials

    def place_block(self, interface: Interface, seed: int, x: int, y: int, z: int, direction=None):
        choose(seed, self.materials).place_block(interface, seed, x, y, z, direction)

class WeightedMaterial(Material):
    def __init__(self, materials : list[tuple[Material, int]]) -> None:
        self.materials = materials

    def place_block(self, interface: Interface, seed: int, x: int, y: int, z: int, direction=None):
        choose_weighted(seed, self.materials).place_block(interface, seed, x, y, z, direction)