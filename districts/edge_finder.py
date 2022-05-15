from terrain.buildmap import NOTHING, ROAD
from util.point_utils import three_by_three, in_bounds

def find_edges(bmap):
    edges = set()

    for x in range(len(bmap)):
        for z in range(len(bmap)):
            if bmap[x][z] == NOTHING and any(
                [in_bounds((px, pz), bmap) and bmap[px][pz] == ROAD for px, pz in three_by_three((x, z))]
            ):
                edges.add((x, z))

    return edges