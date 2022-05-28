from dataclasses import dataclass
from directions import Direction
from palette.block import Block
from palette.material import Material, BasicMaterial

@dataclass
class Palette:
    fence : Material = Block('oak_fence').material()
    frame : Material = Block('oak_log', is_pillar=True).material()
    floor : Material = Block('oak_planks').material()
    roof : Material = Block('oak_log').material()
    wall : Material = Block('oak_planks').material()
    wall_stairs : Material = Block('oak_stairs', is_stairs=True).material()
    wall_fence : Material = Block('cobblestone_wall').material() # listen we gotta figure out a better naming system
    wall_accent : Material = Block('polished_andesite').material()
    trapdoor : Material = Block('oak_trapdoor').material()
    fence : Material = Block('oak_fence').material()
    roof_stairs : Material = Block('oak_stairs', is_stairs=True).material()
    roof_slab : Material = Block('oak_slab').material()