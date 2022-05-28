from gdpc.interface import requestPlayerArea, Interface, setBuildArea
from gdpc.worldLoader import WorldSlice
from noise.random import set_seed
from noise.noise import recursive_hash
from terrain.buildmap import get_build_map
from terrain.watermap import get_water_map
from pathfinding.highway_generator import HighwayGenerator
from palette.material import MixedMaterial
from palette.block import Block

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

tx, tz = (48, 48)

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

HighwayGenerator(
    area=area, 
    hmap=hmap, 
    wmap=wmap, 
    bmap=bmap,
    p1=(0,0), 
    p2=(tx,tz),
    road_material = Block('bricks').material(),
    slab_material = Block('brick_slab').material(),
    bridge_material = MixedMaterial(
        [Block('oak_planks').material()]
    ),
    bridge_slab_material = Block('oak_slab').material(),
).generate(interface)

interface.sendBlocks()