from gdpc.interface import requestPlayerArea, Interface, setBuildArea
from districts.blocks.district_generator import DistrictGenerator
from noise.random import set_seed
from noise.noise import recursive_hash
from noise.random_number_generator import RandomNumberGenerator

from shapely.geometry import Point
from shapely.geometry.polygon import Polygon

area = list(requestPlayerArea(200, 200))
area[1] = 3
area[4] = 200
setBuildArea(*area)
set_seed(recursive_hash(*area))

interface = Interface(area[0] + 1, 0, area[2] + 1, True)

DistrictGenerator(area=area).generate(interface)

interface.sendBlocks()