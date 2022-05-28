from house.grid import Grid
from palette.block import Block
from palette.material import BasicMaterial, MixedMaterial, WeightedMaterial
from palette.palette_old import Palette
from palette.sets.biome_sets import create_palette, desert_biome_set

class House:
    grid : Grid
    has_receded_ground_floor : bool
    has_frame : bool

    def __init__(self, grid : Grid) -> None:
        self.grid = grid
        self.has_receded_ground_floor = True
        self.has_frame = False

        self.palette = create_palette(desert_biome_set)

        for node in self.grid.nodes.values():
            node.palette = self.palette