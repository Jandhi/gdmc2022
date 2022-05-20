from palette.sets.blocks import *

woods = [
    'oak',
    'spruce',
    'birch',
    'dark_oak',
    'jungle',
    'acacia',
    'crimson',
    'warped'
]

wood_set = {
    block : 'planks',
    stairs : 'stairs',
    slab : 'slab',
    door : 'door',
    trapdoor : 'trapdoor',
    sign : 'sign',
    fence : 'fence',
    fence_gate : 'fence_gate',
    pressure_plate : 'pressure_plate'
}

wood_sets = {
    wood : {
        block : f'{wood}_{block}' for block in wood_set
    } for wood in woods
}