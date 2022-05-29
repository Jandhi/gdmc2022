from telnetlib import theNULL
from nbt import nbt
import json
from gdpc.interface import requestPlayerArea, Interface, setBuildArea

size_x = 20
size_z = 20

area = list(requestPlayerArea(size_x, size_z))
area[1] = 3
area[4] = 200
setBuildArea(*area)

block_lookup = {
    "minecraft:stone_bricks": "stone",
    "minecraft:mossy_stone_bricks": "stone_accent",
    "minecraft:oak_planks": "wood",
    "minecraft:jungle_planks": "wood_accent",
    "minecraft:birch_planks": "floor",
    "minecraft:cobblestone": "foundation",
    "minecraft:oak_log": "frame",
    "minecraft:white_concrete": "wall",
    "minecraft:white_terracotta": "wall_accent",
    "minecraft:bricks": "ceiling",
    "minecraft:brick_stairs": "ceiling_stair",
    "minecraft:spruce_planks": "ceiling_accent",
    "minecraft:spruce_stairs": "ceiling_stair_accent",
    "minecraft:glass_pane": "window",
    "minecraft:oak_trapdoor": "shutter",
    "minecraft:spruce_slab": "window_sill",
    "minecraft:oak_fence": "supports",
    "minecraft:wall_torch": "torch",
    "minecraft:glowstone": "light",
    "minecraft:oak_door": "door"
}

biome = ""
with open("./nbt biom convert/biom/desert.json", "r") as read_file:
    biome = json.load(read_file)

nbtfile = nbt.NBTFile("./schematics/structures/housetest.nbt")

def get_properties(i):
    pal = nbtfile['palette'].tags[i]
    attr = ""
    if 'Properties' in pal:
        props = pal['Properties']
        for prop in props.tags:
            attr += f',{prop.name}={prop.value}'
    return attr[1:]

def should_preserve_props(old_block, new_block):
    preserve_types = ["log", "stair", "trapdoor", "torch", "fence", "door"]
    for type in preserve_types:
        if type in old_block and type in new_block:
            return True
    return False 

def palette_lookup(i):
    pal = nbtfile['palette'].tags[i]
    return pal['Name'].value

interface = Interface(area[0], 3, area[2], True)

for block_tag in nbtfile['blocks'].tags:
    block_name = palette_lookup(block_tag['state'].value)
    props = get_properties(block_tag['state'].value)
    if block_name in block_lookup.keys():
        block_type = block_lookup.get(block_name)
        x, y, z = block_tag['pos'][0].value, block_tag['pos'][1].value, block_tag['pos'][2].value
        converted_block = biome[block_type]
        if len(props) > 0:
            if should_preserve_props(block_name, converted_block):
                interface.placeBlock(x, y, z, f'{converted_block}[{props}]')
            else:
                interface.placeBlock(x, y, z, converted_block)   
        else:
            interface.placeBlock(x, y, z, converted_block)
            
        


