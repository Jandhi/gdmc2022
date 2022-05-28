from tkinter import Y
from house.grid import Grid
from palette.block import Block
from palette.material import BasicMaterial
from palette.palette import Palette
from misc.tree import Tree
from market.stall import Stall
from random import seed
from random import randint

class City:

    def __init__(self, p1, hmap, wmap, p2) -> None:
        self.p1 = p1
        self.p2 = p2
        self.trees = []
        self.stalls = []
        self.hmap = hmap
        self.wmap = wmap

    def add_tree(self, point, type):
        self.trees.append(Tree(point, type))

    def add_random_trees(self, num, dist):
        x_min = self.p1[0]+2
        x_max = self.p2[0]-2
        z_min = self.p1[1]+2
        z_max = self.p2[1]-2

        for i in range(0, num):

            a = randint(x_min,x_max)
            b = randint(z_min,z_max)
            point = (a, self.hmap[a][b], b)
            if self.wmap[a][b] == False:
                c = randint(4,10)
                if c==10:
                    type = "mega_oak"
                elif 10>c>8:
                    type = "large_oak"
                elif 4<=c<=8:
                    type = "medium_oak"
                else:
                    type = "small_oak"
                #type = "mega_jungle"
                new_tree = Tree(point, type)
                self.trees.append(new_tree)

    def add_stall(self, point):
        self.stalls.append(Stall(point))
        
    def add_giga_stall(self, point):
        self.stalls.append(Stall(point, '','','','','',20,10,8))

    def add_stalls(self):
        self.stalls.append(Stall((120, 4, 100), 'basic','none','basic','none', 'z_minus'))
        self.stalls.append(Stall((110, 4, 100), 'stair','basic','back_down','campfire', 'z_minus'))
        self.stalls.append(Stall((100, 4, 100), 'half_stair','trapdoor','sides_down','trapdoor', 'z_minus'))
        self.stalls.append(Stall((90, 4, 100), 'slab','fence','sides_down','banner', 'z_minus'))
        self.stalls.append(Stall((80, 4, 100), 'half_slab','fence_gate','front_down','none'))
        self.stalls.append(Stall((70, 4, 100), 'stair_slab','stair','front_back_down','none'))
        self.stalls.append(Stall((60, 4, 100), 'stair_slab','slab','front_back_down','none'))

    def add_stalls2(self):
        self.stalls.append(Stall((120, 4, 100), 'half_stair','trapdoor','sides_down','trapdoor', 'x_minus'))
        self.stalls.append(Stall((110, 4, 100), 'half_stair','trapdoor','sides_down','trapdoor', 'z_minus'))
        self.stalls.append(Stall((100, 4, 100), 'half_stair','trapdoor','sides_down','trapdoor', 'z_plus'))
        self.stalls.append(Stall((90, 4, 100), 'half_stair','trapdoor','sides_down','trapdoor', 'x_plus'))