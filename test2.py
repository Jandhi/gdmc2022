from clear import Clear
from house.grid import Grid
from gdpc.interface import requestPlayerArea, Interface, setBuildArea
from house.house import House
from house.house_generator import HouseGenerator
from checkerboard import CheckerBoardGenerator
from noise.random import hash_vector, set_seed

area = list(requestPlayerArea(66, 66))
area[1] = 3
area[4] = 200
setBuildArea(*area)

interface = Interface(area[0], 0, area[2], True)
set_seed(hash_vector(interface.offset))

grid = Grid((1, 3, 1), (5, 5, 5))
for x in range(3):
    for z in range(2):
        for y in range(2):
            grid.add_node(x + 5, y, z + 5)

house = House(grid)

print(area)

Clear(area=(1, 1, 66, 66), y=4, height_limit=30).generate(interface)
CheckerBoardGenerator(grid=grid, area=(1, 1, 66, 66), tile_width=grid.width, tile_depth=grid.depth, y=3).generate(interface)
HouseGenerator(house=house).generate(interface)

for x in range(50):
    for z in range(50):
        for node in house.grid.nodes.values():
            node.palette.wall.place_block(interface, x, 20, z)
        