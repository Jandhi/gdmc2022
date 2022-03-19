from generator import Generator
from house.house import House
from house.walls.wall_generator import WallGenerator
from house.grid import Grid
from gdpc.interface import Interface
from house.roof.roof_generator import RoofGenerator
from house.windows.window_generator import WindowGenerator
from house.floor_generator import FloorGenerator

class HouseGenerator(Generator):
    name = 'House Generator'
    house : House = None

    def __generate__(self, interface : Interface):
        if not self.house:
            return

        for generator in (WallGenerator, WindowGenerator, FloorGenerator, RoofGenerator):
            generator(house=self.house).generate(interface)