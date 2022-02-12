from house.decoration.flag_generator import FlagGenerator
from house.grid import Grid
from house.frame_generator import FrameGenerator
from house.floor_generator import FloorGenerator
from clear import Clear
from checkerboard import CheckerBoardGenerator
from house.roof.roof_generator import RoofGenerator
from house.roof.tower_roof import TowerRoofGenerator
from house.walls.wall_generator import WallGenerator

grid = Grid((0, 3, 0), (20, 20, 20))
grid.add_node(0, 0, 0)
grid.add_node(0, 0, 1)
grid.add_node(1, 0, 0)
grid.add_node(0, 1, 0)
grid.add_node(2, 0, 0)

grid.add_node(3, 0, 3)
grid.add_node(3, 1, 3)
grid.add_node(3, 2, 3)

grid.add_node(4, 0, 0)
grid.add_node(4, 0, 1)

grid.add_node(0, 0, 4)
grid.add_node(0, 1, 4)
grid.add_node(1, 0, 4)

grid.add_node(0, 5, 0)


Clear(height_limit=32, area=(-1, -1, 64, 64), y=4).generate()
CheckerBoardGenerator(tile_width=grid.width, tile_depth=grid.depth, area=(0, 0, 64, 64), y=3).generate()
WallGenerator(grid=grid).generate()
RoofGenerator(grid=grid).generate()
FrameGenerator(grid=grid).generate()
FloorGenerator(grid=grid).generate()
FlagGenerator(grid=grid).generate()
TowerRoofGenerator(node=grid.nodes[(0, 1, 4)],y_offset=grid.height).generate()