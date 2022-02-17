from house.grid import GridNode
from palette.material import Material
from tools import setBlockMaterial

class WallDesign:
    def generate_wall(self, node : GridNode, direction):
        pass

class BasicWall(WallDesign):
    material = Material([
        ('stone_bricks', 12), 
        ('cobblestone', 6), 
        ('stone', 3),
        ('cracked_stone_bricks', 2),
        ('gravel', 1)
    ])

    def generate_wall(self, node : GridNode, direction):
        points = node.get_side_points([direction])
        x0, y0, z0 = node.get_origin()

        for x, y, z in points:
            setBlockMaterial(x0 + x, y0 + y, z0 + z, self.material)