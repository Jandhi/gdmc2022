from gdpc.interface import requestPlayerArea, Interface, setBuildArea
from gdpc.worldLoader import WorldSlice
from districts.blocks.bubble_generator import BubbleGenerator
from noise.random import set_seed
from noise.noise import recursive_hash
from noise.random_number_generator import RandomNumberGenerator

from shapely.geometry import Point
from shapely.geometry.polygon import Polygon
from pathfinding.pathfinder import get_path
from pathfinding.roadpaths import BRIDGE, ROAD, ROAD_SLAB, get_cost, create_get_neighbours_function
from terrain.watermap import get_water_map

area = list(requestPlayerArea(21, 21))
area[1] = 3
area[4] = 200
setBuildArea(*area)
set_seed(recursive_hash(*area))
slice = WorldSlice(area[0], area[2], area[3], area[5])

interface = Interface(area[0], 0, area[2], True)

hmap = slice.heightmaps['MOTION_BLOCKING_NO_LEAVES']

hmap = [[hmap[x + 1][z] for z in range(20)] for x in range(20)]
wmap = get_water_map(interface, hmap)

path = get_path(
    (0, hmap[0][0] - 1, 0, ROAD, 0),  
    (15, hmap[15][15] - 1, 15, ROAD, 0),
    create_get_neighbours_function(20, 20, slice, interface, wmap),
    get_cost,
    lambda node : (node[0], node[1], node[2]) == (15, hmap[15][15] - 1, 15)
)

for x, y, z, type, dir in path:
    block = {
        ROAD : 'cobblestone',
        ROAD_SLAB : 'cobblestone_slab',
        BRIDGE : 'oak_planks'
    }[type]

    if (x, z) == (0, 0) or (x, z) == (15, 15):
        block = 'red_wool'

    interface.placeBlock(x, y, z, block)

interface.sendBlocks()