from directions import Direction
from house.grid import GridNode
from gdpc.interface import Interface
from palette.palette import WALL_PRIMARY, WALL_SECONDARY
from palette.sets.block_types import BLOCK

from vector import sum_vectors

class WallDesign:
    def generate_wall(self, interface : Interface, node : GridNode, direction):
        pass

class BasicWall(WallDesign):
    def generate_wall(self, interface : Interface, node : GridNode, direction):
        points = node.get_side_points([direction])
        x0, y0, z0 = node.get_origin()

        for x, y, z in points:
            node.palette.get_material(WALL_PRIMARY, BLOCK).place_block(interface, x0 + x, y0 + y, z0 + z)     

class RecededWall(WallDesign):
    def generate_wall(self, interface : Interface, node : GridNode, direction):
        points = node.get_side_points([direction])
        x0, y0, z0 = node.get_origin()

        for point in points:
            diffVector = Direction.vectors[Direction.opposite[direction]]
            x, y, z = sum_vectors(point, diffVector)

            material = node.palette.get_material(WALL_PRIMARY, BLOCK) if y != 1 else node.palette.get_material(WALL_SECONDARY, BLOCK)

            if x == 0 and not node.get_neighbour(Direction.x_minus):
                continue
            if z == 0 and not node.get_neighbour(Direction.z_minus):
                continue
            if x == node.width - 1 and not node.get_neighbour(Direction.x_plus):
                continue
            if z == node.depth - 1 and not node.get_neighbour(Direction.z_plus):
                continue

            material.place_block(interface, x0 + x, y0 + y, z0 + z)