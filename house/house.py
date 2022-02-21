from house.grid import Grid
from palette.block import Block
from palette.material import BasicMaterial
from palette.palette import Palette

class House:
    grid : Grid
    receded_ground_floor : bool = True

    def __init__(self, grid : Grid) -> None:
        self.grid = grid

        upper_palette = Palette(wall=Block('sandstone').material())
        lower_palette = Palette(wall=Block('end_stone_bricks').material())

        for node in self.grid.nodes.values():
            node.palette = lower_palette if node.y == 0 else upper_palette