NOTHING = 0
ROAD = 1
HOUSE = 2

def get_build_map(hmap):
    return [[NOTHING for z in range(len(hmap[0]))] for x in range(len(hmap))]