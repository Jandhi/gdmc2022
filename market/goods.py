from dataclasses import dataclass
from directions import Direction
from palette.block import Block
from palette.material import Material, BasicMaterial

@dataclass
class Flower_Shop:
    counter_goods : list[Material] = (BasicMaterial(Block('flower_pot')), BasicMaterial(Block('potted_lily_of_the_valley')), 
        BasicMaterial(Block('potted_dandelion')), BasicMaterial(Block('potted_cornflower')), BasicMaterial(Block('potted_poppy')),
        BasicMaterial(Block('potted_allium')), BasicMaterial(Block('potted_blue_orchid')), BasicMaterial(Block('potted_azure_bluet')),
        BasicMaterial(Block('potted_red_tulip')), BasicMaterial(Block('potted_pink_tulip')), BasicMaterial(Block('potted_white_tulip')),
        BasicMaterial(Block('potted_orange_tulip')), BasicMaterial(Block('potted_oxeye_daisy')), BasicMaterial(Block('flower_pot')),
        BasicMaterial(Block('flower_pot')))

    floor_goods : list[Material] = (BasicMaterial(Block('flower_pot')), BasicMaterial(Block('potted_lily_of_the_valley')), 
        BasicMaterial(Block('potted_dandelion')), BasicMaterial(Block('potted_cornflower')), BasicMaterial(Block('potted_poppy')),
        BasicMaterial(Block('potted_allium')), BasicMaterial(Block('potted_blue_orchid')), BasicMaterial(Block('potted_azure_bluet')),
        BasicMaterial(Block('potted_red_tulip')), BasicMaterial(Block('potted_pink_tulip')), BasicMaterial(Block('potted_white_tulip')),
        BasicMaterial(Block('potted_orange_tulip')), BasicMaterial(Block('potted_oxeye_daisy')), BasicMaterial(Block('flower_pot')),
        BasicMaterial(Block('flower_pot')))

@dataclass
class Plant_Shop:
    counter_goods : list[Material] = (BasicMaterial(Block('flower_pot')), BasicMaterial(Block('potted_fern')), 
        BasicMaterial(Block('potted_birch_sapling')), BasicMaterial(Block('potted_oak_sapling')), BasicMaterial(Block('potted_jungle_sapling')),
        BasicMaterial(Block('potted_spruce_sapling')), BasicMaterial(Block('potted_acacia_sapling')), BasicMaterial(Block('potted_dark_oak_sapling')),
        BasicMaterial(Block('potted_cactus')), BasicMaterial(Block('potted_bamboo')), BasicMaterial(Block('potted_dead_bush')),
        BasicMaterial(Block('flower_pot')))

    floor_goods : list[Material] = (BasicMaterial(Block('flower_pot')), BasicMaterial(Block('potted_fern')), 
        BasicMaterial(Block('potted_birch_sapling')), BasicMaterial(Block('potted_oak_sapling')), BasicMaterial(Block('potted_jungle_sapling')),
        BasicMaterial(Block('potted_spruce_sapling')), BasicMaterial(Block('potted_acacia_sapling')), BasicMaterial(Block('potted_dark_oak_sapling')),
        BasicMaterial(Block('potted_cactus')), BasicMaterial(Block('potted_bamboo')), BasicMaterial(Block('potted_dead_bush')),
        BasicMaterial(Block('flower_pot')))

@dataclass
class Head_Shop:
    counter_goods : list[Material] = (BasicMaterial(Block('dragon_head')), BasicMaterial(Block('creeper_head')), 
        BasicMaterial(Block('zombie_head')), BasicMaterial(Block('skeleton_skull')), BasicMaterial(Block('wither_skeleton_skull')))

    floor_goods = False

@dataclass
class Wool_Shop:
    counter_goods : list[Material] = (BasicMaterial(Block('cyan_carpet')), BasicMaterial(Block('light_gray_carpet')), 
        BasicMaterial(Block('lime_carpet')), BasicMaterial(Block('light_blue_carpet')), BasicMaterial(Block('purple_carpet')),
        BasicMaterial(Block('green_carpet')), BasicMaterial(Block('blue_carpet')), BasicMaterial(Block('brown_carpet')),
        BasicMaterial(Block('red_carpet')), BasicMaterial(Block('black_carpet')), BasicMaterial(Block('orange_carpet')),
        BasicMaterial(Block('magenta_carpet')), BasicMaterial(Block('white_carpet')), BasicMaterial(Block('white_carpet')),
        BasicMaterial(Block('gray_carpet')), BasicMaterial(Block('pink_carpet')), BasicMaterial(Block('yellow_carpet')))

    floor_goods = False

