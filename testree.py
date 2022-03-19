from house.decoration.flag_generator import FlagGenerator
from house.grid import Grid
from house.frame_generator import FrameGenerator
from house.floor_generator import FloorGenerator
from clear import Clear
from checkerboard import CheckerBoardGenerator
from house.house import House
from house.roof.roof_generator import RoofGenerator
from house.roof.tower_roof import TowerRoofGenerator
from house.walls.wall_generator import WallGenerator
from misc.tree import Tree
from city.city import City
from misc.tree_generator import TreeGenerator
from gdpc.interface import requestPlayerArea, Interface, setBuildArea

size_x = 200
size_z = 200

area = list(requestPlayerArea(size_x, size_z))
area[1] = 3
area[4] = 200
setBuildArea(*area)

interface = Interface(area[0], 0, area[2], True)

city = City((1,1), 3, (200,200))
#city.add_tree((100, 4, 100),"large_birch")
#city.add_tree((80, 4, 120),"")
#city.add_tree((80, 4, 80),"")
#city.add_tree((90, 4, 90),"")
#city.add_tree((70, 4, 77),"")
city.add_random_trees(500, 5)
#CheckerBoardGenerator(tile_width=5, tile_depth=5, area=(1, 1, size_x, size_z), y=3).generate(interface)

TreeGenerator(city=city).generate(interface)