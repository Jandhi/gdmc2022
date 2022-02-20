from house.decoration.flag_generator import FlagGenerator
from house.grid import Grid
from house.frame_generator import FrameGenerator
from house.floor_generator import FloorGenerator
from clear import Clear
from checkerboard import CheckerBoardGenerator
from house.roof.roof_generator import RoofGenerator
from house.roof.tower_roof import TowerRoofGenerator
from house.walls.wall_generator import WallGenerator
from gdpc.interface import requestPlayerArea, Interface, setBuildArea

MULTI = True

area = list(requestPlayerArea(66, 66))
area[1] = 3
area[4] = 200
setBuildArea(*area)

interface = Interface(area[0], 0, area[2], True)

grid = Grid((1, 3, 1), (5, 7, 5))
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

Clear(interface=interface, height_limit=32, area=(0, 0, 66, 66), y=4).generate()
CheckerBoardGenerator(interface=interface, tile_width=grid.width, tile_depth=grid.depth, area=(1, 1, 65, 65), y=3).generate()

WallGenerator(interface=interface, grid=grid).generate()
RoofGenerator(interface=interface, grid=grid).generate()
FrameGenerator(interface=interface, grid=grid).generate()
FloorGenerator(interface=interface, grid=grid).generate()
FlagGenerator(interface=interface, grid=grid).generate()
TowerRoofGenerator(interface=interface, node=grid.nodes[(0, 1, 4)],y_offset=grid.height).generate()