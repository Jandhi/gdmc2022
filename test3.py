from gdpc.interface import requestPlayerArea, Interface, setBuildArea
from districts.blocks.block_generator import BlockGenerator

area = list(requestPlayerArea(17, 17))
area[1] = 3
area[4] = 200
setBuildArea(*area)

interface = Interface(area[0], 0, area[2], True)

width = area[3] - area[0] + 1
depth = area[5] - area[2] + 1

for x in range(width):
    for z in range(depth):
        interface.placeBlock(x, 3, z, 'green_wool')
        interface.placeBlock(x, 4, z, 'air')

BlockGenerator(passable_map=[[True for z in range(depth)] for x in range(width)]).generate(interface)