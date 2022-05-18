from gdpc.interface import Interface
from gdpc.worldLoader import WorldSlice

def get_water_map(hmap, slice : WorldSlice, origin):
    return [[is_water(hmap, x, z, slice, origin) for z in range(len(hmap[0]))] for x in range(len(hmap))]

def is_water(hmap, x, z, slice, origin):
    block = slice.getBlockAt(
        x + origin[0], 
        hmap[x][z] - 1,
        z + origin[2])

    return block in [
        'minecraft:water',
        'minecraft:seagrass',
        'minecraft:tall_seagrass'
    ]