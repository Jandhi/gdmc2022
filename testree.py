from gdpc.worldLoader import WorldSlice
from noise.noise import recursive_hash
from misc.tree import Tree
from city.city import City
from misc.tree_generator import TreeGenerator
from gdpc.interface import requestPlayerArea, Interface, setBuildArea
from noise.random import set_seed
from terrain.buildmap import get_build_map
from terrain.watermap import get_water_map

size_x = 200
size_z = 200

area = list(requestPlayerArea(size_x, size_z))
area[1] = 3
area[4] = 210
origin = (area[0], area[1], area[2])
setBuildArea(*area)
set_seed(recursive_hash(*area))
slice = WorldSlice(area[0], area[2], area[3], area[5])

interface = Interface(area[0], 0, area[2], True)

hmap = slice.heightmaps['MOTION_BLOCKING_NO_LEAVES']
omap = slice.heightmaps['OCEAN_FLOOR']
wmap = get_water_map(hmap, slice, origin)   
bmap = get_build_map(hmap)

city = City((1,1), hmap, wmap, (200,200))
#city.add_tree((100, 4, 100),"mega_jungle")
#city.add_tree((100, 4, 98),"small_baobab")
#city.add_tree((99, 4, 99),"small_baobab")
#city.add_tree((101, 4, 99),"small_baobab")
#city.add_tree((100, 4, 101),"medium_baobab")
#city.add_tree((101, 4, 101),"medium_baobab")
#city.add_tree((101, 4, 100),"medium_baobab")
#city.add_tree((80, 4, 120),"")
#city.add_tree((80, 4, 80),"")
#city.add_tree((90, 4, 90),"")
#city.add_tree((70, 4, 77),"")
city.add_random_trees(500, 5)
#CheckerBoardGenerator(tile_width=5, tile_depth=5, area=(1, 1, size_x, size_z), y=3).generate(interface)

TreeGenerator(city=city).generate(interface)