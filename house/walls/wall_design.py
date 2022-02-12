from house.grid import GridNode
from tools import setBlock

class WallDesign:
    block = 'stone_bricks'

    def generate_wall(self, node : GridNode, direction):
        pass

class BasicWall(WallDesign):
    def generate_wall(self, node : GridNode, direction):
        points = node.get_side_points([direction])
        x0, y0, z0 = node.get_origin()

        for x, y, z in points:
            setBlock(x0 + x, y0 + y, z0 + z, self.block)