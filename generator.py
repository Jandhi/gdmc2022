from progress.bar import Bar
from gdpc.interface import Interface
from palette.palette import Palette

class Generator():
    name = 'Generator'
    bar = None
    x1, y1, z1, x2, y2, z2 = 0, 0, 0, 0, 0, 0
    area = 0, 0, 0, 0
    width, height, depth = 0, 0, 0
    palette : Palette
    
    def __init__(self, **kwargs) -> None:
        self.__dict__.update(kwargs)
        
        if len(self.area) == 4:
            self.x1, self.z1, self.x2, self.z2 = self.area
        else:
            self.x1, self.y1, self.z1, self.x2, self.y2, self.z2 = self.area
        
        self.width = self.x2 - self.x1
        self.height = self.y2 - self.y1
        self.depth = self.z2 - self.z1

    def __get_work_amount__(self) -> int:
        pass
    
    def generate(self, interface : Interface):
        work = self.__get_work_amount__()

        if work:
            self.bar = Bar(f'Running {self.name}', max=work)
        else:
            print(f'Running {self.name}')

        self.__generate__(interface)

        if self.bar:
            self.bar.finish()

        interface.sendBlocks()
        
    def __generate__(self2, interface: Interface):
        pass