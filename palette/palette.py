from dataclasses import dataclass
from directions import Direction
from palette.block import Block
from palette.material import Material, BasicMaterial

@dataclass
class Palette:
    fence : Material = BasicMaterial(Block('oak_fence'))
    frame : Material = BasicMaterial(Block('oak_log', is_log=True))
    floor : Material = BasicMaterial(Block('oak_planks'))
    roof : Material = BasicMaterial(Block('oak_log'))
    wall : Material = BasicMaterial(Block('oak_planks'))
    wood : Material = BasicMaterial(Block('birch_wood'))
    leaves : Material = BasicMaterial(Block(f'birch_leaves[persistent=true]'))