def filter_neighbours(point, points, hmap = None, wmap = None):
    x, z = point

    if hmap is not None:
        def is_not_water(point):
            px, pz = point

            if px >= len(hmap) or pz >= len(hmap[0]):
                return False

            return abs(hmap[px][pz] - hmap[x][z]) <= 1

        points = filter(is_not_water, points)

    if wmap is not None:
        def is_not_water(point):
            px, pz = point

            if px >= len(wmap) or pz >= len(wmap[0]):
                return False

            return not wmap[px][pz]

        points = filter(is_not_water, points)

    return points

def neighbours_2d(point, hmap = None, wmap = None):
    x, z = point
    points = [(x + 1, z), (x, z + 1), (x - 1, z), (x, z - 1)]
    return filter_neighbours(point, points, hmap, wmap)

def distance_2d(p1, p2):
    x1, z1 = p1
    x2, z2 = p2
    return ((x2 - x1) ** 2 + (z2 - z1) ** 2) ** 0.5

def distance_3d(p1, p2):
    x1, y1, z1 = p1
    x2, y2, z2 = p2
    return ((x2 - x1) ** 2 + (y2 - y1) ** 2 + (z2 - z1) ** 2) ** 0.5

def neighbours_2d_diagonal(point, hmap = None, wmap = None):
    x, z = point
    points = neighbours_2d(point) + [(x + 1, z + 1), (x + 1, z - 1), (x - 1, z + 1), (x - 1, z - 1)]
    return filter_neighbours(point, points, hmap, wmap)

def three_by_three(point):
    return set([
        (point[0] + 1, point[1] + 1), (point[0], point[1] + 1), (point[0] - 1, point[1] + 1),
        (point[0] + 1, point[1]), (point[0], point[1]), (point[0] - 1, point[1]),
        (point[0] + 1, point[1] - 1), (point[0], point[1] - 1), (point[0] - 1, point[1] - 1),
    ])

def in_bounds(point, map):
    return 0 <= point[0] < len(map) and 0 <= point[1] < len(map[0])