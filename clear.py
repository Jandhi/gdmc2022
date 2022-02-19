from tools import area, setBlock
from generator import Generator

class Clear(Generator):
    name='clear'
    height_limit=100
    y=4

    def __get_work_amount__(self) -> int:
        return self.width * self.depth

    def __generate__(self):
        for x in range(self.x1, self.x2):
            for z in range(self.z1, self.z2):
                self.bar.next()
                for y in range(self.y, self.height_limit):
                    setBlock(x, y, z, 'air')

if __name__ == '__main__':
    Clear(height_limit=50, area=area, y=4).generate()