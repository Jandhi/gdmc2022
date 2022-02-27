from generator import Generator
from house.walls.wall_generator import WallGenerator
from house.grid import Grid
from gdpc.interface import Interface
from house.frame_generator import FrameGenerator

class HouseGenerator(Generator):
    name = 'HouseGenerator'
    grid : Grid = None

    def __generate__(self, interface : Interface):
        if not self.house:
            return
        
        WallGenerator(house=self.house).generate(interface)