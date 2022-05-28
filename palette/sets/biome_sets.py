from noise.random import choose
from palette.design.design import ROOF_DESIGN
from palette.design.roof_designs import BALCONY, DOME, FLAT
from palette.sets.set_categories import ROOF, WALL, STONE, WOOD
from palette.sets.stone_sets import sandstone_set, cut_sandstone_set, smooth_sandstone_set
from palette.sets.wood_sets import BIRCH, JUNGLE, OAK, WARPED, wood_sets
from palette.palette import *

desert_biome_set = {
    WALL : [
        {
            WALL_PRIMARY : smooth_sandstone_set, 
            WALL_SECONDARY : cut_sandstone_set
        }, 
    ],
    STONE : [
        {
            STONE : smooth_sandstone_set, 
            STONE_ACCENT : cut_sandstone_set
        },
        {
            STONE : sandstone_set,
            STONE_ACCENT : cut_sandstone_set
        } 
    ],
    WOOD : [
        {
            WOOD : wood_sets[BIRCH],
            WOOD_ACCENT : wood_sets[OAK],
        },
        {
            WOOD : wood_sets[BIRCH],
            WOOD_ACCENT : wood_sets[JUNGLE],
        }
    ],
    ROOF : [
        {
            ROOF_PRIMARY : wood_sets[WARPED],
            ROOF_DESIGN : DOME
        },
        {
            ROOF_DESIGN : FLAT
        },
        {
            ROOF_DESIGN : BALCONY
        },
        {
            ROOF_DESIGN : DOME
        }
    ],
    FLOOR : [
        {},
        {},
        {
            FLOOR : smooth_sandstone_set
        }
    ]
}

def combine(*biome_sets):
    total = {}
    
    for set in biome_sets:
        for category, list in set:
            if category not in total:
                total[category] = list
            else:
                total[category] += list
    
    return total

def narrow(set):
    total = {}

    for category, palette_list in set:
        palette_list : list
        if len(list) <= 2:
            total[category] = palette_list
        else:
            copied = palette_list.copy()
            item1 = choose(hash('narrow1'), copied)
            copied.remove(item1)
            item2 = choose(hash('narrow2'), copied)
            total[category] = [item1, item2]
    
    return total

def create_palette(set):
    data = {}

    for category, palette_list in set.items():
        item_list : dict = choose(hash('palette'), palette_list)

        for name, value in item_list.items():
            data[name] = value

    return Palette(data)