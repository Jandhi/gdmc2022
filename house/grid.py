from directions import Direction
from vector import sum_vectors

class GridNode:
    def __init__(self, x, y, z, grid) -> None:
        self.x = x
        self.y = y
        self.z = z
        self.coords = (x, y, z)
        self.grid = grid
        self.width = grid.width
        self.height = grid.height
        self.depth = grid.depth

    def get_neighbour(self, direction):
        distance_vector = Direction.vectors[direction]
        coords = sum_vectors(distance_vector, self.coords)

        if coords in self.grid.nodes:
            return self.grid.nodes[coords]
        else:
            return None
    
    def get_neighbours(self) -> list:
        nodes = []
        for dx, dy, dz in [(1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1)]:
            x = self.x + dx
            y = self.y + dy
            z = self.z + dz
            if (x, y, z) in self.grid.nodes:
                nodes.append(self.grid.nodes[(x, y, z)])
        
        return nodes

    def get_origin(self) -> tuple[int, int, int]:
        x, y, z = self.grid.origin
        return (
            x + self.x * (self.grid.width - 1), 
            y + self.y * (self.grid.height - 1), 
            z + self.z * (self.grid.depth - 1)
        )
    
    def get_world_area(self) -> tuple[int, int, int, int, int, int]:
        x, y, z = self.get_origin()
        return (x, y, z, x + self.grid.width, y + self.grid.height, z + self.grid.depth)

    def get_side_points(self, directions) -> list[tuple[int, int, int]]:
        points = []

        x1, y1, z1 = 0, 0, 0
        x2, y2, z2 = self.width, self.height, self.depth

        if Direction.x_plus in directions:
            x1 = self.width - 1
        if Direction.x_minus in directions:
            x2 = x1 + 1
        if Direction.z_plus in directions:
            z1 = self.depth - 1
        if Direction.z_minus in directions:
            z2 = z1 + 1
        if Direction.y_plus in directions:
            y1 = self.height - 1
        if Direction.y_minus in directions:
            y2 = y1 + 1

        for x in range(x1, x2):
            for y in range(y1, y2):
                for z in range(z1, z2):
                    points.append((x, y, z))

        return points 

class Grid:
    nodes = {}

    def __init__(self, origin, size = (5, 5, 5)) -> None:
        self.origin = origin
        self.width, self.height, self.depth = size

    def add_node(self, x, y, z) -> GridNode:
        self.nodes[(x, y, z)] = GridNode(x, y, z, self)