from house.grid import GridNode
from palette.material import Material
from gdpc.interface import Interface

class WallDesign:
    def generate_wall(self, node : GridNode, direction):
        pass

class BasicWall(WallDesign):
    def generate_wall(self, interface : Interface, node : GridNode, direction):
        points = node.get_side_points([direction])
        x0, y0, z0 = node.get_origin()

        for x, y, z in points:
            interface.placeBlock(x0 + x, y0 + y, z0 + z, 'red_terracotta')