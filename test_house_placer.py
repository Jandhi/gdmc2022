from gdpc.interface import requestPlayerArea, Interface, setBuildArea
from gdpc.worldLoader import WorldSlice
from noise.random import set_seed
from noise.noise import recursive_hash
from palette.sets.biome_sets import *
from terrain.buildmap import get_build_map
from terrain.watermap import get_water_map
from house.house_placer import HousePlacer

area = list(requestPlayerArea(50, 50))
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

HousePlacer(
    area=area, 
    grid_size=(7,5,7),
    slice=slice, 
    hmap=hmap, 
    omap=omap, 
    wmap=wmap, 
    bmap=bmap,
    point=(100,100),
    palette=create_palette(combine(
        desert_biome_set, 
        oak_biome_set
    ))
).attempt_placement((20, hmap[20][20], 20), interface)

interface.sendBlocks()