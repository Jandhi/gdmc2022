from gdpc.interface import requestPlayerArea, Interface, setBuildArea
from gdpc.worldLoader import WorldSlice
from districts.blocks.bubble_generator import BubbleGenerator
from districts.edge_finder import find_edges
from house.house_placer import HousePlacer
from noise.random import set_seed
from noise.noise import recursive_hash
from palette.block import Block
from palette.material import MixedMaterial
from pathfinding.pathfinder import get_path
from pathfinding.roadpaths import BRIDGE, ROAD, ROAD_SLAB, get_cost, create_get_neighbours_function
from terrain.buildmap import get_build_map
from terrain.watermap import get_water_map
from gdpc.direct_interface import runCommand

area = list(requestPlayerArea(200, 200))
area[1] = 3
area[4] = 200
origin = (area[0], area[1], area[2])
setBuildArea(*area)
set_seed(recursive_hash(*area))
slice = WorldSlice(area[0], area[2], area[3], area[5])

interface = Interface(area[0], 0, area[2], True)

hmap = slice.heightmaps['MOTION_BLOCKING_NO_LEAVES']
omap = slice.heightmaps['OCEAN_FLOOR']
wmap = get_water_map(hmap, slice, origin)   
bmap = get_build_map(hmap)

mixed_road = MixedMaterial(
    [
        Block('cobblestone').material(),
        Block('gravel').material(),
        Block('stone').material(),
        Block('stone_bricks').material()
    ]
)

mixed_slab = MixedMaterial(
    [
        Block('cobblestone_slab').material(),
        Block('stone_slab').material(),
        Block('stone_brick_slab').material()
    ]
)

BubbleGenerator(
    area=area, 
    hmap=hmap, 
    wmap=wmap, 
    bmap=bmap, 
    omap=omap,
    slice=slice,
    point_amount=20,
    road_material=mixed_road,
    slab_material=mixed_slab,
).generate(interface)

edges = find_edges(bmap)

for point in edges:
    HousePlacer(area=area, hmap=hmap, wmap=wmap, bmap=bmap).attempt_placement(point, interface)

interface.sendBlocks()