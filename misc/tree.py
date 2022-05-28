from house.grid import Grid
from palette.block import Block
from palette.material import BasicMaterial
from palette.palette_old import Palette

class Tree:
    palette: Palette

    #p1 and p2 are the starting and end points of the rectangle that forms the road
    def __init__(self, origin, type) -> None:
        self.origin = origin
        self.type = type

        self.palette = Palette(floor=Block('black_terracotta').material())

    def get_origin(self):
        return self.origin

    