from generator import Generator
from misc.tree import Tree
from city.city import City
from gdpc.interface import Interface
from palette.block import Block
from palette.palette import Palette
from palette.material import Material
from random import seed
from random import randint

class TreeGenerator(Generator):
    name = 'Tree Generator'
    city : City = None

    def __get_work_amount__(self) -> int:
        if self.city:
            return len(self.city.trees)

    def __generate__(self, interface : Interface):
        if not self.city:
            return

        for tree in self.city.trees:
            #print(tree.get_origin())
            self.generate_tree(tree, interface)
            self.bar.next()

    def generate_tree(self, tree, interface):
        if tree.type == 'medium_pine':
            self.generate_medium_pine(tree, interface)
        elif tree.type == 'small_pine':
            self.generate_small_pine(tree, interface, 95)
        elif tree.type == 'large_pine':
            self.generate_large_pine(tree, interface)
        elif tree.type == 'small_birch':
            self.generate_small_birch(tree, interface)
        elif tree.type == 'medium_birch':
            self.generate_medium_birch(tree, interface)
        elif tree.type == 'large_birch':
            self.generate_large_birch(tree, interface)

    def generate_small_pine(self, tree, interface, chance=100):
        x0, y0, z0 = tree.get_origin()
        seed()
        height = randint(5,7)+y0

        for y in range (y0,height+2):
            if y == height+1:
                tree.palette.leaves.place_block(interface, x0, y, z0, chance)
                continue
            tree.palette.wood.place_block(interface, x0, y, z0)
            if y%2 == height%2 and y > y0+1:
                tree.palette.leaves.place_block(interface, x0+1, y, z0, chance)
                tree.palette.leaves.place_block(interface, x0-1, y, z0, chance)
                tree.palette.leaves.place_block(interface, x0, y, z0+1, chance)
                tree.palette.leaves.place_block(interface, x0, y, z0-1, chance)
            elif y == height-1:
                tree.palette.leaves.place_block(interface, x0+1, y, z0+1, chance)
                tree.palette.leaves.place_block(interface, x0-1, y, z0-1, chance)
                tree.palette.leaves.place_block(interface, x0-1, y, z0+1, chance)
                tree.palette.leaves.place_block(interface, x0+1, y, z0-1, chance)
                tree.palette.leaves.place_block(interface, x0+1, y, z0, chance)
                tree.palette.leaves.place_block(interface, x0-1, y, z0, chance)
                tree.palette.leaves.place_block(interface, x0, y, z0+1, chance)
                tree.palette.leaves.place_block(interface, x0, y, z0-1, chance)
            elif y%2 == (height-1)%2 and y>y0:
                tree.palette.leaves.place_block(interface, x0+2, y, z0, chance)
                tree.palette.leaves.place_block(interface, x0-2, y, z0, chance)
                tree.palette.leaves.place_block(interface, x0, y, z0+2, chance)
                tree.palette.leaves.place_block(interface, x0, y, z0-2, chance)
                tree.palette.leaves.place_block(interface, x0+1, y, z0+1, chance)
                tree.palette.leaves.place_block(interface, x0-1, y, z0-1, chance)
                tree.palette.leaves.place_block(interface, x0-1, y, z0+1, chance)
                tree.palette.leaves.place_block(interface, x0+1, y, z0-1, chance)
                tree.palette.leaves.place_block(interface, x0+1, y, z0, chance)
                tree.palette.leaves.place_block(interface, x0-1, y, z0, chance)
                tree.palette.leaves.place_block(interface, x0, y, z0+1, chance)
                tree.palette.leaves.place_block(interface, x0, y, z0-1, chance)
                

    def generate_medium_pine(self, tree, interface):
        x0, y0, z0 = tree.get_origin()
        seed()
        height = randint(8,13)+y0

        for y in range (y0,height+2):
            if y == height+1:
                tree.palette.leaves.place_block(interface, x0, y, z0)
                continue
            tree.palette.wood.place_block(interface, x0, y, z0)
            if y == height:
                tree.palette.leaves.place_block(interface, x0+1, y, z0)
                tree.palette.leaves.place_block(interface, x0-1, y, z0)
                tree.palette.leaves.place_block(interface, x0, y, z0+1)
                tree.palette.leaves.place_block(interface, x0, y, z0-1)
            elif y == height-1:
                tree.palette.leaves.place_block(interface, x0+2, y, z0)
                tree.palette.leaves.place_block(interface, x0-2, y, z0)
                tree.palette.leaves.place_block(interface, x0, y, z0+2)
                tree.palette.leaves.place_block(interface, x0, y, z0-2)
                tree.palette.leaves.place_block(interface, x0+1, y, z0+1)
                tree.palette.leaves.place_block(interface, x0-1, y, z0-1)
                tree.palette.leaves.place_block(interface, x0-1, y, z0+1)
                tree.palette.leaves.place_block(interface, x0+1, y, z0-1)
                tree.palette.leaves.place_block(interface, x0+2, y, z0+1)
                tree.palette.leaves.place_block(interface, x0-2, y, z0-1)
                tree.palette.leaves.place_block(interface, x0-2, y, z0+1)
                tree.palette.leaves.place_block(interface, x0+2, y, z0-1)
                tree.palette.leaves.place_block(interface, x0+1, y, z0+2)
                tree.palette.leaves.place_block(interface, x0-1, y, z0-2)
                tree.palette.leaves.place_block(interface, x0-1, y, z0+2)
                tree.palette.leaves.place_block(interface, x0+1, y, z0-2)
            elif y%2 == height%2 and y > y0+2:
                tree.palette.leaves.place_block(interface, x0+2, y, z0)
                tree.palette.leaves.place_block(interface, x0-2, y, z0)
                tree.palette.leaves.place_block(interface, x0, y, z0+2)
                tree.palette.leaves.place_block(interface, x0, y, z0-2)
                tree.palette.leaves.place_block(interface, x0+1, y, z0+1)
                tree.palette.leaves.place_block(interface, x0-1, y, z0-1)
                tree.palette.leaves.place_block(interface, x0-1, y, z0+1)
                tree.palette.leaves.place_block(interface, x0+1, y, z0-1)
                tree.palette.leaves.place_block(interface, x0+1, y, z0)
                tree.palette.leaves.place_block(interface, x0-1, y, z0)
                tree.palette.leaves.place_block(interface, x0, y, z0+1)
                tree.palette.leaves.place_block(interface, x0, y, z0-1)

            elif y%2 == (height-1)%2 and y>y0+1:
                tree.palette.leaves.place_block(interface, x0+2, y, z0)
                tree.palette.leaves.place_block(interface, x0-2, y, z0)
                tree.palette.leaves.place_block(interface, x0, y, z0+2)
                tree.palette.leaves.place_block(interface, x0, y, z0-2)
                tree.palette.leaves.place_block(interface, x0+1, y, z0+1)
                tree.palette.leaves.place_block(interface, x0-1, y, z0-1)
                tree.palette.leaves.place_block(interface, x0-1, y, z0+1)
                tree.palette.leaves.place_block(interface, x0+1, y, z0-1)
                tree.palette.leaves.place_block(interface, x0+2, y, z0+1)
                tree.palette.leaves.place_block(interface, x0-2, y, z0-1)
                tree.palette.leaves.place_block(interface, x0-2, y, z0+1)
                tree.palette.leaves.place_block(interface, x0+2, y, z0-1)
                tree.palette.leaves.place_block(interface, x0+1, y, z0+2)
                tree.palette.leaves.place_block(interface, x0-1, y, z0-2)
                tree.palette.leaves.place_block(interface, x0-1, y, z0+2)
                tree.palette.leaves.place_block(interface, x0+1, y, z0-2)
                tree.palette.leaves.place_block(interface, x0+3, y, z0)
                tree.palette.leaves.place_block(interface, x0-3, y, z0)
                tree.palette.leaves.place_block(interface, x0, y, z0+3)
                tree.palette.leaves.place_block(interface, x0, y, z0-3)
                tree.palette.leaves.place_block(interface, x0+2, y, z0+2)
                tree.palette.leaves.place_block(interface, x0-2, y, z0-2)
                tree.palette.leaves.place_block(interface, x0-2, y, z0+2)
                tree.palette.leaves.place_block(interface, x0+2, y, z0-2)

    def generate_large_pine(self, tree, interface):
        x0, y0, z0 = tree.get_origin()
        seed()
        height = randint(14,21)+y0

        for y in range (y0,height+3):
            if y == height+1:
                tree.palette.leaves.place_block(interface, x0, y, z0)
                tree.palette.leaves.place_block(interface, x0+1, y, z0)
                tree.palette.leaves.place_block(interface, x0-1, y, z0)
                tree.palette.leaves.place_block(interface, x0, y, z0+1)
                tree.palette.leaves.place_block(interface, x0, y, z0-1)
                continue
            elif y == height+2:
                tree.palette.leaves.place_block(interface, x0, y, z0)
                continue
            tree.palette.wood.place_block(interface, x0, y, z0)
            if y == height:
                tree.palette.leaves.place_block(interface, x0+1, y, z0)
                tree.palette.leaves.place_block(interface, x0-1, y, z0)
                tree.palette.leaves.place_block(interface, x0, y, z0+1)
                tree.palette.leaves.place_block(interface, x0, y, z0-1)
            elif y%3 == (height-1)%3 and y > y0+5:
                tree.palette.leaves.place_block(interface, x0+2, y, z0)
                tree.palette.leaves.place_block(interface, x0-2, y, z0)
                tree.palette.leaves.place_block(interface, x0, y, z0+2)
                tree.palette.leaves.place_block(interface, x0, y, z0-2)
                tree.palette.leaves.place_block(interface, x0+1, y, z0+1)
                tree.palette.leaves.place_block(interface, x0-1, y, z0-1)
                tree.palette.leaves.place_block(interface, x0-1, y, z0+1)
                tree.palette.leaves.place_block(interface, x0+1, y, z0-1)
                tree.palette.leaves.place_block(interface, x0+1, y, z0)
                tree.palette.leaves.place_block(interface, x0-1, y, z0)
                tree.palette.leaves.place_block(interface, x0, y, z0+1)
                tree.palette.leaves.place_block(interface, x0, y, z0-1)
            elif y%3 == (height-2)%3 and y > y0+4:
                tree.palette.leaves.place_block(interface, x0+2, y, z0)
                tree.palette.leaves.place_block(interface, x0-2, y, z0)
                tree.palette.leaves.place_block(interface, x0, y, z0+2)
                tree.palette.leaves.place_block(interface, x0, y, z0-2)
                tree.palette.leaves.place_block(interface, x0+1, y, z0+1)
                tree.palette.leaves.place_block(interface, x0-1, y, z0-1)
                tree.palette.leaves.place_block(interface, x0-1, y, z0+1)
                tree.palette.leaves.place_block(interface, x0+1, y, z0-1)
                tree.palette.leaves.place_block(interface, x0+2, y, z0+1)
                tree.palette.leaves.place_block(interface, x0-2, y, z0-1)
                tree.palette.leaves.place_block(interface, x0-2, y, z0+1)
                tree.palette.leaves.place_block(interface, x0+2, y, z0-1)
                tree.palette.leaves.place_block(interface, x0+1, y, z0+2)
                tree.palette.leaves.place_block(interface, x0-1, y, z0-2)
                tree.palette.leaves.place_block(interface, x0-1, y, z0+2)
                tree.palette.leaves.place_block(interface, x0+1, y, z0-2)
                tree.palette.leaves.place_block(interface, x0+3, y, z0)
                tree.palette.leaves.place_block(interface, x0-3, y, z0)
                tree.palette.leaves.place_block(interface, x0, y, z0+3)
                tree.palette.leaves.place_block(interface, x0, y, z0-3)
                tree.palette.leaves.place_block(interface, x0+2, y, z0+2)
                tree.palette.leaves.place_block(interface, x0-2, y, z0-2)
                tree.palette.leaves.place_block(interface, x0-2, y, z0+2)
                tree.palette.leaves.place_block(interface, x0+2, y, z0-2)

            elif y%3 == height%3 and y>y0+3:
                tree.palette.leaves.place_block(interface, x0+2, y, z0)
                tree.palette.leaves.place_block(interface, x0-2, y, z0)
                tree.palette.leaves.place_block(interface, x0, y, z0+2)
                tree.palette.leaves.place_block(interface, x0, y, z0-2)
                tree.palette.leaves.place_block(interface, x0+2, y, z0+1)
                tree.palette.leaves.place_block(interface, x0-2, y, z0-1)
                tree.palette.leaves.place_block(interface, x0-2, y, z0+1)
                tree.palette.leaves.place_block(interface, x0+2, y, z0-1)
                tree.palette.leaves.place_block(interface, x0+1, y, z0+2)
                tree.palette.leaves.place_block(interface, x0-1, y, z0-2)
                tree.palette.leaves.place_block(interface, x0-1, y, z0+2)
                tree.palette.leaves.place_block(interface, x0+1, y, z0-2)
                tree.palette.leaves.place_block(interface, x0+3, y, z0)
                tree.palette.leaves.place_block(interface, x0-3, y, z0)
                tree.palette.leaves.place_block(interface, x0, y, z0+3)
                tree.palette.leaves.place_block(interface, x0, y, z0-3)
                tree.palette.leaves.place_block(interface, x0+2, y, z0+2)
                tree.palette.leaves.place_block(interface, x0-2, y, z0-2)
                tree.palette.leaves.place_block(interface, x0-2, y, z0+2)
                tree.palette.leaves.place_block(interface, x0+2, y, z0-2)
                tree.palette.leaves.place_block(interface, x0+3, y, z0+1)
                tree.palette.leaves.place_block(interface, x0-3, y, z0+1)
                tree.palette.leaves.place_block(interface, x0+1, y, z0+3)
                tree.palette.leaves.place_block(interface, x0+1, y, z0-3)
                tree.palette.leaves.place_block(interface, x0+3, y, z0+2)
                tree.palette.leaves.place_block(interface, x0-3, y, z0+2)
                tree.palette.leaves.place_block(interface, x0+2, y, z0+3)
                tree.palette.leaves.place_block(interface, x0+2, y, z0-3)
                tree.palette.leaves.place_block(interface, x0+3, y, z0-1)
                tree.palette.leaves.place_block(interface, x0-3, y, z0-1)
                tree.palette.leaves.place_block(interface, x0-1, y, z0+3)
                tree.palette.leaves.place_block(interface, x0-1, y, z0-3)
                tree.palette.leaves.place_block(interface, x0+3, y, z0-2)
                tree.palette.leaves.place_block(interface, x0-3, y, z0-2)
                tree.palette.leaves.place_block(interface, x0-2, y, z0+3)
                tree.palette.leaves.place_block(interface, x0-2, y, z0-3)
                tree.palette.leaves.place_block(interface, x0+4, y, z0)
                tree.palette.leaves.place_block(interface, x0-4, y, z0)
                tree.palette.leaves.place_block(interface, x0, y, z0+4)
                tree.palette.leaves.place_block(interface, x0, y, z0-4)

    def generate_small_birch(self, tree, interface):
        x0, y0, z0 = tree.get_origin()
        seed()
        height = randint(5,9)+y0

        for y in range (y0,height+3):
            if y >= height:
                tree.palette.leaves.place_block(interface, x0, y, z0)
            else:
                tree.palette.wood.place_block(interface, x0, y, z0)
            if y==int(height/2)+2 or y==height+1:
                tree.palette.leaves.place_block(interface, x0+1, y, z0)
                tree.palette.leaves.place_block(interface, x0-1, y, z0)
                tree.palette.leaves.place_block(interface, x0, y, z0+1)
                tree.palette.leaves.place_block(interface, x0, y, z0-1)
            elif y > int(height/2)+2 and y < height+2:
                tree.palette.leaves.place_block(interface, x0+1, y, z0+1)
                tree.palette.leaves.place_block(interface, x0-1, y, z0-1)
                tree.palette.leaves.place_block(interface, x0-1, y, z0+1)
                tree.palette.leaves.place_block(interface, x0+1, y, z0-1)
                tree.palette.leaves.place_block(interface, x0+1, y, z0)
                tree.palette.leaves.place_block(interface, x0-1, y, z0)
                tree.palette.leaves.place_block(interface, x0, y, z0+1)
                tree.palette.leaves.place_block(interface, x0, y, z0-1)

    def generate_medium_birch(self, tree, interface):
        x0, y0, z0 = tree.get_origin()
        seed()
        height = randint(10,16)+y0
        branch_num = randint(2,5)
        branches = []
        branches.append([x0, height, z0])
        for y in range (y0,height): #tree stem
            tree.palette.wood.place_block(interface, x0, y, z0)
            if y == y0:
                chance = randint(1,4)
                if chance != 4:
                    tree.palette.wood.place_block(interface, x0+1, y, z0)
                chance = randint(1,4)
                if chance != 4:
                    tree.palette.wood.place_block(interface, x0-1, y, z0)
                chance = randint(1,4)
                if chance != 4:
                    tree.palette.wood.place_block(interface, x0, y, z0+1)
                chance = randint(1,4)
                if chance != 4:
                    tree.palette.wood.place_block(interface, x0, y, z0-1)

        
        for a in range (0, branch_num):
            branch_height = randint(int(height/2)+2, height-1)
            branch_pos = randint(1, 16)
            if branch_pos == 1:
                branches.append([x0+2,branch_height,z0])
                tree.palette.wood.place_block(interface, x0+2, branch_height, z0)
                tree.palette.wood.place_block(interface, x0+2, branch_height-1, z0)
                tree.palette.wood.place_block(interface, x0+1, branch_height-2, z0)
            elif branch_pos == 2:
                branches.append([x0+2,branch_height,z0+1])
                tree.palette.wood.place_block(interface, x0+2,branch_height,z0+1)
                tree.palette.wood.place_block(interface, x0+2,branch_height-1,z0+1)
                b = randint(1,2)
                if b==1:
                    tree.palette.wood.place_block(interface, x0+1,branch_height-2,z0+1)
                else:
                    tree.palette.wood.place_block(interface, x0+1,branch_height-2,z0)
            elif branch_pos == 3:
                branches.append([x0+2,branch_height,z0+2])
                tree.palette.wood.place_block(interface, x0+2,branch_height,z0+2)
                tree.palette.wood.place_block(interface, x0+2,branch_height-1,z0+2)
                tree.palette.wood.place_block(interface, x0+1,branch_height-2,z0+1)
            elif branch_pos == 4:
                branches.append([x0+2,branch_height,z0-1])
                tree.palette.wood.place_block(interface, x0+2, branch_height, z0-1)
                tree.palette.wood.place_block(interface, x0+2, branch_height-1, z0-1)
                b = randint(1,2)
                if b==1:
                    tree.palette.wood.place_block(interface, x0+1,branch_height-2,z0-1)
                else:
                    tree.palette.wood.place_block(interface, x0+1,branch_height-2,z0)
            elif branch_pos == 5:
                branches.append([x0+2,branch_height,z0-2])
                tree.palette.wood.place_block(interface, x0+2, branch_height, z0-2)
                tree.palette.wood.place_block(interface, x0+2, branch_height-1, z0-2)
                tree.palette.wood.place_block(interface, x0+1,branch_height-2,z0-1)
            elif branch_pos == 6:
                branches.append([x0-2,branch_height,z0])
                tree.palette.wood.place_block(interface, x0-2, branch_height, z0)
                tree.palette.wood.place_block(interface, x0-2, branch_height-1, z0)
                tree.palette.wood.place_block(interface, x0-1, branch_height-2, z0)
            elif branch_pos == 7:
                branches.append([x0-2,branch_height,z0+1])
                tree.palette.wood.place_block(interface, x0-2,branch_height,z0+1)
                tree.palette.wood.place_block(interface, x0-2,branch_height-1,z0+1)
                b = randint(1,2)
                if b==1:
                    tree.palette.wood.place_block(interface, x0-1,branch_height-2,z0+1)
                else:
                    tree.palette.wood.place_block(interface, x0-1,branch_height-2,z0)
            elif branch_pos == 8:
                branches.append([x0-2,branch_height,z0+2])
                tree.palette.wood.place_block(interface, x0-2,branch_height,z0+2)
                tree.palette.wood.place_block(interface, x0-2,branch_height-1,z0+2)
                tree.palette.wood.place_block(interface, x0-1,branch_height-2,z0+1)
            elif branch_pos == 9:
                branches.append([x0-2,branch_height,z0-1])
                tree.palette.wood.place_block(interface, x0-2, branch_height, z0-1)
                tree.palette.wood.place_block(interface, x0-2, branch_height-1, z0-1)
                b = randint(1,2)
                if b==1:
                    tree.palette.wood.place_block(interface, x0-1,branch_height-2,z0-1)
                else:
                    tree.palette.wood.place_block(interface, x0-1,branch_height-2,z0)
            elif branch_pos == 10:
                branches.append([x0-2,branch_height,z0-2])
                tree.palette.wood.place_block(interface, x0-2, branch_height, z0-2)
                tree.palette.wood.place_block(interface, x0-2, branch_height-1, z0-2)
                tree.palette.wood.place_block(interface, x0-1,branch_height-2,z0-1)
            elif branch_pos == 11:
                branches.append([x0+1,branch_height,z0-2])
                tree.palette.wood.place_block(interface, x0+1, branch_height, z0-2)
                tree.palette.wood.place_block(interface, x0+1, branch_height-1, z0-2)
                b = randint(1,2)
                if b==1:
                    tree.palette.wood.place_block(interface, x0+1,branch_height-2,z0-1)
                else:
                    tree.palette.wood.place_block(interface, x0,branch_height-2,z0-1)
            elif branch_pos == 12:
                branches.append([x0,branch_height,z0-2])
                tree.palette.wood.place_block(interface, x0, branch_height, z0-2)
                tree.palette.wood.place_block(interface, x0, branch_height-1, z0-2)
                tree.palette.wood.place_block(interface, x0, branch_height-2, z0-1)
            elif branch_pos == 13:
                branches.append([x0-1,branch_height,z0-2])
                tree.palette.wood.place_block(interface, x0-1, branch_height, z0-2)
                tree.palette.wood.place_block(interface, x0-1, branch_height-1, z0-2)
                b = randint(1,2)
                if b==1:
                    tree.palette.wood.place_block(interface, x0-1,branch_height-2,z0-1)
                else:
                    tree.palette.wood.place_block(interface, x0,branch_height-2,z0-1)
            elif branch_pos == 14:
                branches.append([x0+1,branch_height,z0+2])
                tree.palette.wood.place_block(interface, x0+1, branch_height, z0+2)
                tree.palette.wood.place_block(interface, x0+1, branch_height-1, z0+2)
                b = randint(1,2)
                if b==1:
                    tree.palette.wood.place_block(interface, x0+1,branch_height-2,z0+1)
                else:
                    tree.palette.wood.place_block(interface, x0,branch_height-2,z0+1)
            elif branch_pos == 15:
                branches.append([x0,branch_height,z0+2])
                tree.palette.wood.place_block(interface, x0, branch_height, z0+2)
                tree.palette.wood.place_block(interface, x0, branch_height-1, z0+2)
                tree.palette.wood.place_block(interface, x0, branch_height-2, z0+1)
            elif branch_pos == 16:
                branches.append([x0-1,branch_height,z0+2])
                tree.palette.wood.place_block(interface, x0-1, branch_height, z0+2)
                tree.palette.wood.place_block(interface, x0-1, branch_height-1, z0+2)
                b = randint(1,2)
                if b==1:
                    tree.palette.wood.place_block(interface, x0-1,branch_height-2,z0+1)
                else:
                    tree.palette.wood.place_block(interface, x0,branch_height-2,z0+1)

        for branch in branches:
            x1, y1, z1 = branch[0], branch[1], branch[2]

            tree.palette.leaves.place_block(interface, x1, y1+3, z1)

            tree.palette.leaves.place_block(interface, x1, y1+2, z1)
            tree.palette.leaves.place_block(interface, x1+1, y1+2, z1)
            tree.palette.leaves.place_block(interface, x1-1, y1+2, z1)
            tree.palette.leaves.place_block(interface, x1, y1+2, z1+1)
            tree.palette.leaves.place_block(interface, x1, y1+2, z1-1)

            tree.palette.leaves.place_block(interface, x1, y1+1, z1)
            tree.palette.leaves.place_block(interface, x1+1, y1+1, z1+1)
            tree.palette.leaves.place_block(interface, x1-1, y1+1, z1-1)
            tree.palette.leaves.place_block(interface, x1-1, y1+1, z1+1)
            tree.palette.leaves.place_block(interface, x1+1, y1+1, z1-1)
            tree.palette.leaves.place_block(interface, x1+1, y1+1, z1)
            tree.palette.leaves.place_block(interface, x1-1, y1+1, z1)
            tree.palette.leaves.place_block(interface, x1, y1+1, z1+1)
            tree.palette.leaves.place_block(interface, x1, y1+1, z1-1)

            tree.palette.leaves.place_block(interface, x1+1, y1, z1+1)
            tree.palette.leaves.place_block(interface, x1-1, y1, z1-1)
            tree.palette.leaves.place_block(interface, x1-1, y1, z1+1)
            tree.palette.leaves.place_block(interface, x1+1, y1, z1-1)
            tree.palette.leaves.place_block(interface, x1+1, y1, z1)
            tree.palette.leaves.place_block(interface, x1-1, y1, z1)
            tree.palette.leaves.place_block(interface, x1, y1, z1+1)
            tree.palette.leaves.place_block(interface, x1, y1, z1-1)

            tree.palette.leaves.place_block(interface, x1+1, y1-1, z1)
            tree.palette.leaves.place_block(interface, x1-1, y1-1, z1)
            tree.palette.leaves.place_block(interface, x1, y1-1, z1+1)
            tree.palette.leaves.place_block(interface, x1, y1-1, z1-1)

    def generate_large_birch(self, tree, interface):
        x0, y0, z0 = tree.get_origin()
        seed()
        height = randint(16,23)+y0
        branch_num = randint(3,7)
        branches = []
        branches.append([x0, height, z0])
        for y in range (y0,height): #tree stem
            tree.palette.wood.place_block(interface, x0, y, z0)
            if y == y0:
                chance = randint(1,4)
                if chance != 4:
                    tree.palette.wood.place_block(interface, x0+1, y, z0)
                chance = randint(1,4)
                if chance != 4:
                    tree.palette.wood.place_block(interface, x0-1, y, z0)
                chance = randint(1,4)
                if chance != 4:
                    tree.palette.wood.place_block(interface, x0, y, z0+1)
                chance = randint(1,4)
                if chance != 4:
                    tree.palette.wood.place_block(interface, x0, y, z0-1)

        
        for a in range (0, branch_num):
            branch_height = randint(int(height/2)+4, height-1)
            branch_pos = randint(1, 24)
            if branch_pos == 1:
                branches.append([x0+3,branch_height,z0])
                tree.palette.wood.place_block(interface, x0+3, branch_height, z0)
                tree.palette.wood.place_block(interface, x0+3, branch_height-1, z0)
                tree.palette.wood.place_block(interface, x0+3, branch_height-2, z0)
                tree.palette.wood.place_block(interface, x0+2, branch_height-3, z0)
                tree.palette.wood.place_block(interface, x0+1, branch_height-4, z0)
            elif branch_pos == 2:
                branches.append([x0+3,branch_height,z0+1])
                tree.palette.wood.place_block(interface, x0+3,branch_height,z0+1)
                tree.palette.wood.place_block(interface, x0+3,branch_height-1,z0+1)
                tree.palette.wood.place_block(interface, x0+3,branch_height-2,z0+1)
                b = randint(1,3)
                if b==1:
                    tree.palette.wood.place_block(interface, x0+2,branch_height-3,z0+1)
                    tree.palette.wood.place_block(interface, x0+1,branch_height-4,z0+1)
                elif b==2:
                    tree.palette.wood.place_block(interface, x0+2,branch_height-3,z0+1)
                    tree.palette.wood.place_block(interface, x0+1,branch_height-4,z0)
                else:
                    tree.palette.wood.place_block(interface, x0+2,branch_height-3,z0)
                    tree.palette.wood.place_block(interface, x0+1,branch_height-4,z0)
            elif branch_pos == 3:
                branches.append([x0+3,branch_height,z0+3])
                tree.palette.wood.place_block(interface, x0+3, branch_height, z0+3)
                tree.palette.wood.place_block(interface, x0+3, branch_height-1, z0+3)
                tree.palette.wood.place_block(interface, x0+3, branch_height-2, z0+3)
                tree.palette.wood.place_block(interface, x0+2, branch_height-3, z0+2)
                tree.palette.wood.place_block(interface, x0+1, branch_height-4, z0+1)
            elif branch_pos == 4:
                branches.append([x0+3,branch_height,z0-1])
                tree.palette.wood.place_block(interface, x0+3,branch_height,z0-1)
                tree.palette.wood.place_block(interface, x0+3,branch_height-1,z0-1)
                tree.palette.wood.place_block(interface, x0+3,branch_height-2,z0-1)
                b = randint(1,3)
                if b==1:
                    tree.palette.wood.place_block(interface, x0+2,branch_height-3,z0-1)
                    tree.palette.wood.place_block(interface, x0+1,branch_height-4,z0-1)
                elif b==2:
                    tree.palette.wood.place_block(interface, x0+2,branch_height-3,z0-1)
                    tree.palette.wood.place_block(interface, x0+1,branch_height-4,z0)
                else:
                    tree.palette.wood.place_block(interface, x0+2,branch_height-3,z0)
                    tree.palette.wood.place_block(interface, x0+1,branch_height-4,z0)
            elif branch_pos == 5:
                branches.append([x0+3,branch_height,z0-3])
                tree.palette.wood.place_block(interface, x0+3, branch_height, z0-3)
                tree.palette.wood.place_block(interface, x0+3, branch_height-1, z0-3)
                tree.palette.wood.place_block(interface, x0+3, branch_height-2, z0-3)
                tree.palette.wood.place_block(interface, x0+2, branch_height-3, z0-2)
                tree.palette.wood.place_block(interface, x0+1, branch_height-4, z0-1)
            elif branch_pos == 6:
                branches.append([x0-3,branch_height,z0])
                tree.palette.wood.place_block(interface, x0-3, branch_height, z0)
                tree.palette.wood.place_block(interface, x0-3, branch_height-1, z0)
                tree.palette.wood.place_block(interface, x0-3, branch_height-2, z0)
                tree.palette.wood.place_block(interface, x0-2, branch_height-3, z0)
                tree.palette.wood.place_block(interface, x0-1, branch_height-4, z0)
            elif branch_pos == 7:
                branches.append([x0-3,branch_height,z0+1])
                tree.palette.wood.place_block(interface, x0-3,branch_height,z0+1)
                tree.palette.wood.place_block(interface, x0-3,branch_height-1,z0+1)
                tree.palette.wood.place_block(interface, x0+-3,branch_height-2,z0+1)
                b = randint(1,3)
                if b==1:
                    tree.palette.wood.place_block(interface, x0-2,branch_height-3,z0+1)
                    tree.palette.wood.place_block(interface, x0-1,branch_height-4,z0+1)
                elif b==2:
                    tree.palette.wood.place_block(interface, x0-2,branch_height-3,z0+1)
                    tree.palette.wood.place_block(interface, x0-1,branch_height-4,z0)
                else:
                    tree.palette.wood.place_block(interface, x0-2,branch_height-3,z0)
                    tree.palette.wood.place_block(interface, x0-1,branch_height-4,z0)
            elif branch_pos == 8:
                branches.append([x0-3,branch_height,z0+3])
                tree.palette.wood.place_block(interface, x0-3, branch_height, z0+3)
                tree.palette.wood.place_block(interface, x0-3, branch_height-1, z0+3)
                tree.palette.wood.place_block(interface, x0-3, branch_height-2, z0+3)
                tree.palette.wood.place_block(interface, x0-2, branch_height-3, z0+2)
                tree.palette.wood.place_block(interface, x0-1, branch_height-4, z0+1)
            elif branch_pos == 9:
                branches.append([x0-3,branch_height,z0-1])
                tree.palette.wood.place_block(interface, x0-3,branch_height,z0-1)
                tree.palette.wood.place_block(interface, x0-3,branch_height-1,z0-1)
                tree.palette.wood.place_block(interface, x0-3,branch_height-2,z0-1)
                b = randint(1,3)
                if b==1:
                    tree.palette.wood.place_block(interface, x0-2,branch_height-3,z0-1)
                    tree.palette.wood.place_block(interface, x0-1,branch_height-4,z0-1)
                elif b==2:
                    tree.palette.wood.place_block(interface, x0-2,branch_height-3,z0-1)
                    tree.palette.wood.place_block(interface, x0-1,branch_height-4,z0)
                else:
                    tree.palette.wood.place_block(interface, x0-2,branch_height-3,z0)
                    tree.palette.wood.place_block(interface, x0-1,branch_height-4,z0)
            elif branch_pos == 10:
                branches.append([x0-3,branch_height,z0-3])
                tree.palette.wood.place_block(interface, x0-3, branch_height, z0-3)
                tree.palette.wood.place_block(interface, x0-3, branch_height-1, z0-3)
                tree.palette.wood.place_block(interface, x0-3, branch_height-2, z0-3)
                tree.palette.wood.place_block(interface, x0-2, branch_height-3, z0-2)
                tree.palette.wood.place_block(interface, x0-1, branch_height-4, z0-1)
            elif branch_pos == 11:
                branches.append([x0+1,branch_height,z0-3])
                tree.palette.wood.place_block(interface, x0+1, branch_height, z0-3)
                tree.palette.wood.place_block(interface, x0+1, branch_height-1, z0-3)
                tree.palette.wood.place_block(interface, x0+1, branch_height-2, z0-3)
                b = randint(1,3)
                if b==1:
                    tree.palette.wood.place_block(interface, x0+1,branch_height-3,z0-2)
                    tree.palette.wood.place_block(interface, x0+1,branch_height-4,z0-1)
                elif b==2:
                    tree.palette.wood.place_block(interface, x0+1,branch_height-3,z0-2)
                    tree.palette.wood.place_block(interface, x0,branch_height-4,z0-1)
                else:
                    tree.palette.wood.place_block(interface, x0,branch_height-3,z0-2)
                    tree.palette.wood.place_block(interface, x0,branch_height-4,z0-1)
            elif branch_pos == 12:
                branches.append([x0,branch_height,z0-3])
                tree.palette.wood.place_block(interface, x0, branch_height, z0-3)
                tree.palette.wood.place_block(interface, x0, branch_height-1, z0-3)
                tree.palette.wood.place_block(interface, x0, branch_height-2, z0-3)
                tree.palette.wood.place_block(interface, x0, branch_height-3, z0-2)
                tree.palette.wood.place_block(interface, x0, branch_height-4, z0-1)
            elif branch_pos == 13:
                branches.append([x0+1,branch_height,z0-3])
                tree.palette.wood.place_block(interface, x0-1, branch_height, z0-3)
                tree.palette.wood.place_block(interface, x0-1, branch_height-1, z0-3)
                tree.palette.wood.place_block(interface, x0-1, branch_height-2, z0-3)
                b = randint(1,3)
                if b==1:
                    tree.palette.wood.place_block(interface, x0-1,branch_height-3,z0-2)
                    tree.palette.wood.place_block(interface, x0-1,branch_height-4,z0-1)
                elif b==2:
                    tree.palette.wood.place_block(interface, x0-1,branch_height-3,z0-2)
                    tree.palette.wood.place_block(interface, x0,branch_height-4,z0-1)
                else:
                    tree.palette.wood.place_block(interface, x0,branch_height-3,z0-2)
                    tree.palette.wood.place_block(interface, x0,branch_height-4,z0-1)
            elif branch_pos == 14:
                branches.append([x0+1,branch_height,z0+3])
                tree.palette.wood.place_block(interface, x0+1, branch_height, z0+3)
                tree.palette.wood.place_block(interface, x0+1, branch_height-1, z0+3)
                tree.palette.wood.place_block(interface, x0+1, branch_height-2, z0+3)
                b = randint(1,3)
                if b==1:
                    tree.palette.wood.place_block(interface, x0+1,branch_height-3,z0+2)
                    tree.palette.wood.place_block(interface, x0+1,branch_height-4,z0+1)
                elif b==2:
                    tree.palette.wood.place_block(interface, x0+1,branch_height-3,z0+2)
                    tree.palette.wood.place_block(interface, x0,branch_height-4,z0+1)
                else:
                    tree.palette.wood.place_block(interface, x0,branch_height-3,z0+2)
                    tree.palette.wood.place_block(interface, x0,branch_height-4,z0+1)
            elif branch_pos == 15:
                branches.append([x0,branch_height,z0+3])
                tree.palette.wood.place_block(interface, x0, branch_height, z0+3)
                tree.palette.wood.place_block(interface, x0, branch_height-1, z0+3)
                tree.palette.wood.place_block(interface, x0, branch_height-2, z0+3)
                tree.palette.wood.place_block(interface, x0, branch_height-3, z0+2)
                tree.palette.wood.place_block(interface, x0, branch_height-4, z0+1)
            elif branch_pos == 16:
                branches.append([x0+1,branch_height,z0+3])
                tree.palette.wood.place_block(interface, x0-1, branch_height, z0+3)
                tree.palette.wood.place_block(interface, x0-1, branch_height-1, z0+3)
                tree.palette.wood.place_block(interface, x0-1, branch_height-2, z0+3)
                b = randint(1,3)
                if b==1:
                    tree.palette.wood.place_block(interface, x0-1,branch_height-3,z0+2)
                    tree.palette.wood.place_block(interface, x0-1,branch_height-4,z0+1)
                elif b==2:
                    tree.palette.wood.place_block(interface, x0-1,branch_height-3,z0+2)
                    tree.palette.wood.place_block(interface, x0,branch_height-4,z0+1)
                else:
                    tree.palette.wood.place_block(interface, x0,branch_height-3,z0+2)
                    tree.palette.wood.place_block(interface, x0,branch_height-4,z0+1)
            elif branch_pos == 17:
                branches.append([x0+3,branch_height,z0+2])
                tree.palette.wood.place_block(interface, x0+3,branch_height,z0+2)
                tree.palette.wood.place_block(interface, x0+3,branch_height-1,z0+2)
                tree.palette.wood.place_block(interface, x0+3,branch_height-2,z0+2)
                b = randint(1,3)
                if b==1:
                    tree.palette.wood.place_block(interface, x0+2,branch_height-3,z0+2)
                    tree.palette.wood.place_block(interface, x0+1,branch_height-4,z0+1)
                elif b==2:
                    tree.palette.wood.place_block(interface, x0+2,branch_height-3,z0+1)
                    tree.palette.wood.place_block(interface, x0+1,branch_height-4,z0+1)
                else:
                    tree.palette.wood.place_block(interface, x0+2,branch_height-3,z0+1)
                    tree.palette.wood.place_block(interface, x0+1,branch_height-4,z0)
            elif branch_pos == 18:
                branches.append([x0+3,branch_height,z0-2])
                tree.palette.wood.place_block(interface, x0+3,branch_height,z0-2)
                tree.palette.wood.place_block(interface, x0+3,branch_height-1,z0-2)
                tree.palette.wood.place_block(interface, x0+3,branch_height-2,z0-2)
                b = randint(1,3)
                if b==1:
                    tree.palette.wood.place_block(interface, x0+2,branch_height-3,z0-2)
                    tree.palette.wood.place_block(interface, x0+1,branch_height-4,z0-1)
                elif b==2:
                    tree.palette.wood.place_block(interface, x0+2,branch_height-3,z0-1)
                    tree.palette.wood.place_block(interface, x0+1,branch_height-4,z0-1)
                else:
                    tree.palette.wood.place_block(interface, x0+2,branch_height-3,z0-1)
                    tree.palette.wood.place_block(interface, x0+1,branch_height-4,z0)
            elif branch_pos == 19:
                branches.append([x0-3,branch_height,z0+2])
                tree.palette.wood.place_block(interface, x0-3,branch_height,z0+2)
                tree.palette.wood.place_block(interface, x0-3,branch_height-1,z0+2)
                tree.palette.wood.place_block(interface, x0-3,branch_height-2,z0+2)
                b = randint(1,3)
                if b==1:
                    tree.palette.wood.place_block(interface, x0-2,branch_height-3,z0+2)
                    tree.palette.wood.place_block(interface, x0-1,branch_height-4,z0+1)
                elif b==2:
                    tree.palette.wood.place_block(interface, x0-2,branch_height-3,z0+1)
                    tree.palette.wood.place_block(interface, x0-1,branch_height-4,z0+1)
                else:
                    tree.palette.wood.place_block(interface, x0-2,branch_height-3,z0+1)
                    tree.palette.wood.place_block(interface, x0-1,branch_height-4,z0)
            elif branch_pos == 20:
                branches.append([x0-3,branch_height,z0-2])
                tree.palette.wood.place_block(interface, x0-3,branch_height,z0-2)
                tree.palette.wood.place_block(interface, x0-3,branch_height-1,z0-2)
                tree.palette.wood.place_block(interface, x0-3,branch_height-2,z0-2)
                b = randint(1,3)
                if b==1:
                    tree.palette.wood.place_block(interface, x0-2,branch_height-3,z0-2)
                    tree.palette.wood.place_block(interface, x0-1,branch_height-4,z0-1)
                elif b==2:
                    tree.palette.wood.place_block(interface, x0-2,branch_height-3,z0-1)
                    tree.palette.wood.place_block(interface, x0-1,branch_height-4,z0-1)
                else:
                    tree.palette.wood.place_block(interface, x0-2,branch_height-3,z0-1)
                    tree.palette.wood.place_block(interface, x0-1,branch_height-4,z0)
            elif branch_pos == 21:
                branches.append([x0+2,branch_height,z0+3])
                tree.palette.wood.place_block(interface, x0+2,branch_height,z0+3)
                tree.palette.wood.place_block(interface, x0+2,branch_height-1,z0+3)
                tree.palette.wood.place_block(interface, x0+2,branch_height-2,z0+3)
                b = randint(1,3)
                if b==1:
                    tree.palette.wood.place_block(interface, x0+2,branch_height-3,z0+2)
                    tree.palette.wood.place_block(interface, x0+1,branch_height-4,z0+1)
                elif b==2:
                    tree.palette.wood.place_block(interface, x0+1,branch_height-3,z0+2)
                    tree.palette.wood.place_block(interface, x0+1,branch_height-4,z0+1)
                else:
                    tree.palette.wood.place_block(interface, x0+1,branch_height-3,z0+2)
                    tree.palette.wood.place_block(interface, x0,branch_height-4,z0+1)
            elif branch_pos == 22:
                branches.append([x0-2,branch_height,z0+3])
                tree.palette.wood.place_block(interface, x0-2,branch_height,z0+3)
                tree.palette.wood.place_block(interface, x0-2,branch_height-1,z0+3)
                tree.palette.wood.place_block(interface, x0-2,branch_height-2,z0+3)
                b = randint(1,3)
                if b==1:
                    tree.palette.wood.place_block(interface, x0-2,branch_height-3,z0+2)
                    tree.palette.wood.place_block(interface, x0-1,branch_height-4,z0+1)
                elif b==2:
                    tree.palette.wood.place_block(interface, x0-1,branch_height-3,z0+2)
                    tree.palette.wood.place_block(interface, x0-1,branch_height-4,z0+1)
                else:
                    tree.palette.wood.place_block(interface, x0-1,branch_height-3,z0+2)
                    tree.palette.wood.place_block(interface, x0,branch_height-4,z0+1)
            elif branch_pos == 23:
                branches.append([x0+2,branch_height,z0-3])
                tree.palette.wood.place_block(interface, x0+2,branch_height,z0-3)
                tree.palette.wood.place_block(interface, x0+2,branch_height-1,z0-3)
                tree.palette.wood.place_block(interface, x0+2,branch_height-2,z0-3)
                b = randint(1,3)
                if b==1:
                    tree.palette.wood.place_block(interface, x0+2,branch_height-3,z0-2)
                    tree.palette.wood.place_block(interface, x0+1,branch_height-4,z0-1)
                elif b==2:
                    tree.palette.wood.place_block(interface, x0+1,branch_height-3,z0-2)
                    tree.palette.wood.place_block(interface, x0+1,branch_height-4,z0-1)
                else:
                    tree.palette.wood.place_block(interface, x0+1,branch_height-3,z0-2)
                    tree.palette.wood.place_block(interface, x0,branch_height-4,z0-1)
            elif branch_pos == 24:
                branches.append([x0-2,branch_height,z0-3])
                tree.palette.wood.place_block(interface, x0-2,branch_height,z0-3)
                tree.palette.wood.place_block(interface, x0-2,branch_height-1,z0-3)
                tree.palette.wood.place_block(interface, x0-2,branch_height-2,z0-3)
                b = randint(1,3)
                if b==1:
                    tree.palette.wood.place_block(interface, x0-2,branch_height-3,z0-2)
                    tree.palette.wood.place_block(interface, x0-1,branch_height-4,z0-1)
                elif b==2:
                    tree.palette.wood.place_block(interface, x0-1,branch_height-3,z0-2)
                    tree.palette.wood.place_block(interface, x0-1,branch_height-4,z0-1)
                else:
                    tree.palette.wood.place_block(interface, x0-1,branch_height-3,z0-2)
                    tree.palette.wood.place_block(interface, x0,branch_height-4,z0-1)

        for branch in branches:
            x1, y1, z1 = branch[0], branch[1], branch[2]

            tree.palette.leaves.place_block(interface, x1, y1+4, z1)

            tree.palette.leaves.place_block(interface, x1, y1+3, z1)
            tree.palette.leaves.place_block(interface, x1+1, y1+3, z1)
            tree.palette.leaves.place_block(interface, x1-1, y1+3, z1)
            tree.palette.leaves.place_block(interface, x1, y1+3, z1+1)
            tree.palette.leaves.place_block(interface, x1, y1+3, z1-1)

            tree.palette.leaves.place_block(interface, x1, y1+2, z1)
            tree.palette.leaves.place_block(interface, x1+1, y1+2, z1+1)
            tree.palette.leaves.place_block(interface, x1-1, y1+2, z1-1)
            tree.palette.leaves.place_block(interface, x1-1, y1+2, z1+1)
            tree.palette.leaves.place_block(interface, x1+1, y1+2, z1-1)
            tree.palette.leaves.place_block(interface, x1+1, y1+2, z1)
            tree.palette.leaves.place_block(interface, x1-1, y1+2, z1)
            tree.palette.leaves.place_block(interface, x1, y1+2, z1+1)
            tree.palette.leaves.place_block(interface, x1, y1+2, z1-1)
            tree.palette.leaves.place_block(interface, x1+2, y1+2, z1)
            tree.palette.leaves.place_block(interface, x1-2, y1+2, z1)
            tree.palette.leaves.place_block(interface, x1, y1+2, z1+2)
            tree.palette.leaves.place_block(interface, x1, y1+2, z1-2)

            tree.palette.leaves.place_block(interface, x1, y1+1, z1)
            tree.palette.leaves.place_block(interface, x1+1, y1+1, z1+1)
            tree.palette.leaves.place_block(interface, x1-1, y1+1, z1-1)
            tree.palette.leaves.place_block(interface, x1-1, y1+1, z1+1)
            tree.palette.leaves.place_block(interface, x1+1, y1+1, z1-1)
            tree.palette.leaves.place_block(interface, x1+1, y1+1, z1)
            tree.palette.leaves.place_block(interface, x1-1, y1+1, z1)
            tree.palette.leaves.place_block(interface, x1, y1+1, z1+1)
            tree.palette.leaves.place_block(interface, x1, y1+1, z1-1)
            tree.palette.leaves.place_block(interface, x1+2, y1+1, z1)
            tree.palette.leaves.place_block(interface, x1-2, y1+1, z1)
            tree.palette.leaves.place_block(interface, x1, y1+1, z1+2)
            tree.palette.leaves.place_block(interface, x1, y1+1, z1-2)
            tree.palette.leaves.place_block(interface, x1+2, y1+1, z1-1)
            tree.palette.leaves.place_block(interface, x1-2, y1+1, z1-1)
            tree.palette.leaves.place_block(interface, x1-1, y1+1, z1+2)
            tree.palette.leaves.place_block(interface, x1-1, y1+1, z1-2)
            tree.palette.leaves.place_block(interface, x1+2, y1+1, z1+1)
            tree.palette.leaves.place_block(interface, x1-2, y1+1, z1+1)
            tree.palette.leaves.place_block(interface, x1+1, y1+1, z1+2)
            tree.palette.leaves.place_block(interface, x1+1, y1+1, z1-2)
            
            tree.palette.leaves.place_block(interface, x1+1, y1, z1+1)
            tree.palette.leaves.place_block(interface, x1-1, y1, z1-1)
            tree.palette.leaves.place_block(interface, x1-1, y1, z1+1)
            tree.palette.leaves.place_block(interface, x1+1, y1, z1-1)
            tree.palette.leaves.place_block(interface, x1+1, y1, z1)
            tree.palette.leaves.place_block(interface, x1-1, y1, z1)
            tree.palette.leaves.place_block(interface, x1, y1, z1+1)
            tree.palette.leaves.place_block(interface, x1, y1, z1-1)
            tree.palette.leaves.place_block(interface, x1+2, y1, z1)
            tree.palette.leaves.place_block(interface, x1-2, y1, z1)
            tree.palette.leaves.place_block(interface, x1, y1, z1+2)
            tree.palette.leaves.place_block(interface, x1, y1, z1-2)

            tree.palette.leaves.place_block(interface, x1+1, y1-1, z1)
            tree.palette.leaves.place_block(interface, x1-1, y1-1, z1)
            tree.palette.leaves.place_block(interface, x1, y1-1, z1+1)
            tree.palette.leaves.place_block(interface, x1, y1-1, z1-1)
            tree.palette.leaves.place_block(interface, x1+1, y1-1, z1+1)
            tree.palette.leaves.place_block(interface, x1-1, y1-1, z1-1)
            tree.palette.leaves.place_block(interface, x1-1, y1-1, z1+1)
            tree.palette.leaves.place_block(interface, x1+1, y1-1, z1-1)
            tree.palette.leaves.place_block(interface, x1+1, y1-2, z1)
            tree.palette.leaves.place_block(interface, x1-1, y1-2, z1)
            tree.palette.leaves.place_block(interface, x1, y1-2, z1+1)
            tree.palette.leaves.place_block(interface, x1, y1-2, z1-1)
            
