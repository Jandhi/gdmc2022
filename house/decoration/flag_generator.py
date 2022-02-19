from random import choice, shuffle
from directions import Direction
from house.walls.wall_design import BasicWall
from tools import setBlock
from generator import Generator
from house.grid import Grid, GridNode
from vector import multiply_vector, sum_vectors

class FlagGenerator(Generator):
    name = 'Flag Generator'
    grid : Grid = None
    design = None

    def __generate__(self):
        if not self.grid:
            return
        
        self.generate_for_node(self.get_highest_node())

    def get_highest_node(self) -> GridNode:
        nodes = list(self.grid.nodes.values())
        shuffle(nodes)
        def height(node):
            return node.y
        return max(nodes, key=height) 

    def generate_for_node(self, node : GridNode):
        x0, y0, z0 = node.get_origin()
        x, z = node.width // 2, node.depth // 2
        
        # random wool
        wool_color = choice(['red_wool', 'orange_wool', 'magenta_wool', 'blue_wool', 'green_wool'])
        
        # wind
        primary_wind_direction = choice(Direction.cardinal)
        is_adjacent = lambda direction : direction != primary_wind_direction and direction != Direction.opposite[primary_wind_direction]
        secondary_wind_direction = choice(list(filter(is_adjacent, Direction.cardinal)))
        primary_vector = Direction.vectors[primary_wind_direction]
        secondary_vector = Direction.vectors[secondary_wind_direction]

        for y in range(0, 7):
            # pole
            px, py, pz = x + x0, y + y0 + node.height, z + z0
            center = (px, py, pz)
            setBlock(px, py, pz, 'spruce_log' if y == 0 else 'spruce_fence')

            def setRelative(vector, color):
                setBlock(vector[0], vector[1], vector[2], f'{color}_wool')

            mv = multiply_vector

            # flag
            if y == 4:
                setRelative(sum_vectors(center, primary_vector), 'red')
                setRelative(sum_vectors(center, mv(primary_vector, 2), secondary_vector), 'green')
                setRelative(sum_vectors(center, mv(primary_vector, 3), mv(secondary_vector, 2)), 'green')
                setRelative(sum_vectors(center, mv(primary_vector, 4), mv(secondary_vector, 3)), 'green')
            elif y == 5:
                setRelative(sum_vectors(center, primary_vector), 'red')
                setRelative(sum_vectors(center, mv(primary_vector, 2), secondary_vector), 'red')
                setRelative(sum_vectors(center, mv(primary_vector, 3), secondary_vector), 'white')
                setRelative(sum_vectors(center, mv(primary_vector, 4), mv(secondary_vector, 2)), 'white')
            elif y == 6:
                setRelative(sum_vectors(center, primary_vector), 'red')
                setRelative(sum_vectors(center, mv(primary_vector, 2), secondary_vector), 'black')
                setRelative(sum_vectors(center, mv(primary_vector, 3), secondary_vector), 'black')
                setRelative(sum_vectors(center, mv(primary_vector, 4), mv(secondary_vector, 2)), 'black')
