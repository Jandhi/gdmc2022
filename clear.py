from generator import Generator
from gdpc.interface import Interface, runCommand

from vector import sum_vectors

class Clear(Generator):
    name='clear'

    def __get_work_amount__(self) -> int:
        return self.width * self.depth

    def __generate__(self, interface : Interface):
        '''
        Maybe someone can get this to work someday
        x1, y1, z1 = sum_vectors(interface.offset, (self.x1, self.y1, self.z1))
        x2, y2, z2 = sum_vectors(interface.offset, (self.x2, self.y2, self.z2))
        runCommand(f'/fill {x1} {y1} {z1} {x2} {y2} {z2} air')
        '''
        
        for x in range(self.x1, self.x2):
            for z in range(self.z1, self.z2):
                self.bar.next()
                for y in range(self.y, self.height_limit):
                    interface.placeBlock(x, y, z, 'air')