@dataclass
class Glazed_Terracotta_Shop:
    counter_goods : list[Material] = (BasicMaterial(Block('cyan_glazed_terracotta')), BasicMaterial(Block('light_gray_glazed_terracotta')), 
        BasicMaterial(Block('lime_glazed_terracotta')), BasicMaterial(Block('light_blue_glazed_terracotta')), BasicMaterial(Block('purple_glazed_terracotta')),
        BasicMaterial(Block('green_glazed_terracotta')), BasicMaterial(Block('blue_glazed_terracotta')), BasicMaterial(Block('brown_glazed_terracotta')),
        BasicMaterial(Block('red_glazed_terracotta')), BasicMaterial(Block('black_glazed_terracotta')), BasicMaterial(Block('orange_glazed_terracotta')),
        BasicMaterial(Block('magenta_glazed_terracotta')), BasicMaterial(Block('white_glazed_terracotta')), BasicMaterial(Block('white_glazed_terracotta')),
        BasicMaterial(Block('gray_glazed_terracotta')), BasicMaterial(Block('pink_glazed_terracotta')), BasicMaterial(Block('yellow_glazed_terracotta')))

    floor_goods = False

@dataclass
class Glass_Shop:
    counter_goods : list[Material] = (BasicMaterial(Block('cyan_stained_glass')), BasicMaterial(Block('light_gray_stained_glass')), 
        BasicMaterial(Block('lime_stained_glass')), BasicMaterial(Block('light_blue_stained_glass')), BasicMaterial(Block('purple_stained_glass')),
        BasicMaterial(Block('green_stained_glass')), BasicMaterial(Block('blue_stained_glass')), BasicMaterial(Block('brown_stained_glass')),
        BasicMaterial(Block('red_stained_glass')), BasicMaterial(Block('black_stained_glass')), BasicMaterial(Block('orange_stained_glass')),
        BasicMaterial(Block('magenta_stained_glass')), BasicMaterial(Block('white_stained_glass')), BasicMaterial(Block('white_stained_glass')),
        BasicMaterial(Block('glass')), BasicMaterial(Block('glass')), BasicMaterial(Block('glass')),
        BasicMaterial(Block('gray_stained_glass')), BasicMaterial(Block('pink_stained_glass')), BasicMaterial(Block('yellow_stained_glass')))

    floor_goods = False

@dataclass
class Shulker_Shop:
    counter_goods : list[Material] = (BasicMaterial(Block('cyan_shulker_box')), BasicMaterial(Block('light_gray_shulker_box')), 
        BasicMaterial(Block('lime_shulker_box')), BasicMaterial(Block('light_blue_shulker_box')), BasicMaterial(Block('purple_shulker_box')),
        BasicMaterial(Block('green_shulker_box')), BasicMaterial(Block('blue_shulker_box')), BasicMaterial(Block('brown_shulker_box')),
        BasicMaterial(Block('red_shulker_box')), BasicMaterial(Block('black_shulker_box')), BasicMaterial(Block('orange_shulker_box')),
        BasicMaterial(Block('magenta_shulker_box')), BasicMaterial(Block('white_shulker_box')), BasicMaterial(Block('white_shulker_box')),
        BasicMaterial(Block('shulker_box')), BasicMaterial(Block('shulker_box')), BasicMaterial(Block('shulker_box')),
        BasicMaterial(Block('gray_shulker_box')), BasicMaterial(Block('pink_shulker_box')), BasicMaterial(Block('yellow_shulker_box')))

    floor_goods = False

@dataclass
class Food_Shop:
    counter_goods : list[Material] = (BasicMaterial(Block('cake')), BasicMaterial(Block('melon')), 
        BasicMaterial(Block('pumpkin')), BasicMaterial(Block(f'sea_pickle[waterlogged=false]')),
        BasicMaterial(Block('player_head')))

    floor_goods = False


    #/setblock ~ ~1 ~ minecraft:player_head[rotation=0]{SkullOwner:{Id:[I;440871046,979259357,-1150162889,656058295],Properties:{textures:[{Value:"eyJ0ZXh0dXJlcyI6eyJTS0lOIjp7InVybCI6Imh0dHA6Ly90ZXh0dXJlcy5taW5lY3JhZnQubmV0L3RleHR1cmUvM2U4MGM3M2I3NjVkOWYyZTJhMWFlNmQ5ZGY5NmM1ZmJjNjEyNmVlNTRmOWRmMGE0NmJiMWYwMGVmMGIwMjc5ZSJ9fX0="}]}}} replace

@dataclass
class Armour_Shop:
    counter_goods : list[Material] = (BasicMaterial(Block('armor_stand')),
        BasicMaterial(Block('armor_stand[NoBasePlate:1b]')))

    floor_goods = False

    #/summon minecraft:armor_stand ~ ~1 ~ {ShowArms:1b,NoBasePlate:1b,ArmorItems:[{id:"minecraft:leather_boots",Count:1b},{id:"minecraft:leather_leggings",Count:1b},{id:"minecraft:leather_chestplate",Count:1b},{id:"minecraft:player_head",Count:1b,tag:{SkullOwner:{Id:[I;440871046,979259357,-1150162889,656058295],Properties:{textures:[{Value:"eyJ0ZXh0dXJlcyI6eyJTS0lOIjp7InVybCI6Imh0dHA6Ly90ZXh0dXJlcy5taW5lY3JhZnQubmV0L3RleHR1cmUvM2U4MGM3M2I3NjVkOWYyZTJhMWFlNmQ5ZGY5NmM1ZmJjNjEyNmVlNTRmOWRmMGE0NmJiMWYwMGVmMGIwMjc5ZSJ9fX0="}]}}}}]}