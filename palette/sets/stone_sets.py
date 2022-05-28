from re import M
from palette.block import create_block
from palette.sets.block_types import *
from palette.material import BasicMaterial

def make_set(dict):
    return {name : BasicMaterial(create_block(block)) for name, block in dict.items()}

# BASIC

stone_set = make_set({
    BLOCK : 'stone',
    DECORATED : 'polished_andesite',
    CRACKED : 'cobblestone',
    STAIRS : 'stone_stairs',
    SLAB : 'stone_slab',
    PRESSURE_PLATE : 'stone_pressure_plate',
    BUTTON : 'stone_button',
})

cobblestone_set = make_set({
    BLOCK : 'cobblestone',
    STAIRS : 'cobblestone_stairs',
    SLAB : 'cobblestone_slab',
    FENCE : 'cobblestone_wall'
})

mossy_cobblestone_set = make_set({
    BLOCK : 'mossy_cobblestone',
    STAIRS : 'mossy_cobblestone_stairs',
    SLAB : 'mossy_cobblestone_slab',
    FENCE : 'mossy_cobblestone_wall'
})

smooth_stone_set = make_set({
    BLOCK : 'smooth_stone',
    SLAB : 'smooth_stone_slab'
})

stone_bricks_set = make_set({
    BLOCK : 'stone_bricks',
    CRACKED : 'cracked_stone_bricks',
    DECORATED : 'chiseled_stone_bricks',
    STAIRS : 'stone_brick_stairs',
    SLAB : 'stone_brick_slab',
    FENCE : 'stone_brick_wall'
})

mossy_stone_bricks_set = make_set({
    BLOCK : 'mossy_stone_bricks',
    CRACKED : 'cracked_stone_bricks',
    DECORATED : 'chiseled_stone_bricks',
    STAIRS : 'mossy_stone_brick_stairs',
    SLAB : 'mossy_stone_brick_slab',
    FENCE : 'mossy_stone_brick_wall'
})

# SANDSTONE

smooth_sandstone_set = make_set({
    BLOCK : 'smooth_sandstone',
    DECORATED : 'chiseled_sandstone',
    CRACKED : 'sandstone',
    PILLAR : 'cut_sandstone',
    STAIRS : 'smooth_sandstone_stairs',
    SLAB : 'smooth_sandstone_slab',
    FENCE : 'sandstone_wall',
})

sandstone_set = make_set({
    BLOCK : 'sandstone',
    DECORATED : 'chiseled_sandstone',
    PILLAR : 'cut_sandstone',
    STAIRS : 'sandstone_stairs',
    SLAB : 'sandstone_slab',
    FENCE : 'sandstone_wall',
})

cut_sandstone_set = make_set({
    BLOCK : 'cut_sandstone',
    DECORATED : 'chiseled_sandstone',
    CRACKED : 'sandstone',
    PILLAR : 'cut_sandstone',
    STAIRS : 'smooth_sandstone_stairs',
    SLAB : 'cut_sandstone_slab',
    FENCE : 'sandstone_wall',
})

smooth_red_sandstone_set = make_set({
    BLOCK : 'smooth_red_sandstone',
    DECORATED : 'chiseled_red_sandstone',
    CRACKED : 'red_sandstone',
    PILLAR : 'cut_red_sandstone',
    STAIRS : 'smooth_red_sandstone_stairs',
    SLAB : 'smooth_red_sandstone_slab',
    FENCE : 'red_sandstone_wall',
})

red_sandstone_set = make_set({
    BLOCK : 'red_sandstone',
    DECORATED : 'chiseled_red_sandstone',
    PILLAR : 'cut_red_sandstone',
    STAIRS : 'red_sandstone_stairs',
    SLAB : 'red_sandstone_slab',
    FENCE : 'red_sandstone_wall',
})

cut_red_sandstone_set = make_set({
    BLOCK : 'cut_red_sandstone',
    DECORATED : 'chiseled_red_sandstone',
    CRACKED : 'red_sandstone',
    PILLAR : 'cut_red_sandstone',
    STAIRS : 'smooth_red_sandstone_stairs',
    SLAB : 'cut_red_sandstone_slab',
    FENCE : 'red_sandstone_wall',
})

