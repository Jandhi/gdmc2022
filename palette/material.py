from gdpc.interface import Interface
from noise.random import hash_vector
from noise.noise import choose, choose_weighted
from palette.block import Block
from random import seed
from random import randint

class Material:
    def place_block(self, interface: Interface, seed: int, x: int, y: int, z: int, direction=None):
        pass

class BasicMaterial(Material):
    def __init__(self, block : Block) -> None:
        self.block = block

    def place_block(self, interface: Interface, x: int, y: int, z: int, chance: int=100, direction=None, Seed: int=None):
        seed()
        if chance!=100:
            a = randint(1,100)
            if a<=chance:
                block = self.block.get_facing(direction)
                interface.placeBlock(x, y, z, block)
            else:
                pass
        else:
            block = self.block.get_facing(direction)
            interface.placeBlock(x, y, z, block)
        
    #a place block that has the possibility of passing swap as true to allow the x and z passed values to swap, used for rotational purposes    
    def place_block_swap(self, interface: Interface, x:int, y:int, z:int, swap: bool=False):
        block = self.block
        if swap:
            interface.placeBlock(z, y, x, block)
        else:
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