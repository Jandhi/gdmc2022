from generator import Generator
from gdpc.interface import Interface

class Clear(Generator):
    name='clear'
    height_limit=100
    y=4

    def __get_work_amount__(self) -> int:
        return self.width * self.depth

    def __generate__(self, interface : Interface):
        for x in range(self.x1, self.x2):
            for z in range(self.z1, self.z2):
                self.bar.next()
                for y in range(self.y, self.height_limit):
                    interface.placeBlock(x, y, z, 'air')