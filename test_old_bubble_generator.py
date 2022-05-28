from gdpc.interface import requestPlayerArea, Interface, setBuildArea
from gdpc.worldLoader import WorldSlice
from districts.blocks.bubble_generator_old import BubbleGenerator
from noise.random import set_seed
from noise.noise import recursive_hash
from noise.random_number_generator import RandomNumberGenerator

from shapely.geometry import Point
from shapely.geometry.polygon import Polygon


area = list(requestPlayerArea(50, 50))
area[1] = 3
area[4] = 200
setBuildArea(*area)
set_seed(recursive_hash(*area))
slice = WorldSlice(area[0], area[2], area[3], area[5])

interface = Interface(area[0], 0, area[2], True)

BubbleGenerator(point_amount=8,area=area, slice=slice).generate(interface)

interface.sendBlocks()