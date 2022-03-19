from tkinter import Y
from house.grid import Grid
from palette.block import Block
from palette.material import BasicMaterial
from palette.palette import Palette
from misc.tree import Tree
from random import seed
from random import randint

class City:

    def __init__(self, p1, y, p2) -> None:
        self.p1 = p1
        self.y = y
        self.p2 = p2
        self.trees = []

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
            point = (a, self.y+1, b)
            c = randint(0,9)
            if c>5:
                 type = "medium_birch"
            elif 3<=c<=5:
                 type = "small_birch"
            else:
                type = "large_birch"
            type = "small_pine"
            new_tree = Tree(point, type)
            self.trees.append(new_tree)
