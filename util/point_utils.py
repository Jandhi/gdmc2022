def neighbours_2d(point):
    x, z = point
    return [(x + 1, z), (x, z + 1), (x - 1, z), (x, z - 1)]

def distance_2d(p1, p2):
    x1, z1 = p1
    x2, z2 = p2
    return ((x2 - x1) ** 2 + (z2 - z1) ** 2) ** 0.5

def neighbours_2d_diagonal(point):
    x, z = point
    return neighbours_2d(point) + [(x + 1, z + 1), (x + 1, z - 1), (x - 1, z + 1), (x - 1, z - 1)]