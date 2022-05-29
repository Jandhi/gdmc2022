
from nbt import nbt
import json
import random
from gdpc.interface import requestPlayerArea, Interface, setBuildArea


# Load the nbt
# Split it into regions
# generate a layout
# assign regions to the layout
# send the blocks to minecraft

def get_properties(nbt, i):
    pal = nbt['palette'].tags[i]
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

def palette_lookup(nbt, i):
    pal = nbt['palette'].tags[i]
    return pal['Name'].value

def load_nbt(name):
    return nbt.NBTFile(f'./modulizer/resources/{name}.nbt')

def split_nbt(nbt):
    regions = [
        [[[],[],[]],[[],[],[]],[[],[],[]]],
        [[[],[],[]],[[],[],[]],[[],[],[]]],
        [[[],[],[]],[[],[],[]],[[],[],[]]]
    ]
    
    for block_tag in nbt['blocks'].tags:
        x, y, z = block_tag['pos'][0].value, block_tag['pos'][1].value, block_tag['pos'][2].value
        block_name = palette_lookup(nbt, block_tag['state'].value)

        block_props = get_properties(nbt, block_tag['state'].value)
        ix = x // 7
        iy = y // 4
        iz = z // 7
        if iy > 2: 
            iy = 2
        regions[ix][iy][iz].append({
            "pos": (x % 7, y % 4 if iy < 2 else y - 8, z % 7),
            "name": block_name,
            "props": block_props
        })
    return regions

def draw_region(region, x, y, z):
    size_x = 7
    size_z = 7

    area = list(requestPlayerArea(size_x, size_z))
    area[3] += 3 * 7
    area[4] += 8 * 4
    area[5] += 3 * 7

    setBuildArea(*area)
    interface = Interface(area[0], 3, area[2], True)
    for block in region:
        name = block['name']
        props = block['props']
        pos = block['pos']
        if 'air' in name and not 'stair' in name:
            continue
        if len(props) > 0:
            name = f'{name}[{props}]'
        interface.placeBlock(pos[0] + (x * 7), pos[1] + (y * 4), pos[2] + (z * 7), name)

def create_layout(width, depth):
    layout = []
    for x in range(0, width):
        layout.append([])
        for _ in range(0, depth):
            layout[x].append(random.randint(2, 5))
    return layout

def draw_level(level, layout, regions):
    placed = False
    for i in range(0, len(layout)):
        for j in range(0, len(layout[i])):
            height = layout[i][j]
            if level == 0:
                draw_region(regions[i][0][j], i, level, j)
                print("placing ground")
                placed = True
            elif level < height:
                draw_region(regions[i][1][j], i, level, j)
                print("placing middle")
                placed = True
            elif level == height:
                draw_region(regions[i][2][j], i, level, j)
                print("placing roof")
                placed = True
    return placed


def draw_layout(layout, regions):
    level = 0
    placed = True
    while placed:
        placed = draw_level(level, layout, regions)
        level += 1

def find_block(region, x, y, z):
    for block in region:
        bx, by, bz = block['pos'][0], block['pos'][1], block['pos'][2]
        if bx == x and by == y and bz == z:
            return block

def merge_region(region_a, region_b):
    new_region = []
    for block_a in region_a:
        bx, by, bz = block_a['pos'][0], block_a['pos'][1], block_a['pos'][2]
        block_b = find_block(region_b, bx, by, bz)
            
        if 'log' in block_b['name']:
            new_region.append(block_b)
            continue
        elif 'cobblestone' in block_b['name']:
            new_region.append(block_b)
            continue
        elif 'birch' in block_b['name']:
            if bx == 0 or bx == 6 or bz == 0 or bz == 6:
                if 'log' in block_a['name']:
                    new_region.append(block_a)
                continue
        elif 'spruce' in block_b['name']:
            new_region.append(block_b)
            continue
        elif 'air' in block_a['name'] and not 'stair' in block_a['name']:
            new_region.append(block_b)
            continue
        new_region.append(block_a)
    return new_region

nbt = load_nbt("house_1")
regions = split_nbt(nbt)
layout = create_layout(3,3)

#draw_layout(layout, regions)

new_floor_region = merge_region(regions[1][0][0], regions[0][0][1])
new_floor_region = merge_region(new_floor_region, regions[1][0][2])
new_floor_region = merge_region(new_floor_region, regions[2][0][1])

new_mid_region = merge_region(regions[1][1][0], regions[0][1][1])
new_mid_region = merge_region(new_mid_region, regions[1][1][2])
new_mid_region = merge_region(new_mid_region, regions[2][1][1])

new_roof_region = merge_region(regions[1][2][0], regions[0][2][1])
new_roof_region = merge_region(new_roof_region, regions[1][2][2])
new_roof_region = merge_region(new_roof_region, regions[2][2][1])

draw_region(new_floor_region, 0, 0, 0)
draw_region(new_mid_region, 0, 1, 0)
draw_region(new_roof_region, 0, 2, 0)

