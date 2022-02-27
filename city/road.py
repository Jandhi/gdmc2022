from house.grid import Grid
from palette.block import Block
from palette.material import BasicMaterial
from palette.palette import Palette

class Road:
    palette: Palette

    #p1 and p2 are the starting and end points of the rectangle that forms the road
    def __init__(self, p1, y, p2) -> None:
        self.p1 = p1
        self.y = y
        self.p2 = p2

        self.palette = Palette(floor=Block('black_terracotta').material())

    def get_road(self) -> tuple[(int, int), int, (int, int)]:
        return [self.p1, self.y, self.p2]

    def get_road_points(self) -> list[tuple[int, int, int]]:
        points = []
        x1 = self.p1[0]
        z1 = self.p1[1]
        x2 = self.p2[0]
        z2 = self.p2[1]
        for x in range(x1, x2):
            for z in range(z1, z2):
                points.append([x,self.y,z])
        return points