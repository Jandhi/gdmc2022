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
    wood : Material = BasicMaterial(Block('jungle_wood'))
    leaves : Material = BasicMaterial(Block(f'jungle_leaves[persistent=true]'))

    colour_list : list[str] = ('red', 'white', 'orange', 'magenta','light_blue', 'yellow', 'lime', 'pink', 'gray', 'light_gray', 'cyan',
    'blue', 'purple', 'brown', 'green', 'black')

    #market related items
    market_base : Material = BasicMaterial(Block('oak_planks'))
    market_fence : Material = BasicMaterial(Block('oak_fence'))
    market_fence_gate : Material = BasicMaterial(Block('oak_fence_gate'))
    market_trapdoor : Material = BasicMaterial(Block('oak_trapdoor'))
    market_campfire : Material = BasicMaterial(Block(f'campfire[lit=false]'))
    market_upside_down_stair : Material = BasicMaterial(Block(f'oak_stairs[half=top]'))
    market_stair : Material = BasicMaterial(Block(f'oak_stairs'))
    market_top_slab : Material = BasicMaterial(Block(f'oak_slab[type=top]'))