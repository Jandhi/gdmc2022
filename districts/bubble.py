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

    def merge_with(self, bubble):
        ax1, az1 = self.average_point
        ax2, az2 = bubble.average_point

        x = (self.size * ax1 + bubble.size * ax2) / (self.size + bubble.size)
        z = (self.size * az1 + bubble.size * az2) / (self.size + bubble.size)

        self.average_point = (x, z)
        self.size += bubble.size
