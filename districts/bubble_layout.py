
from districts.bubble import Bubble

class BubbleLayout:
    def __init__(self, districts : list[Bubble]) -> None:
        self.districts = districts

        self.are_neighbours_list = [
            [False for district in districts] for other in districts
        ]

        self.connection_length = [
            [-1 for district in districts] for other in districts
        ]

        self.neighbour_count = [
            [0 for district in districts] for other in districts
        ]

    def set_neighbours(self, district1, district2):
        index1 = self.districts.index(district1)
        index2 = self.districts.index(district2)

        self.are_neighbours_list[index1][index2] = True
        self.are_neighbours_list[index2][index1] = True

        self.neighbour_count[index1][index2] += 1
        self.neighbour_count[index2][index1] += 1

    def are_neighbours(self, district1, district2) -> bool:
        index1 = self.districts.index(district1)
        index2 = self.districts.index(district2)
        
        return self.are_neighbours_list[index1][index2]