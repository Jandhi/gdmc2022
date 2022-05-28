from gdpc.interface import requestPlayerArea, Interface, setBuildArea
from gdpc.worldLoader import WorldSlice
from noise.random import set_seed
from noise.noise import recursive_hash
from pathfinding.pathfinder import get_path
from pathfinding.roadpaths import BRIDGE, ROAD, ROAD_SLAB, get_cost, create_get_neighbours_function
from terrain.watermap import get_water_map

area = list(requestPlayerArea(50, 50))
area[1] = 3
area[4] = 200
setBuildArea(*area)
set_seed(recursive_hash(*area))
slice = WorldSlice(area[0], area[2], area[3], area[5])

interface = Interface(area[0], 0, area[2], True)

hmap = slice.heightmaps['MOTION_BLOCKING_NO_LEAVES']
wmap = get_water_map(hmap, slice)

tx, tz = (19, 19)

path = get_path(
    (0, hmap[0][0] - 1, 0, ROAD, 0),  
    (tx, hmap[tx][tz] - 1, tz, ROAD, 0),
    create_get_neighbours_function(20, 20, hmap, interface, wmap),
    get_cost,
    lambda node : (node[0], node[1], node[2]) == (tx, hmap[tx][tz] - 1, tz)
)

for x, y, z, type, dir in path:
    block = {
        ROAD : 'cobblestone',
        ROAD_SLAB : 'cobblestone_slab',
        BRIDGE : 'oak_planks'
    }[type]

    if (x, z) == (0, 0) or (x, z) == (tx, tz):
        block = 'red_wool'

    interface.placeBlock(x, y, z, block)

interface.sendBlocks()