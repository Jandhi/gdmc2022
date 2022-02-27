from house.grid import Grid
from gdpc.interface import requestPlayerArea, Interface, setBuildArea
from house.house import House
from house.house_generator import HouseGenerator
from checkerboard import CheckerBoardGenerator

area = list(requestPlayerArea(66, 66))
area[1] = 3
area[4] = 200
setBuildArea(*area)

interface = Interface(area[0], 0, area[2], True)

grid = Grid((1, 3, 1), (5, 7, 5))
for x in range(3):
    for z in range(2):
        for y in range(2):
            grid.add_node(x + 5, y, z + 5)

house = House(grid)

print(area)

CheckerBoardGenerator(grid=grid, area=(1, 1, 66, 66), tile_width=grid.width, tile_depth=grid.depth, y=3).generate(interface)
HouseGenerator(house=house).generate(interface)