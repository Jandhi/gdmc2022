from house.decoration.flag_generator import FlagGenerator
from house.grid import Grid
from house.frame_generator import FrameGenerator
from house.floor_generator import FloorGenerator
from clear import Clear
from checkerboard import CheckerBoardGenerator
from house.house import House
from house.roof.roof_generator import RoofGenerator
from house.roof.tower_roof import TowerRoofGenerator
from house.walls.wall_generator import WallGenerator
from city.road import Road
from city.city import City
from city.road_generator import RoadGenerator
from gdpc.interface import requestPlayerArea, Interface, setBuildArea

size_x = 200
size_z = 200

area = list(requestPlayerArea(size_x, size_z))
area[1] = 3
area[4] = 200
setBuildArea(*area)

interface = Interface(area[0], 0, area[2], True)

city = City((1,1), 3, (200,200))
city.add_random_roads_across(5, 15, 6)
city.add_random_roads_across(15, 10, 4)
city.add_random_roads_across(50, 5, 2)

CheckerBoardGenerator(tile_width=5, tile_depth=5, area=(1, 1, size_x, size_z), y=3).generate(interface)

for road in city.roads:
    RoadGenerator(road=road).generate(interface)