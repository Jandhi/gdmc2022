from directions import Direction
from vector import sum_vectors
from util.point_utils import distance_2d, distance_3d, neighbours_2d

ROAD = 0
ROAD_SLAB = 1
BRIDGE = 2

def create_get_neighbours_function(width, depth, hmap, interface, wmap):
    def get_neighbours(node):
        neighbours = []
        x, y, z, type, dir = node
        
        
        if type != BRIDGE:
            for px, pz in neighbours_2d((x, z)):
                if not (0 <= px < width and 0 <= pz < depth):
                    continue

                py = hmap[px][pz] - 1
                pdir = Direction.x_plus
                is_water = wmap[px][pz]

                if px < x:
                    pdir = Direction.x_minus
                elif pz > z:
                    pdir = Direction.z_plus
                elif pz < z:
                    pdir = Direction.z_minus

                if py == y:
                    if type == ROAD and not is_water:
                        neighbours.append((px, py, pz, ROAD, 0))
                        neighbours.append((px, py + 1, pz, ROAD_SLAB, 0))
                    elif type == ROAD_SLAB and not is_water:
                        neighbours.append((px, py, pz, ROAD, 0))
                    elif is_water:
                        neighbours.append((px, py, pz, BRIDGE, pdir))
                elif py == y - 1:
                    if type == ROAD and not is_water:
                        neighbours.append((px, py + 1, pz, ROAD_SLAB, 0))
                    elif type == ROAD_SLAB and not is_water:
                        neighbours.append((px, py, pz, ROAD, 0))
                    
                    neighbours.append((px, py + 1, pz, BRIDGE, pdir))
                elif py < y:
                    neighbours.append((px, y, pz, BRIDGE, pdir))
        else:
            dir_vector = Direction.vectors[dir]
            px, py, pz = sum_vectors((x, y, z), dir_vector)

            if not (0 <= px < width and 0 <= pz < depth):
                return neighbours

            is_water = wmap[px][pz]

            ground_y = hmap[px][pz] - 1

            if ground_y < py:
                neighbours.append((px, py, pz, BRIDGE, dir))
            elif ground_y == py:
                if not is_water:
                    neighbours.append((px, py, pz, ROAD, 0))
                    neighbours.append((px, py + 1, pz, ROAD_SLAB, 0))
                else:
                    neighbours.append((px, py, pz, BRIDGE, dir))

        return neighbours

    return get_neighbours

def get_cost(path, end_node):
    return len(path) \
        + distance_3d(
            (path[-1][0], path[-1][1], path[-1][2]), 
            (end_node[0], end_node[1], end_node[2])
        ) \
        + sum([node[3] == BRIDGE for node in path]) \
        + 0.3 * sum([node[3] == ROAD_SLAB for node in path]) \
        + collision_cost(path)

def collision_cost(path):
    xzs = set()

    for node in path:
        (x, z) = node[0], node[2]

        if (x, z) in xzs:
            return 100
        else:
            xzs.add((x, z))

    return 0