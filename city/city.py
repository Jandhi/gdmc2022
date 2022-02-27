from tkinter import Y
from house.grid import Grid
from palette.block import Block
from palette.material import BasicMaterial
from palette.palette import Palette
from city.road import Road
from random import seed
from random import randint

class City:

    def __init__(self, p1, y, p2) -> None:
        self.roads = []
        self.road_points = []
        self.p1 = p1
        self.y = y
        self.p2 = p2
        self.unusable_x = {}
        self.unusable_z = {}

    def add_road(self, p1, y, p2) -> Road:
        self.roads.append(Road(p1, y, p2))

    def add_random_roads_across(self, num, distance_between_roads, road_size):
        seed()
        x_min = self.p1[0]
        x_max = self.p2[0]
        z_min = self.p1[1]
        z_max = self.p2[1]

        for i in range(0, num):
            b = randint(0,1)
            if b==0:
                a = randint(x_min,x_max-5)
                if not a in self.unusable_x:
                    p1=(a,z_min)
                    p2=(a+road_size,z_max)
                    for c in range(a-distance_between_roads,a+distance_between_roads):
                        self.unusable_x[c] = 'used'
                    new_road = Road(p1, self.y, p2)
                    self.roads.append(new_road)
                    self.road_points.append(new_road)
            else:
                a = randint(z_min,z_max-5)
                if not a in self.unusable_z:
                    p1=(x_min,a)
                    p2=(x_max,a+road_size)
                    for c in range(a-distance_between_roads,a+distance_between_roads):
                        self.unusable_z[c] = 'used'
                    new_road = Road(p1, self.y, p2)
                    self.roads.append(new_road)
                    self.road_points.append(new_road)
            
    
    def add_random_roads_between(self, num, distance_between_roads, road_size):
        seed()
        x_min = self.p1[0]
        x_max = self.p2[0]
        z_min = self.p1[1]
        z_max = self.p2[1]

        for i in range(0, num):
            b = randint(0,1)
            if b==0:
                a = randint(x_min,x_max-5)
                if not a in self.unusable_x:
                    p1=(a,z_min)
                    p2=(a+road_size,z_max)
                    for c in range(a-distance_between_roads,a+distance_between_roads):
                        self.unusable_x[c] = 'used'
                    new_road = Road(p1, self.y, p2)
                    self.roads.append(new_road)
                    self.road_points.append(new_road)
            else:
                a = randint(z_min,z_max-5)
                if not a in self.unusable_z:
                    p1=(x_min,a)
                    p2=(x_max,a+road_size)
                    for c in range(a-distance_between_roads,a+distance_between_roads):
                        self.unusable_z[c] = 'used'
                    new_road = Road(p1, self.y, p2)
                    self.roads.append(new_road)
                    self.road_points.append(new_road)