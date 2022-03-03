class Axis:
    X = 'X'
    Y = 'Y'
    Z = 'Z'

class Direction:
    x_plus = 'x_plus'
    x_minus = 'x_minus'
    y_plus = 'y_plus'
    y_minus = 'y_minus'
    z_plus = 'z_plus'
    z_minus = 'z_minus'

    all = {x_plus, x_minus, y_plus, y_minus, z_plus, z_minus}

    north = z_minus
    east = x_plus
    south = z_plus
    west = x_minus
    up = y_plus
    down = y_minus

    cardinal = (north, east, south, west)

    opposite = {
        x_plus : x_minus,
        x_minus : x_plus,
        y_plus : y_minus,
        y_minus : y_plus,
        z_plus : z_minus,
        z_minus : z_plus
    }

    vectors = {
        x_plus : (1, 0, 0),
        x_minus : (-1, 0, 0),
        y_plus : (0, 1, 0),
        y_minus : (0, -1, 0),
        z_plus : (0, 0, 1),
        z_minus : (0, 0, -1)
    }

    cardinal_text = {
        north : 'north',
        east : 'east',
        south : 'south',
        west : 'west'
    }

    forwards = {
        north : north,
        east : east,
        south : south,
        west: west
    }
    right = {
        north: east,
        east: south,
        south: west,
        west: north,
    }
    left = {
        north: west,
        west: south,
        south: east,
        east: north
    }
    backwards = opposite

# adds directions as if block originally faced up
def add_directions(dir1, dir2):
    if dir1 == Direction.y_plus:
        return dir2
    elif dir1 == Direction.y_minus:
        return Direction.opposite[dir2]
    elif dir1 == Direction.x_plus:
        return {
            Direction.y_plus : Direction.x_plus,
            Direction.x_plus : Direction.y_minus,
            Direction.y_minus : Direction.x_minus,
            Direction.x_minus : Direction.y_plus,
            Direction.z_plus : Direction.z_plus,
            Direction.z_minus : Direction.z_minus
        }[dir2]
    elif dir1 == Direction.x_minus:
        return {
            Direction.y_plus : Direction.x_minus,
            Direction.x_minus : Direction.y_minus,
            Direction.y_minus: Direction.x_plus,
            Direction.x_plus: Direction.y_plus,
            Direction.z_plus : Direction.z_plus,
            Direction.z_minus : Direction.z_minus
        }[dir2]
    elif dir1 == Direction.z_plus:
        return {
            Direction.z_minus : Direction.y_plus,
            Direction.y_plus : Direction.z_plus,
            Direction.z_plus : Direction.y_minus,
            Direction.y_minus : Direction.z_minus,
            Direction.x_plus : Direction.x_plus,
            Direction.x_minus : Direction.x_minus,
        }[dir2]
    elif dir1 == Direction.z_minus:
        return {
            Direction.z_plus : Direction.y_plus,
            Direction.y_plus : Direction.z_minus,
            Direction.z_minus : Direction.y_minus,
            Direction.y_minus : Direction.z_plus,
            Direction.x_plus : Direction.x_plus,
            Direction.x_minus : Direction.x_minus,
        }[dir2]