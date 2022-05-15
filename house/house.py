from house.grid import Grid
from palette.block import Block
from palette.material import BasicMaterial, MixedMaterial, WeightedMaterial
from palette.palette import Palette

class House:
    grid : Grid
    has_receded_ground_floor : bool
    has_frame : bool

    def __init__(self, grid : Grid) -> None:
        self.grid = grid
        self.has_receded_ground_floor = True
        self.has_frame = False

        wall = Block('white_wool').material()
        floor = Block('birch_planks').material()

        upper_palette = Palette(
            wall=wall, 
            trapdoor=Block('birch_trapdoor').material(),
            fence=Block('birch_fence').material(),
            floor=floor,
            roof_stairs=Block('warped_stairs', is_stairs=True).material(),
            roof_slab=Block('warped_slab').material()
        )
        lower_palette = Palette(
            wall=wall, 
            wall_stairs=Block('end_stone_brick_stairs', is_stairs=True).material(),
            wall_fence=Block('end_stone_brick_wall').material(),
            wall_accent=WeightedMaterial([
                (Block('cut_sandstone').material(), 10),
                (Block('sandstone').material(), 1)
            ]),
            floor=floor,
        )

        for node in self.grid.nodes.values():
            node.palette = lower_palette if node.y == 0 else upper_palette