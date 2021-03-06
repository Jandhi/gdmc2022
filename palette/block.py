from dataclasses import dataclass

from directions import Direction, add_directions

def create_block(name : str):
    is_log = name.endswith('log') or (name.endswith('stem') and name != 'mushroom_stem')

    return Block(name)

@dataclass
class Block:
    name : str
    attributes : dict[str, str] = None
    is_pillar : bool = False
    is_stairs : bool = False
    base_direction : str = None
    nbt : str = None

    def new(self):
        self.attributes = {}
        return self
    
    def set_attributes(self, attributes : dict[str, str]):
        self.attributes = attributes

    def set_facing(self, direction):
        true_direction = self.get_true_direction(direction)

        if not true_direction:
            return

        if self.is_pillar:
            self.__set_facing_pillar(true_direction)

        if self.is_stairs:
            return self.__set_facing_stairs(true_direction)
    
    def get_true_direction(self, direction):
        if not direction:
            return self.base_direction
        
        if not self.base_direction:
            return direction
        
        return add_directions(direction, self.base_direction)
    
    def __set_facing_stairs(self, direction):
        self.attributes['facing'] = Direction.cardinal_text[direction]
    
    def __set_facing_pillar(self, direction):
        axis = 'x'
        if direction in (Direction.y_plus, Direction.y_minus):
            axis = 'y'
        elif direction in (Direction.z_plus, Direction.z_minus):
            axis = 'z'
        
        self.attributes['axis'] = axis
    
    # this method is added in material.py to create material from block
    def material(self):
        pass

    def __str__(self) -> str:
        string = self.name

        if len(self.attributes) > 0:
            attrs = ''

            for attr in self.attributes:
                attrs += f',{attr}={self.attributes[attr]}'

            string = f'{string}[{attrs[1:]}]'
        
        return string