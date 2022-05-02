from gdpc.interface import Interface

def get_water_map(interface : Interface, hmap):
    return [[is_water(interface, hmap, x, z) for z in range(len(hmap[0]))] for x in range(len(hmap))]

def is_water(interface : Interface, hmap, x, z):
    return interface.getBlock(x, hmap[x][z] - 1, z) in ['minecraft:water', 'minecraft:seagrass']