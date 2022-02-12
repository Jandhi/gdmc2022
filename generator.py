from tools import USE_BATCHING
from http_client import interfaceUtils
from progress.bar import Bar

class Generator():
    name = 'Generator'
    bar = None
    x1, y1, z1, x2, y2, z2 = 0, 0, 0, 0, 0, 0
    area = 0, 0, 0, 0
    width, height, depth = 0, 0, 0
    
    def __init__(self, **kwargs) -> None:
        for key, value in kwargs.items():
            setattr(self, key, value)
        
        if len(self.area) == 4:
            self.x1, self.z1, self.x2, self.z2 = self.area
        else:
            self.x1, self.y1, self.z1, self.x2, self.y2, self.z2 = self.area
        
        self.width = self.x2 - self.x1
        self.height = self.y2 - self.y1
        self.depth = self.z2 - self.z1

    def __get_work_amount__(self) -> int:
        pass
    
    def generate(self):
        work = self.__get_work_amount__()

        if work:
            self.bar = Bar(f'Running {self.name}', max=work)
        else:
            print(f'Running {self.name}')

        self.__generate__()

        if self.bar:
            self.bar.finish()

        if USE_BATCHING:
        # we need to send any blocks remaining in the buffer
            interfaceUtils.sendBlocks()
    
    def __generate__(self2):
        pass