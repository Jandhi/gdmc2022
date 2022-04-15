from gdpc.interface import requestPlayerArea, Interface, setBuildArea
from districts.blocks.block_generator import BlockGenerator
from noise.random import set_seed
from noise.noise import recursive_hash
from noise.random_number_generator import RandomNumberGenerator

from shapely.geometry import Point
from shapely.geometry.polygon import Polygon

area = list(requestPlayerArea(66, 66))
area[1] = 3
area[4] = 200
setBuildArea(*area)
set_seed(recursive_hash(*area))

interface = Interface(area[0] + 1, 0, area[2] + 1, True)

width = area[3] - area[0] - 2
depth = area[5] - area[2] - 2

rng = RandomNumberGenerator(recursive_hash(*area))

for x in range(width):
    for z in range(depth):
        block = 'green_wool' if ((x // 2) + (z // 2)) % 2 == 0 else 'lime_terracotta'
        interface.placeBlock(x, 3, z, block)
        interface.placeBlock(x, 4, z, 'air')

p1 = (rng.rand_int(0, width // 2), rng.rand_int(0, depth // 2))
p2 = (rng.rand_int(0, width // 2), rng.rand_int(depth // 2, depth))
p3 = (rng.rand_int(width // 2, width), rng.rand_int(depth // 2, depth))
p4 = (rng.rand_int(width // 2, width), rng.rand_int(0, depth // 2))
polygon = Polygon([p1, p2, p3, p4])

pmap = [[polygon.contains(Point(x, z)) for z in range(depth)] for x in range(width)]

BlockGenerator(passable_map=pmap).generate(interface)