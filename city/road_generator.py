from generator import Generator
from city.road import Road
from gdpc.interface import Interface
from palette.block import Block
from palette.palette import Palette
from palette.material import Material

class RoadGenerator(Generator):
    name = 'Road Generator'
    road : Road

    def __generate__(self, interface : Interface):
        if not self.road:
            return
        
        points = self.road.get_road_points()
        for point in points:
            self.road.palette.floor.place_block(interface, point[0], point[1], point[2])

            # p1, y, p2 = self.road.get_road()
            # x1 = p1[0]
            # z1 = p1[1]
            # x2 = p2[0]
            # z2 = p2[1]

            # for x in range(x1, x2):
            #     for z in range(z1, z2):
            #         self.road.palette.floor.place_block(interface, x, y, z)
        