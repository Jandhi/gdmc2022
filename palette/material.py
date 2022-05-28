from gdpc.interface import Interface, runCommand
from noise.random import hash_vector
from noise.noise import choose, choose_weighted
from palette.block import Block
from random import seed
from random import randint
from directions import Direction

class Material:
    def place_block(self, interface: Interface, x: int, y: int, z: int, direction=None, attributes=None, seed: int=None):
        pass

class BasicMaterial(Material):
    def __init__(self, block : Block) -> None:
        self.block = block


    def place_block(self, interface: Interface, x: int, y: int, z: int, direction=None, attributes=None, seed: int=None):
        block = self.block.new()
        if attributes:
            block.set_attributes(attributes)
        block.set_facing(direction)

        name = str(block)

        interface.placeBlock(x, y, z, name)

    def place_block_chance(self, interface: Interface, x: int, y: int, z: int, chance: int=100, direction=None, Seed: int=None):
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

    def place_block(self, interface: Interface, x: int, y: int, z: int, direction=None, attributes=None, seed: int=None):
        if not seed:
            seed = hash_vector((x, y, z))

        choose(seed, self.materials).place_block(interface, x, y, z, direction, attributes, seed)

class WeightedMaterial(Material):
    def __init__(self, materials : list[tuple[Material, int]]) -> None:
        self.materials = materials

    def place_block(self, interface: Interface, x: int, y: int, z: int, direction=None, attributes=None, seed: int=None):
        if not seed:
            seed = hash_vector((x, y, z))

        choose_weighted(seed, self.materials).place_block(interface, x, y, z, direction, attributes, seed)

#material class that sends place_block as a setblock command to minecraft, used currently only for placing player heads
class SetBlockMaterial(Material):
    def __init__(self, block : Block) -> None:
        self.block = block

    def place_block(self, interface: Interface, x: int, y: int, z: int, direction=None, Seed: int=None):
        x, y, z = interface.local2global(x, y, z)
        block = self.block.name
        #setting correct direction
        if direction == Direction.x_minus:
            block = block[:11] + '[rotation=12]' + block[11:len(block)]
        elif direction == Direction.x_plus:
            block = block[:11] + '[rotation=4]' + block[11:len(block)]
        elif direction == Direction.z_plus:
            block = block[:11] + '[rotation=8]' + block[11:len(block)]
        command = f'setblock {x} {y} {z} minecraft:{block} replace'
        runCommand(command)

#material class that sends place_block as a summon command to minecraft, used mainly for placing entities
class SummonMaterial(Material):
    def __init__(self, block : Block) -> None:
        self.block = block

    def place_block(self, interface: Interface, x: int, y: int, z: int, direction=None, Seed: int=None):
        x, y, z = interface.local2global(x, y, z)
        block = self.block.name
        if direction == Direction.x_minus:
            self.block.nbt = self.block.nbt[:len(self.block.nbt)-1] + ',Rotation:[90.0f]}'
        elif direction == Direction.x_plus:
            self.block.nbt = self.block.nbt[:len(self.block.nbt)-1] + ',Rotation:[-90.0f]}'
        elif direction == Direction.z_minus:
            self.block.nbt = self.block.nbt[:len(self.block.nbt)-1] + ',Rotation:[180.0f]}'

        if not self.block.nbt:
            command = f'/summon minecraft:{block} {x} {y} {z}'
        else: 
            command = f'/summon minecraft:{block} {x} {y} {z} {self.block.nbt}'
        runCommand(command)
