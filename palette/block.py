from dataclasses import dataclass

from directions import Direction, add_directions

@dataclass
class Block:
    name : str
    is_log : bool = False
    base_direction : str = None

    def get_facing(self, direction):
        true_direction = self.get_true_direction(direction)

        if not true_direction:
            return self.name

        if self.is_log:
            return self.__get_facing_log(true_direction)
        
        return self.name
    
    def get_true_direction(self, direction):
        if not direction:
            return self.base_direction
        
        if not self.base_direction:
            return direction
        
        return add_directions(direction, self.base_direction)
    
    def __get_facing_log(self, direction):
        axis = 'x'
        if direction in (Direction.y_plus, Direction.y_minus):
            axis = 'y'
        elif direction in (Direction.z_plus, Direction.z_minus):
            axis = 'z'
        
        return f'{self.name}[axis={axis}]'