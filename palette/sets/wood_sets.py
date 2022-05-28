from palette.block import Block, create_block
from palette.sets.block_types import *


OAK = 'oak'
SPRUCE = 'spruce'
BIRCH = 'birch'
DARK_OAK = 'dark_oak'
JUNGLE = 'jungle'
ACACIA = 'acacia'
CRIMSON = 'crimson'
WARPED = 'warped'

woods = [
    OAK,
    SPRUCE,
    BIRCH,
    DARK_OAK,
    JUNGLE,
    ACACIA,
    CRIMSON,
    WARPED
]

wood_set_contents = {
    BLOCK : 'planks',
    STAIRS : 'stairs',
    SLAB : 'slab',
    DOOR : 'door',
    TRAPDOOR : 'trapdoor',
    SIGN : 'sign',
    FENCE : 'fence',
    FENCE_GATE : 'fence_gate',
    PRESSURE_PLATE : 'pressure_plate',
    BUTTON : 'button',
}

wood_sets = {
    wood : {
        block : create_block(f'{wood}_{wood_set_contents[block]}').material() for block in wood_set_contents
    } for wood in woods
}