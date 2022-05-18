from generator import Generator
from house.frame_generator import FrameGenerator
from house.house import House
from house.walls.wall_generator import WallGenerator
from house.grid import Grid
from gdpc.interface import Interface
from house.roof.roof_generator import RoofGenerator
from house.windows.window_generator import WindowGenerator
from house.floor_generator import FloorGenerator

class HouseGenerator(Generator):
    name = 'House Generator'

    def __generate__(self, interface : Interface):
        if not self.house:
            return

        generators = [WallGenerator, WindowGenerator, FloorGenerator, RoofGenerator]

        if self.house.has_frame:
            generators.append(FrameGenerator)

        for generator in generators:
            generator(house=self.house).generate(interface)