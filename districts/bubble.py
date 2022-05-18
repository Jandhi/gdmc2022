class Bubble:
    def __init__(self, point, size = 1) -> None:
        self.point = point
        self.size = size
        self.average_point = 0.0, 0.0
    
    def add_point(self, point):
        px, pz = point
        ax, az = self.average_point
        x = ((ax * self.size) + px) / (self.size + 1)
        z = ((az * self.size) + pz) / (self.size + 1)

        self.average_point = (x, z)
        self.size += 1 