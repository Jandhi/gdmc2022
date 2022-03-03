from directions import Direction
from house.walls.wall_design import WallDesign
from house.grid import GridNode
from gdpc.interface import Interface

class WallPillarDesign(WallDesign):
    def generate_wall(self, interface : Interface, node : GridNode, direction):
        for rotation in (Direction.left, Direction.right):
            secondary_direction = rotation[direction]
            if node.get_neighbour(secondary_direction):
                self.generate_pillar(interface, node, direction, secondary_direction)
            else:
                self.generate_corner_pillar(interface, node, direction, secondary_direction)
    
    def generate_pillar(self, interface : Interface, node : GridNode, direction, secondary_direction):
        x0, y0, z0 = node.get_origin()
        x = 0
        z = 0

        if Direction.x_plus in (direction, secondary_direction):
            x = node.width - 1
        if Direction.z_plus in (direction, secondary_direction):
            z = node.depth - 1
        
        for y in range(1, node.height - 1):
            if y == 1:
                node.palette.wall_stairs.place_block(interface, x0 + x, y0 + y, z0 + z, Direction.opposite[direction], {'half': 'bottom'})
            elif y == node.height - 2:
                node.palette.wall_stairs.place_block(interface, x0 + x, y0 + y, z0 + z, Direction.opposite[direction], {'half': 'top'})
            else:
                node.palette.wall.place_block(interface, x0 + x, y0 + y, z0 + z, direction)

    def generate_corner_pillar(self, interface : Interface, node : GridNode, direction, secondary_direction):
        x0, y0, z0 = node.get_origin()
        x = 0
        z = 0

        if Direction.x_plus in (direction, secondary_direction):
            x = node.width - 1
        if Direction.z_plus in (direction, secondary_direction):
            z = node.depth - 1

        if secondary_direction == Direction.x_plus:
            x -= 1
        elif secondary_direction == Direction.x_minus:
            x += 1
        elif secondary_direction == Direction.z_plus:
            z -= 1
        elif secondary_direction == Direction.z_minus:
            z += 1

        for y in range(1, node.height - 1):
            if y == node.height - 2:
                node.palette.wall_stairs.place_block(interface, x0 + x, y0 + y, z0 + z, Direction.opposite[direction], {'half': 'top'})
            else:
                node.palette.wall_wall.place_block(interface, x0 + x, y0 + y, z0 + z)
