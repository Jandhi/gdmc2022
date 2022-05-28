from terrain.buildmap import NOTHING, ROAD
from util.point_utils import three_by_three, in_bounds

def find_edges(bmap, hmap):
    edges = set()

    for x in range(len(bmap)):
        for z in range(len(bmap)):
            if bmap[x][z] == NOTHING:
                __test_edge(x, z, edges, bmap, hmap)

    return edges

def __test_edge(x, z, edges, bmap, hmap):
    for px, pz in three_by_three((x, z)):
        if in_bounds((px, pz), bmap) and bmap[px][pz] == ROAD:
            y = hmap[px][pz] - 1
            return edges.add((x, y, z))