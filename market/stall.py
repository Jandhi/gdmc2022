from numpy import size
from directions import Direction
from palette.block import Block
from palette.palette import Palette
from random import seed
from random import randint
from market.goods import *

class Stall:
    palette: Palette

    #p1 and p2 are the starting and end points of the rectangle that forms the road
    def __init__(self, origin, counter: str = 'basic', side: str = 'basic', roof: str = 'basic', overhang: str = 'none', direction: Direction = 'z_minus', length: int=5, depth: int = 4, height: int = 4) -> None:
        self.origin = origin
        self.overhang = overhang
        self.counter = counter
        self.roof = roof
        self.side = side
        self.direction = direction
        self.length = length
        self.depth = depth
        self.height = height
        self.back_counter = False #should there be a duplicate counter at the rear of the stall
        self.counter_space = [] #list of points where there is space to put items on a counter
        self.floor_space = [] #list of points where there is space to put items on a floor

        self.palette = Palette()

        if side == 'none' or side == 'trapdoor' or side == 'fence_gate':
            seed()
            chance_of_back_counter = randint(1,5)
            if chance_of_back_counter < 5:
                self.back_counter = True

        self.goods = 'none'
        self.set_random_goods()

    def get_origin(self):
        return self.origin

    def set_origin(self, origin):
        self.origin = origin

    def set_direction(self, direction):
        self.direction = direction

    def add_counter_space(self, point):
        self.counter_space.append(point)

    def add_floor_space(self, point):
        self.floor_space.append(point)

    def get_floor_good(self):
        seed()
        list_of_goods = self.goods.floor_goods
        a = randint(0, len(list_of_goods)-1)
        return list_of_goods[a]

    def get_counter_good(self):
        seed()
        list_of_goods = self.goods.counter_goods
        a = randint(0, len(list_of_goods)-1)
        return list_of_goods[a]

    def has_floor_goods(self):
        if self.goods.floor_goods == False:
            return False
        return True

    def set_random_goods(self):
        seed()
        a = randint(1,8) #start at 0 if you want a chance of empty stalls
        if a == 1:
            self.goods = Flower_Shop()
        elif a == 2:
            self.goods = Plant_Shop()
        elif a == 3:
            self.goods = Head_Shop()
        elif a == 4:
            self.goods = Wool_Shop()
        elif a == 5:
            self.goods = Glazed_Terracotta_Shop()
        elif a == 6:
            self.goods = Glass_Shop()
        elif a == 7:
            self.goods = Shulker_Shop()
        elif a == 8:
            self.goods = Food_Shop()
        elif a == 9:
            self.goods = Armour_Shop()
        elif a == 10:
            self.goods = Wool_Shop()