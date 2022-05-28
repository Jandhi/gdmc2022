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
            self.generate_medium_pine(tree, interface, 95)
        elif tree.type == 'small_pine':
            self.generate_small_pine(tree, interface)
        elif tree.type == 'large_pine':
            self.generate_large_pine(tree, interface, 95)
        elif tree.type == 'mega_pine':
            self.generate_mega_pine(tree, interface, 95)
        elif tree.type == 'small_birch':
            self.generate_small_birch(tree, interface, 98)
        elif tree.type == 'medium_birch':
            self.generate_medium_birch(tree, interface, 96)
        elif tree.type == 'large_birch':
            self.generate_large_birch(tree, interface, 95)
        elif tree.type == 'mega_birch':
            self.generate_mega_birch(tree, interface, 93)
        elif tree.type == 'small_hedge':
            self.generate_small_hedge(tree, interface)
        elif tree.type == 'medium_hedge':
            self.generate_medium_hedge(tree, interface)
        elif tree.type == 'large_hedge':
            self.generate_large_hedge(tree, interface)
        elif tree.type == 'mega_hedge':
            self.generate_mega_hedge(tree, interface, 98)
        elif tree.type == 'small_baobab':
            self.generate_small_baobab(tree, interface)
        elif tree.type == 'medium_baobab':
            self.generate_medium_baobab(tree, interface)
        elif tree.type == 'large_baobab':
            self.generate_large_baobab(tree, interface)
        elif tree.type == 'small_oak':
            self.generate_small_oak(tree, interface)
        elif tree.type == 'medium_oak':
            self.generate_medium_oak(tree, interface)
        elif tree.type == 'large_oak':
            self.generate_large_oak(tree, interface)
        elif tree.type == 'mega_oak':
            self.generate_mega_oak(tree, interface, 96)
        elif tree.type == 'small_jungle':
            self.generate_small_jungle(tree, interface)
        elif tree.type == 'medium_jungle':
            self.generate_medium_jungle(tree, interface)
        elif tree.type == 'large_jungle':
            self.generate_large_jungle(tree, interface)
        elif tree.type == 'mega_jungle':
            self.generate_mega_jungle(tree, interface)

    def generate_small_pine(self, tree, interface, leaf_chance: int=100):
        x0, y0, z0 = tree.get_origin()
        seed()
        height = randint(5,7)+y0

        for y in range (y0,height+2):
            if y == height+1:
                tree.palette.leaves.place_block(interface, x0, y, z0, leaf_chance)
                continue
            tree.palette.wood.place_block(interface, x0, y, z0)
            if y%2 == height%2 and y > y0+1:
                tree.palette.leaves.place_block(interface, x0+1, y, z0, leaf_chance)
                tree.palette.leaves.place_block(interface, x0-1, y, z0, leaf_chance)
                tree.palette.leaves.place_block(interface, x0, y, z0+1, leaf_chance)
                tree.palette.leaves.place_block(interface, x0, y, z0-1, leaf_chance)
            elif y == height-1:
                tree.palette.leaves.place_block(interface, x0+1, y, z0+1, leaf_chance)
                tree.palette.leaves.place_block(interface, x0-1, y, z0-1, leaf_chance)
                tree.palette.leaves.place_block(interface, x0-1, y, z0+1, leaf_chance)
                tree.palette.leaves.place_block(interface, x0+1, y, z0-1, leaf_chance)
                tree.palette.leaves.place_block(interface, x0+1, y, z0, leaf_chance)
                tree.palette.leaves.place_block(interface, x0-1, y, z0, leaf_chance)
                tree.palette.leaves.place_block(interface, x0, y, z0+1, leaf_chance)
                tree.palette.leaves.place_block(interface, x0, y, z0-1, leaf_chance)
            elif y%2 == (height-1)%2 and y>y0:
                tree.palette.leaves.place_block(interface, x0+2, y, z0, leaf_chance)
                tree.palette.leaves.place_block(interface, x0-2, y, z0, leaf_chance)
                tree.palette.leaves.place_block(interface, x0, y, z0+2, leaf_chance)
                tree.palette.leaves.place_block(interface, x0, y, z0-2, leaf_chance)
                tree.palette.leaves.place_block(interface, x0+1, y, z0+1, leaf_chance)
                tree.palette.leaves.place_block(interface, x0-1, y, z0-1, leaf_chance)
                tree.palette.leaves.place_block(interface, x0-1, y, z0+1, leaf_chance)
                tree.palette.leaves.place_block(interface, x0+1, y, z0-1, leaf_chance)
                tree.palette.leaves.place_block(interface, x0+1, y, z0, leaf_chance)
                tree.palette.leaves.place_block(interface, x0-1, y, z0, leaf_chance)
                tree.palette.leaves.place_block(interface, x0, y, z0+1, leaf_chance)
                tree.palette.leaves.place_block(interface, x0, y, z0-1, leaf_chance)
                
    def generate_medium_pine(self, tree, interface, leaf_chance: int=100):
        x0, y0, z0 = tree.get_origin()
        seed()
        height = randint(8,13)+y0

        for y in range (y0,height+2):
            if y == height+1:
                tree.palette.leaves.place_block(interface, x0, y, z0, leaf_chance)
                continue
            tree.palette.wood.place_block(interface, x0, y, z0)
            if y == height:
                tree.palette.leaves.place_block(interface, x0+1, y, z0, leaf_chance)
                tree.palette.leaves.place_block(interface, x0-1, y, z0, leaf_chance)
                tree.palette.leaves.place_block(interface, x0, y, z0+1, leaf_chance)
                tree.palette.leaves.place_block(interface, x0, y, z0-1, leaf_chance)
            elif y == height-1:
                tree.palette.leaves.place_block(interface, x0+2, y, z0, leaf_chance)
                tree.palette.leaves.place_block(interface, x0-2, y, z0, leaf_chance)
                tree.palette.leaves.place_block(interface, x0, y, z0+2, leaf_chance)
                tree.palette.leaves.place_block(interface, x0, y, z0-2, leaf_chance)
                tree.palette.leaves.place_block(interface, x0+1, y, z0+1, leaf_chance)
                tree.palette.leaves.place_block(interface, x0-1, y, z0-1, leaf_chance)
                tree.palette.leaves.place_block(interface, x0-1, y, z0+1, leaf_chance)
                tree.palette.leaves.place_block(interface, x0+1, y, z0-1, leaf_chance)
                tree.palette.leaves.place_block(interface, x0+2, y, z0+1, leaf_chance)
                tree.palette.leaves.place_block(interface, x0-2, y, z0-1, leaf_chance)
                tree.palette.leaves.place_block(interface, x0-2, y, z0+1, leaf_chance)
                tree.palette.leaves.place_block(interface, x0+2, y, z0-1, leaf_chance)
                tree.palette.leaves.place_block(interface, x0+1, y, z0+2, leaf_chance)
                tree.palette.leaves.place_block(interface, x0-1, y, z0-2, leaf_chance)
                tree.palette.leaves.place_block(interface, x0-1, y, z0+2, leaf_chance)
                tree.palette.leaves.place_block(interface, x0+1, y, z0-2, leaf_chance)
            elif y%2 == height%2 and y > y0+2:
                tree.palette.leaves.place_block(interface, x0+2, y, z0, leaf_chance)
                tree.palette.leaves.place_block(interface, x0-2, y, z0, leaf_chance)
                tree.palette.leaves.place_block(interface, x0, y, z0+2, leaf_chance)
                tree.palette.leaves.place_block(interface, x0, y, z0-2, leaf_chance)
                tree.palette.leaves.place_block(interface, x0+1, y, z0+1, leaf_chance)
                tree.palette.leaves.place_block(interface, x0-1, y, z0-1, leaf_chance)
                tree.palette.leaves.place_block(interface, x0-1, y, z0+1, leaf_chance)
                tree.palette.leaves.place_block(interface, x0+1, y, z0-1, leaf_chance)
                tree.palette.leaves.place_block(interface, x0+1, y, z0, leaf_chance)
                tree.palette.leaves.place_block(interface, x0-1, y, z0, leaf_chance)
                tree.palette.leaves.place_block(interface, x0, y, z0+1, leaf_chance)
                tree.palette.leaves.place_block(interface, x0, y, z0-1, leaf_chance)

            elif y%2 == (height-1)%2 and y>y0+1:
                tree.palette.leaves.place_block(interface, x0+2, y, z0, leaf_chance)
                tree.palette.leaves.place_block(interface, x0-2, y, z0, leaf_chance)
                tree.palette.leaves.place_block(interface, x0, y, z0+2, leaf_chance)
                tree.palette.leaves.place_block(interface, x0, y, z0-2, leaf_chance)
                tree.palette.leaves.place_block(interface, x0+1, y, z0+1, leaf_chance)
                tree.palette.leaves.place_block(interface, x0-1, y, z0-1, leaf_chance)
                tree.palette.leaves.place_block(interface, x0-1, y, z0+1, leaf_chance)
                tree.palette.leaves.place_block(interface, x0+1, y, z0-1, leaf_chance)
                tree.palette.leaves.place_block(interface, x0+2, y, z0+1, leaf_chance)
                tree.palette.leaves.place_block(interface, x0-2, y, z0-1, leaf_chance)
                tree.palette.leaves.place_block(interface, x0-2, y, z0+1, leaf_chance)
                tree.palette.leaves.place_block(interface, x0+2, y, z0-1, leaf_chance)
                tree.palette.leaves.place_block(interface, x0+1, y, z0+2, leaf_chance)
                tree.palette.leaves.place_block(interface, x0-1, y, z0-2, leaf_chance)
                tree.palette.leaves.place_block(interface, x0-1, y, z0+2, leaf_chance)
                tree.palette.leaves.place_block(interface, x0+1, y, z0-2, leaf_chance)
                tree.palette.leaves.place_block(interface, x0+3, y, z0, leaf_chance)
                tree.palette.leaves.place_block(interface, x0-3, y, z0, leaf_chance)
                tree.palette.leaves.place_block(interface, x0, y, z0+3, leaf_chance)
                tree.palette.leaves.place_block(interface, x0, y, z0-3, leaf_chance)
                tree.palette.leaves.place_block(interface, x0+2, y, z0+2, leaf_chance)
                tree.palette.leaves.place_block(interface, x0-2, y, z0-2, leaf_chance)
                tree.palette.leaves.place_block(interface, x0-2, y, z0+2, leaf_chance)
                tree.palette.leaves.place_block(interface, x0+2, y, z0-2, leaf_chance)

    def generate_large_pine(self, tree, interface, leaf_chance: int=100):
        x0, y0, z0 = tree.get_origin()
        seed()
        height = randint(14,21)+y0

        for y in range (y0,height+3):
            if y == height+1:
                tree.palette.leaves.place_block(interface, x0, y, z0, leaf_chance)
                tree.palette.leaves.place_block(interface, x0+1, y, z0, leaf_chance)
                tree.palette.leaves.place_block(interface, x0-1, y, z0, leaf_chance)
                tree.palette.leaves.place_block(interface, x0, y, z0+1, leaf_chance)
                tree.palette.leaves.place_block(interface, x0, y, z0-1, leaf_chance)
                continue
            elif y == height+2:
                tree.palette.leaves.place_block(interface, x0, y, z0, leaf_chance)
                continue
            tree.palette.wood.place_block(interface, x0, y, z0)
            if y == height:
                tree.palette.leaves.place_block(interface, x0+1, y, z0, leaf_chance)
                tree.palette.leaves.place_block(interface, x0-1, y, z0, leaf_chance)
                tree.palette.leaves.place_block(interface, x0, y, z0+1, leaf_chance)
                tree.palette.leaves.place_block(interface, x0, y, z0-1, leaf_chance)
            elif y%3 == (height-1)%3 and y > y0+5:
                tree.palette.leaves.place_block(interface, x0+2, y, z0, leaf_chance)
                tree.palette.leaves.place_block(interface, x0-2, y, z0, leaf_chance)
                tree.palette.leaves.place_block(interface, x0, y, z0+2, leaf_chance)
                tree.palette.leaves.place_block(interface, x0, y, z0-2, leaf_chance)
                tree.palette.leaves.place_block(interface, x0+1, y, z0+1, leaf_chance)
                tree.palette.leaves.place_block(interface, x0-1, y, z0-1, leaf_chance)
                tree.palette.leaves.place_block(interface, x0-1, y, z0+1, leaf_chance)
                tree.palette.leaves.place_block(interface, x0+1, y, z0-1, leaf_chance)
                tree.palette.leaves.place_block(interface, x0+1, y, z0, leaf_chance)
                tree.palette.leaves.place_block(interface, x0-1, y, z0, leaf_chance)
                tree.palette.leaves.place_block(interface, x0, y, z0+1, leaf_chance)
                tree.palette.leaves.place_block(interface, x0, y, z0-1, leaf_chance)
            elif y%3 == (height-2)%3 and y > y0+4:
                tree.palette.leaves.place_block(interface, x0+2, y, z0, leaf_chance)
                tree.palette.leaves.place_block(interface, x0-2, y, z0, leaf_chance)
                tree.palette.leaves.place_block(interface, x0, y, z0+2, leaf_chance)
                tree.palette.leaves.place_block(interface, x0, y, z0-2, leaf_chance)
                tree.palette.leaves.place_block(interface, x0+1, y, z0+1, leaf_chance)
                tree.palette.leaves.place_block(interface, x0-1, y, z0-1, leaf_chance)
                tree.palette.leaves.place_block(interface, x0-1, y, z0+1, leaf_chance)
                tree.palette.leaves.place_block(interface, x0+1, y, z0-1, leaf_chance)
                tree.palette.leaves.place_block(interface, x0+2, y, z0+1, leaf_chance)
                tree.palette.leaves.place_block(interface, x0-2, y, z0-1, leaf_chance)
                tree.palette.leaves.place_block(interface, x0-2, y, z0+1, leaf_chance)
                tree.palette.leaves.place_block(interface, x0+2, y, z0-1, leaf_chance)
                tree.palette.leaves.place_block(interface, x0+1, y, z0+2, leaf_chance)
                tree.palette.leaves.place_block(interface, x0-1, y, z0-2, leaf_chance)
                tree.palette.leaves.place_block(interface, x0-1, y, z0+2, leaf_chance)
                tree.palette.leaves.place_block(interface, x0+1, y, z0-2, leaf_chance)
                tree.palette.leaves.place_block(interface, x0+3, y, z0, leaf_chance)
                tree.palette.leaves.place_block(interface, x0-3, y, z0, leaf_chance)
                tree.palette.leaves.place_block(interface, x0, y, z0+3, leaf_chance)
                tree.palette.leaves.place_block(interface, x0, y, z0-3, leaf_chance)
                tree.palette.leaves.place_block(interface, x0+2, y, z0+2, leaf_chance)
                tree.palette.leaves.place_block(interface, x0-2, y, z0-2, leaf_chance)
                tree.palette.leaves.place_block(interface, x0-2, y, z0+2, leaf_chance)
                tree.palette.leaves.place_block(interface, x0+2, y, z0-2, leaf_chance)

            elif y%3 == height%3 and y>y0+3:
                tree.palette.leaves.place_block(interface, x0+2, y, z0, leaf_chance)
                tree.palette.leaves.place_block(interface, x0-2, y, z0, leaf_chance)
                tree.palette.leaves.place_block(interface, x0, y, z0+2, leaf_chance)
                tree.palette.leaves.place_block(interface, x0, y, z0-2, leaf_chance)
                tree.palette.leaves.place_block(interface, x0+2, y, z0+1, leaf_chance)
                tree.palette.leaves.place_block(interface, x0-2, y, z0-1, leaf_chance)
                tree.palette.leaves.place_block(interface, x0-2, y, z0+1, leaf_chance)
                tree.palette.leaves.place_block(interface, x0+2, y, z0-1, leaf_chance)
                tree.palette.leaves.place_block(interface, x0+1, y, z0+2, leaf_chance)
                tree.palette.leaves.place_block(interface, x0-1, y, z0-2, leaf_chance)
                tree.palette.leaves.place_block(interface, x0-1, y, z0+2, leaf_chance)
                tree.palette.leaves.place_block(interface, x0+1, y, z0-2, leaf_chance)
                tree.palette.leaves.place_block(interface, x0+3, y, z0, leaf_chance)
                tree.palette.leaves.place_block(interface, x0-3, y, z0, leaf_chance)
                tree.palette.leaves.place_block(interface, x0, y, z0+3, leaf_chance)
                tree.palette.leaves.place_block(interface, x0, y, z0-3, leaf_chance)
                tree.palette.leaves.place_block(interface, x0+2, y, z0+2, leaf_chance)
                tree.palette.leaves.place_block(interface, x0-2, y, z0-2, leaf_chance)
                tree.palette.leaves.place_block(interface, x0-2, y, z0+2, leaf_chance)
                tree.palette.leaves.place_block(interface, x0+2, y, z0-2, leaf_chance)
                tree.palette.leaves.place_block(interface, x0+3, y, z0+1, leaf_chance)
                tree.palette.leaves.place_block(interface, x0-3, y, z0+1, leaf_chance)
                tree.palette.leaves.place_block(interface, x0+1, y, z0+3, leaf_chance)
                tree.palette.leaves.place_block(interface, x0+1, y, z0-3, leaf_chance)
                tree.palette.leaves.place_block(interface, x0+3, y, z0+2, leaf_chance)
                tree.palette.leaves.place_block(interface, x0-3, y, z0+2, leaf_chance)
                tree.palette.leaves.place_block(interface, x0+2, y, z0+3, leaf_chance)
                tree.palette.leaves.place_block(interface, x0+2, y, z0-3, leaf_chance)
                tree.palette.leaves.place_block(interface, x0+3, y, z0-1, leaf_chance)
                tree.palette.leaves.place_block(interface, x0-3, y, z0-1, leaf_chance)
                tree.palette.leaves.place_block(interface, x0-1, y, z0+3, leaf_chance)
                tree.palette.leaves.place_block(interface, x0-1, y, z0-3, leaf_chance)
                tree.palette.leaves.place_block(interface, x0+3, y, z0-2, leaf_chance)
                tree.palette.leaves.place_block(interface, x0-3, y, z0-2, leaf_chance)
                tree.palette.leaves.place_block(interface, x0-2, y, z0+3, leaf_chance)
                tree.palette.leaves.place_block(interface, x0-2, y, z0-3, leaf_chance)
                tree.palette.leaves.place_block(interface, x0+4, y, z0, leaf_chance)
                tree.palette.leaves.place_block(interface, x0-4, y, z0, leaf_chance)
                tree.palette.leaves.place_block(interface, x0, y, z0+4, leaf_chance)
                tree.palette.leaves.place_block(interface, x0, y, z0-4, leaf_chance)

    def generate_mega_pine(self, tree, interface, leaf_chance: int=100):
        self.generate_large_pine(tree, interface, leaf_chance)
        x0, y0, z0 = tree.get_origin()
        new_tree = Tree((x0+1, y0, z0), tree.type)
        self.generate_large_pine(new_tree, interface, leaf_chance)
        new_tree = Tree((x0+1, y0, z0+1), tree.type)
        self.generate_large_pine(new_tree, interface, leaf_chance)
        new_tree = Tree((x0, y0, z0+1), tree.type)
        self.generate_large_pine(new_tree, interface, leaf_chance)

    def generate_small_birch(self, tree, interface, leaf_chance: int=100):
        x0, y0, z0 = tree.get_origin()
        seed()
        height = randint(5,9)+y0

        for y in range (y0,height+3):
            if y >= height:
                tree.palette.leaves.place_block(interface, x0, y, z0, leaf_chance)
            else:
                tree.palette.wood.place_block(interface, x0, y, z0)
            if y==int(height/2)+2 or y==height+1:
                tree.palette.leaves.place_block(interface, x0+1, y, z0, leaf_chance)
                tree.palette.leaves.place_block(interface, x0-1, y, z0, leaf_chance)
                tree.palette.leaves.place_block(interface, x0, y, z0+1, leaf_chance)
                tree.palette.leaves.place_block(interface, x0, y, z0-1, leaf_chance)
            elif y > int(height/2)+2 and y < height+2:
                tree.palette.leaves.place_block(interface, x0+1, y, z0+1, leaf_chance)
                tree.palette.leaves.place_block(interface, x0-1, y, z0-1, leaf_chance)
                tree.palette.leaves.place_block(interface, x0-1, y, z0+1, leaf_chance)
                tree.palette.leaves.place_block(interface, x0+1, y, z0-1, leaf_chance)
                tree.palette.leaves.place_block(interface, x0+1, y, z0, leaf_chance)
                tree.palette.leaves.place_block(interface, x0-1, y, z0, leaf_chance)
                tree.palette.leaves.place_block(interface, x0, y, z0+1, leaf_chance)
                tree.palette.leaves.place_block(interface, x0, y, z0-1, leaf_chance)

    def generate_medium_birch(self, tree, interface, leaf_chance: int=100):
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
            branch_height = randint(int((height-y0)/2+y0)+2, height-1)
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

            tree.palette.leaves.place_block(interface, x1, y1+3, z1, leaf_chance)

            tree.palette.leaves.place_block(interface, x1, y1+2, z1, leaf_chance)
            tree.palette.leaves.place_block(interface, x1+1, y1+2, z1, leaf_chance)
            tree.palette.leaves.place_block(interface, x1-1, y1+2, z1, leaf_chance)
            tree.palette.leaves.place_block(interface, x1, y1+2, z1+1, leaf_chance)
            tree.palette.leaves.place_block(interface, x1, y1+2, z1-1, leaf_chance)

            tree.palette.leaves.place_block(interface, x1, y1+1, z1, leaf_chance)
            tree.palette.leaves.place_block(interface, x1+1, y1+1, z1+1, leaf_chance)
            tree.palette.leaves.place_block(interface, x1-1, y1+1, z1-1, leaf_chance)
            tree.palette.leaves.place_block(interface, x1-1, y1+1, z1+1, leaf_chance)
            tree.palette.leaves.place_block(interface, x1+1, y1+1, z1-1, leaf_chance)
            tree.palette.leaves.place_block(interface, x1+1, y1+1, z1, leaf_chance)
            tree.palette.leaves.place_block(interface, x1-1, y1+1, z1, leaf_chance)
            tree.palette.leaves.place_block(interface, x1, y1+1, z1+1, leaf_chance)
            tree.palette.leaves.place_block(interface, x1, y1+1, z1-1, leaf_chance)

            tree.palette.leaves.place_block(interface, x1+1, y1, z1+1, leaf_chance)
            tree.palette.leaves.place_block(interface, x1-1, y1, z1-1, leaf_chance)
            tree.palette.leaves.place_block(interface, x1-1, y1, z1+1, leaf_chance)
            tree.palette.leaves.place_block(interface, x1+1, y1, z1-1, leaf_chance)
            tree.palette.leaves.place_block(interface, x1+1, y1, z1, leaf_chance)
            tree.palette.leaves.place_block(interface, x1-1, y1, z1, leaf_chance)
            tree.palette.leaves.place_block(interface, x1, y1, z1+1, leaf_chance)
            tree.palette.leaves.place_block(interface, x1, y1, z1-1, leaf_chance)

            tree.palette.leaves.place_block(interface, x1+1, y1-1, z1, leaf_chance)
            tree.palette.leaves.place_block(interface, x1-1, y1-1, z1, leaf_chance)
            tree.palette.leaves.place_block(interface, x1, y1-1, z1+1, leaf_chance)
            tree.palette.leaves.place_block(interface, x1, y1-1, z1-1, leaf_chance)

    def generate_large_birch(self, tree, interface, leaf_chance: int=100):
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
            branch_height = randint(int((height-y0)/2+y0)+4, height-1)
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

            tree.palette.leaves.place_block(interface, x1, y1+4, z1, leaf_chance)

            tree.palette.leaves.place_block(interface, x1, y1+3, z1, leaf_chance)
            tree.palette.leaves.place_block(interface, x1+1, y1+3, z1, leaf_chance)
            tree.palette.leaves.place_block(interface, x1-1, y1+3, z1, leaf_chance)
            tree.palette.leaves.place_block(interface, x1, y1+3, z1+1, leaf_chance)
            tree.palette.leaves.place_block(interface, x1, y1+3, z1-1, leaf_chance)

            tree.palette.leaves.place_block(interface, x1, y1+2, z1, leaf_chance)
            tree.palette.leaves.place_block(interface, x1+1, y1+2, z1+1, leaf_chance)
            tree.palette.leaves.place_block(interface, x1-1, y1+2, z1-1, leaf_chance)
            tree.palette.leaves.place_block(interface, x1-1, y1+2, z1+1, leaf_chance)
            tree.palette.leaves.place_block(interface, x1+1, y1+2, z1-1, leaf_chance)
            tree.palette.leaves.place_block(interface, x1+1, y1+2, z1, leaf_chance)
            tree.palette.leaves.place_block(interface, x1-1, y1+2, z1, leaf_chance)
            tree.palette.leaves.place_block(interface, x1, y1+2, z1+1, leaf_chance)
            tree.palette.leaves.place_block(interface, x1, y1+2, z1-1, leaf_chance)
            tree.palette.leaves.place_block(interface, x1+2, y1+2, z1, leaf_chance)
            tree.palette.leaves.place_block(interface, x1-2, y1+2, z1, leaf_chance)
            tree.palette.leaves.place_block(interface, x1, y1+2, z1+2, leaf_chance)
            tree.palette.leaves.place_block(interface, x1, y1+2, z1-2, leaf_chance)

            tree.palette.leaves.place_block(interface, x1, y1+1, z1, leaf_chance)
            tree.palette.leaves.place_block(interface, x1+1, y1+1, z1+1, leaf_chance)
            tree.palette.leaves.place_block(interface, x1-1, y1+1, z1-1, leaf_chance)
            tree.palette.leaves.place_block(interface, x1-1, y1+1, z1+1, leaf_chance)
            tree.palette.leaves.place_block(interface, x1+1, y1+1, z1-1, leaf_chance)
            tree.palette.leaves.place_block(interface, x1+1, y1+1, z1, leaf_chance)
            tree.palette.leaves.place_block(interface, x1-1, y1+1, z1, leaf_chance)
            tree.palette.leaves.place_block(interface, x1, y1+1, z1+1, leaf_chance)
            tree.palette.leaves.place_block(interface, x1, y1+1, z1-1, leaf_chance)
            tree.palette.leaves.place_block(interface, x1+2, y1+1, z1, leaf_chance)
            tree.palette.leaves.place_block(interface, x1-2, y1+1, z1, leaf_chance)
            tree.palette.leaves.place_block(interface, x1, y1+1, z1+2, leaf_chance)
            tree.palette.leaves.place_block(interface, x1, y1+1, z1-2, leaf_chance)
            tree.palette.leaves.place_block(interface, x1+2, y1+1, z1-1, leaf_chance)
            tree.palette.leaves.place_block(interface, x1-2, y1+1, z1-1, leaf_chance)
            tree.palette.leaves.place_block(interface, x1-1, y1+1, z1+2, leaf_chance)
            tree.palette.leaves.place_block(interface, x1-1, y1+1, z1-2, leaf_chance)
            tree.palette.leaves.place_block(interface, x1+2, y1+1, z1+1, leaf_chance)
            tree.palette.leaves.place_block(interface, x1-2, y1+1, z1+1, leaf_chance)
            tree.palette.leaves.place_block(interface, x1+1, y1+1, z1+2, leaf_chance)
            tree.palette.leaves.place_block(interface, x1+1, y1+1, z1-2, leaf_chance)
            
            tree.palette.leaves.place_block(interface, x1+1, y1, z1+1, leaf_chance)
            tree.palette.leaves.place_block(interface, x1-1, y1, z1-1, leaf_chance)
            tree.palette.leaves.place_block(interface, x1-1, y1, z1+1, leaf_chance)
            tree.palette.leaves.place_block(interface, x1+1, y1, z1-1, leaf_chance)
            tree.palette.leaves.place_block(interface, x1+1, y1, z1, leaf_chance)
            tree.palette.leaves.place_block(interface, x1-1, y1, z1, leaf_chance)
            tree.palette.leaves.place_block(interface, x1, y1, z1+1, leaf_chance)
            tree.palette.leaves.place_block(interface, x1, y1, z1-1, leaf_chance)
            tree.palette.leaves.place_block(interface, x1+2, y1, z1, leaf_chance)
            tree.palette.leaves.place_block(interface, x1-2, y1, z1, leaf_chance)
            tree.palette.leaves.place_block(interface, x1, y1, z1+2, leaf_chance)
            tree.palette.leaves.place_block(interface, x1, y1, z1-2, leaf_chance)

            tree.palette.leaves.place_block(interface, x1+1, y1-1, z1, leaf_chance)
            tree.palette.leaves.place_block(interface, x1-1, y1-1, z1, leaf_chance)
            tree.palette.leaves.place_block(interface, x1, y1-1, z1+1, leaf_chance)
            tree.palette.leaves.place_block(interface, x1, y1-1, z1-1, leaf_chance)
            tree.palette.leaves.place_block(interface, x1+1, y1-1, z1+1, leaf_chance)
            tree.palette.leaves.place_block(interface, x1-1, y1-1, z1-1, leaf_chance)
            tree.palette.leaves.place_block(interface, x1-1, y1-1, z1+1, leaf_chance)
            tree.palette.leaves.place_block(interface, x1+1, y1-1, z1-1, leaf_chance)
            tree.palette.leaves.place_block(interface, x1+1, y1-2, z1, leaf_chance)
            tree.palette.leaves.place_block(interface, x1-1, y1-2, z1, leaf_chance)
            tree.palette.leaves.place_block(interface, x1, y1-2, z1+1, leaf_chance)
            tree.palette.leaves.place_block(interface, x1, y1-2, z1-1, leaf_chance)
            
    def generate_mega_birch(self, tree, interface, leaf_chance: int=100):
        self.generate_large_birch(tree, interface, leaf_chance)
        x0, y0, z0 = tree.get_origin()
        new_tree = Tree((x0+1, y0, z0), tree.type)
        self.generate_large_birch(new_tree, interface, leaf_chance)
        new_tree = Tree((x0+1, y0, z0+1), tree.type)
        self.generate_large_birch(new_tree, interface, leaf_chance)
        new_tree = Tree((x0, y0, z0+1), tree.type)
        self.generate_large_birch(new_tree, interface, leaf_chance)

    def generate_small_hedge(self, tree, interface, leaf_chance: int=100):
        x0, y0, z0 = tree.get_origin()
        seed()
        height = randint(4,7)+y0

        for y in range (y0,height+2):
            if y == height+1:
                tree.palette.leaves.place_block(interface, x0, y, z0, leaf_chance)
                continue
            else:
                tree.palette.wood.place_block(interface, x0, y, z0)
            if y>y0:
                tree.palette.leaves.place_block(interface, x0+1, y, z0, leaf_chance)
                tree.palette.leaves.place_block(interface, x0-1, y, z0, leaf_chance)
                tree.palette.leaves.place_block(interface, x0, y, z0+1, leaf_chance)
                tree.palette.leaves.place_block(interface, x0, y, z0-1, leaf_chance)

    def generate_medium_hedge(self, tree, interface, leaf_chance: int=100):
        x0, y0, z0 = tree.get_origin()
        seed()
        height = randint(8,13)+y0

        for y in range (y0,height+2):
            if y == height+1:
                tree.palette.leaves.place_block(interface, x0, y, z0, leaf_chance)
                continue
            else:
                tree.palette.wood.place_block(interface, x0, y, z0)
            if y>y0:
                tree.palette.leaves.place_block(interface, x0+1, y, z0, leaf_chance)
                tree.palette.leaves.place_block(interface, x0-1, y, z0, leaf_chance)
                tree.palette.leaves.place_block(interface, x0, y, z0+1, leaf_chance)
                tree.palette.leaves.place_block(interface, x0, y, z0-1, leaf_chance)
            if y>y0+2 and y<height-1:
                tree.palette.leaves.place_block(interface, x0+1, y, z0+1, leaf_chance)
                tree.palette.leaves.place_block(interface, x0-1, y, z0-1, leaf_chance)
                tree.palette.leaves.place_block(interface, x0-1, y, z0+1, leaf_chance)
                tree.palette.leaves.place_block(interface, x0+1, y, z0-1, leaf_chance)

    def generate_large_hedge(self, tree, interface, leaf_chance: int=100):
        x0, y0, z0 = tree.get_origin()
        seed()
        height = randint(14,19)+y0

        for y in range (y0,height+2):
            if y == height+1:
                tree.palette.leaves.place_block(interface, x0, y, z0, leaf_chance)
                continue
            else:
                tree.palette.wood.place_block(interface, x0, y, z0)
            if y>y0:
                tree.palette.leaves.place_block(interface, x0+1, y, z0, leaf_chance)
                tree.palette.leaves.place_block(interface, x0-1, y, z0, leaf_chance)
                tree.palette.leaves.place_block(interface, x0, y, z0+1, leaf_chance)
                tree.palette.leaves.place_block(interface, x0, y, z0-1, leaf_chance)
            if y>y0+2 and y<height-1:
                tree.palette.leaves.place_block(interface, x0+1, y, z0+1, leaf_chance)
                tree.palette.leaves.place_block(interface, x0-1, y, z0-1, leaf_chance)
                tree.palette.leaves.place_block(interface, x0-1, y, z0+1, leaf_chance)
                tree.palette.leaves.place_block(interface, x0+1, y, z0-1, leaf_chance)
            if y>y0+3 and y<height-2:
                tree.palette.leaves.place_block(interface, x0+2, y, z0, leaf_chance)
                tree.palette.leaves.place_block(interface, x0-2, y, z0, leaf_chance)
                tree.palette.leaves.place_block(interface, x0, y, z0+2, leaf_chance)
                tree.palette.leaves.place_block(interface, x0, y, z0-2, leaf_chance)
            if y>y0+5 and y<height-4:
                tree.palette.leaves.place_block(interface, x0+2, y, z0+1, leaf_chance)
                tree.palette.leaves.place_block(interface, x0-2, y, z0+1, leaf_chance)
                tree.palette.leaves.place_block(interface, x0+1, y, z0+2, leaf_chance)
                tree.palette.leaves.place_block(interface, x0+1, y, z0-2, leaf_chance)
                tree.palette.leaves.place_block(interface, x0+2, y, z0-1, leaf_chance)
                tree.palette.leaves.place_block(interface, x0-2, y, z0-1, leaf_chance)
                tree.palette.leaves.place_block(interface, x0-1, y, z0+2, leaf_chance)
                tree.palette.leaves.place_block(interface, x0-1, y, z0-2, leaf_chance)

    def generate_mega_hedge(self, tree, interface, leaf_chance: int=100):
        self.generate_large_hedge(tree, interface, leaf_chance)
        x0, y0, z0 = tree.get_origin()
        new_tree = Tree((x0+1, y0, z0), tree.type)
        self.generate_large_hedge(new_tree, interface, leaf_chance)
        new_tree = Tree((x0+1, y0, z0+1), tree.type)
        self.generate_large_hedge(new_tree, interface, leaf_chance)
        new_tree = Tree((x0, y0, z0+1), tree.type)
        self.generate_large_hedge(new_tree, interface, leaf_chance)

    def generate_small_baobab(self, tree, interface, leaf_chance: int=100):
        x0, y0, z0 = tree.get_origin()
        seed()
        height = randint(12,19)+y0
        branches = []
        
        for y in range (y0,height+1): #tree stem
            tree.palette.wood.place_block(interface, x0, y, z0)
            tree.palette.wood.place_block(interface, x0+1, y, z0+1)
            tree.palette.wood.place_block(interface, x0+1, y, z0)
            tree.palette.wood.place_block(interface, x0, y, z0+1)

        main_branch_pos = randint(0,3)
        if main_branch_pos == 0: #main branch
            branches.append([x0, height+2, z0])
            tree.palette.wood.place_block(interface, x0, height+1, z0)
            tree.palette.wood.place_block(interface, x0, height+2, z0)
        elif main_branch_pos == 1:
            branches.append([x0, height+2, z0+1])
            tree.palette.wood.place_block(interface, x0, height+1, z0+1)
            tree.palette.wood.place_block(interface, x0, height+2, z0+1)
        elif main_branch_pos == 2:
            branches.append([x0+1, height+2, z0])
            tree.palette.wood.place_block(interface, x0+1, height+1, z0)
            tree.palette.wood.place_block(interface, x0+1, height+2, z0)
        else:
            branches.append([x0+1, height+2, z0+1])
            tree.palette.wood.place_block(interface, x0+1, height+1, z0+1)
            tree.palette.wood.place_block(interface, x0+1, height+2, z0+1)

        # random branch generation, 1 random branch for each quadrant
        branch_height = height
        branch_pos = randint(1, 5)
        if branch_pos == 1:
            branches.append([x0-2,branch_height+1,z0])
            tree.palette.wood.place_block(interface, x0-2, branch_height+1, z0)
            tree.palette.wood.place_block(interface, x0-1, branch_height, z0)
        elif branch_pos == 2:
            branches.append([x0-2,branch_height+1,z0-1])
            tree.palette.wood.place_block(interface, x0-2, branch_height+1, z0-1)
            b = randint(1,2)
            if b==1:
                tree.palette.wood.place_block(interface, x0-1,branch_height,z0-1)
            else:
                tree.palette.wood.place_block(interface, x0-1,branch_height,z0)
        elif branch_pos == 3:
            branches.append([x0-2,branch_height+1,z0-2])
            tree.palette.wood.place_block(interface, x0-2, branch_height+1, z0-2)
            tree.palette.wood.place_block(interface, x0-1,branch_height,z0-1)
        elif branch_pos == 4:
            branches.append([x0-1,branch_height+1,z0-2])
            tree.palette.wood.place_block(interface, x0-1, branch_height+1, z0-2)
            b = randint(1,2)
            if b==1:
                tree.palette.wood.place_block(interface, x0-1,branch_height,z0-1)
            else:
                tree.palette.wood.place_block(interface, x0,branch_height,z0-1)
        elif branch_pos == 5:
            branches.append([x0,branch_height+1,z0-2])
            tree.palette.wood.place_block(interface, x0, branch_height+1, z0-2)
            tree.palette.wood.place_block(interface, x0, branch_height, z0-1)

        branch_pos = randint(1, 5)
        if branch_pos == 1:
            branches.append([x0-2,branch_height+1,z0+1])
            tree.palette.wood.place_block(interface, x0-2,branch_height+1,z0+1)
            b = randint(1,2)
            if b==1:
                tree.palette.wood.place_block(interface, x0-1,branch_height,z0+1)
            else:
                tree.palette.wood.place_block(interface, x0-1,branch_height,z0)
        elif branch_pos == 2:
            branches.append([x0-2,branch_height+1,z0+2])
            tree.palette.wood.place_block(interface, x0-2,branch_height+1,z0+2)
            tree.palette.wood.place_block(interface, x0-1,branch_height,z0+1)
        elif branch_pos == 3:
            branches.append([x0-2,branch_height+1,z0+3])
            tree.palette.wood.place_block(interface, x0-2,branch_height+1,z0+3)
            tree.palette.wood.place_block(interface, x0-1,branch_height,z0+2)
        elif branch_pos == 4:
            branches.append([x0,branch_height+1,z0+3])
            tree.palette.wood.place_block(interface, x0, branch_height+1, z0+3)
            tree.palette.wood.place_block(interface, x0, branch_height, z0+2)
        elif branch_pos == 5:
            branches.append([x0-1,branch_height+1,z0+3])
            tree.palette.wood.place_block(interface, x0-1, branch_height+1, z0+3)
            b = randint(1,2)
            if b==1:
                tree.palette.wood.place_block(interface, x0-1,branch_height,z0+2)
            else:
                tree.palette.wood.place_block(interface, x0,branch_height,z0+2)

        branch_pos = randint(1, 5)
        if branch_pos == 1:
            branches.append([x0+1,branch_height+1,z0+3])
            tree.palette.wood.place_block(interface, x0+1, branch_height+1, z0+3)
            tree.palette.wood.place_block(interface, x0+1,branch_height,z0+2)
        elif branch_pos == 2:
            branches.append([x0+2,branch_height+1,z0+3])
            tree.palette.wood.place_block(interface, x0+2,branch_height+1,z0+3)
            b = randint(1,2)
            if b==1:
                tree.palette.wood.place_block(interface, x0+1,branch_height,z0+2)
            else:
                tree.palette.wood.place_block(interface, x0+2,branch_height,z0+2)
        elif branch_pos == 3:
            branches.append([x0+3,branch_height+1,z0+3])
            tree.palette.wood.place_block(interface, x0+3,branch_height+1,z0+3)
            tree.palette.wood.place_block(interface, x0+2,branch_height,z0+2)
        elif branch_pos == 4:
            branches.append([x0+3,branch_height+1,z0+2])
            tree.palette.wood.place_block(interface, x0+3,branch_height+1,z0+2)
            b = randint(1,2)
            if b==1:
                tree.palette.wood.place_block(interface, x0+2,branch_height,z0+1)
            else:
                tree.palette.wood.place_block(interface, x0+2,branch_height,z0+2)
        elif branch_pos == 5:
            branches.append([x0+3,branch_height+1,z0+1])
            tree.palette.wood.place_block(interface, x0+3,branch_height+1,z0+1)
            b = randint(1,2)
            if b==1:
                tree.palette.wood.place_block(interface, x0+2,branch_height,z0+1)
            else:
                tree.palette.wood.place_block(interface, x0+2,branch_height,z0+1)

        branch_pos = randint(1, 5)
        if branch_pos == 1:
            branches.append([x0+3,branch_height+1,z0])
            tree.palette.wood.place_block(interface, x0+3, branch_height+1, z0)
            tree.palette.wood.place_block(interface, x0+2, branch_height, z0)
        elif branch_pos == 2:
            branches.append([x0+3,branch_height+1,z0-1])
            tree.palette.wood.place_block(interface, x0+3, branch_height+1, z0-1)
            b = randint(1,2)
            if b==1:
                tree.palette.wood.place_block(interface, x0+2,branch_height,z0-1)
            else:
                tree.palette.wood.place_block(interface, x0+2,branch_height,z0)
        elif branch_pos == 3:
            branches.append([x0+3,branch_height+1,z0-2])
            tree.palette.wood.place_block(interface, x0+3, branch_height+1, z0-2)
            tree.palette.wood.place_block(interface, x0+2,branch_height,z0-1)
        elif branch_pos == 4:
            branches.append([x0+2,branch_height+1,z0-2])
            tree.palette.wood.place_block(interface, x0+2, branch_height+1, z0-2)
            b = randint(1,2)
            if b==1:
                tree.palette.wood.place_block(interface, x0+1,branch_height,z0-1)
            else:
                tree.palette.wood.place_block(interface, x0+2,branch_height,z0-1)
        elif branch_pos == 5:
            branches.append([x0+1,branch_height+1,z0-2])
            tree.palette.wood.place_block(interface, x0+1, branch_height+1, z0-2)
            tree.palette.wood.place_block(interface, x0+1,branch_height,z0-1)

        for branch in branches:
            x1, y1, z1 = branch[0], branch[1], branch[2]

            tree.palette.leaves.place_block(interface, x1, y1+1, z1, leaf_chance)
            tree.palette.leaves.place_block(interface, x1+1, y1+1, z1, leaf_chance)
            tree.palette.leaves.place_block(interface, x1-1, y1+1, z1, leaf_chance)
            tree.palette.leaves.place_block(interface, x1, y1+1, z1+1, leaf_chance)
            tree.palette.leaves.place_block(interface, x1, y1+1, z1-1, leaf_chance)

            tree.palette.leaves.place_block(interface, x1+1, y1, z1+1, leaf_chance)
            tree.palette.leaves.place_block(interface, x1-1, y1, z1-1, leaf_chance)
            tree.palette.leaves.place_block(interface, x1-1, y1, z1+1, leaf_chance)
            tree.palette.leaves.place_block(interface, x1+1, y1, z1-1, leaf_chance)
            tree.palette.leaves.place_block(interface, x1+1, y1, z1, leaf_chance)
            tree.palette.leaves.place_block(interface, x1-1, y1, z1, leaf_chance)
            tree.palette.leaves.place_block(interface, x1, y1, z1+1, leaf_chance)
            tree.palette.leaves.place_block(interface, x1, y1, z1-1, leaf_chance)
            tree.palette.leaves.place_block(interface, x1+2, y1, z1, leaf_chance)
            tree.palette.leaves.place_block(interface, x1-2, y1, z1, leaf_chance)
            tree.palette.leaves.place_block(interface, x1, y1, z1+2, leaf_chance)
            tree.palette.leaves.place_block(interface, x1, y1, z1-2, leaf_chance)

    def generate_medium_baobab(self, tree, interface, leaf_chance: int=100):
        x0, y0, z0 = tree.get_origin()
        seed()
        height = randint(18,25)+y0
        branches = []
        
        for y in range (y0,height+1): #tree stem
            tree.palette.wood.place_block(interface, x0, y, z0)
            tree.palette.wood.place_block(interface, x0+1, y, z0+1)
            tree.palette.wood.place_block(interface, x0+1, y, z0)
            tree.palette.wood.place_block(interface, x0, y, z0+1)
            tree.palette.wood.place_block(interface, x0-1, y, z0)
            tree.palette.wood.place_block(interface, x0+1, y, z0+2)
            tree.palette.wood.place_block(interface, x0+2, y, z0)
            tree.palette.wood.place_block(interface, x0, y, z0+2)
            tree.palette.wood.place_block(interface, x0, y, z0-1)
            tree.palette.wood.place_block(interface, x0+2, y, z0+1)
            tree.palette.wood.place_block(interface, x0+1, y, z0-1)
            tree.palette.wood.place_block(interface, x0-1, y, z0+1)

        #main branch/top
        tree.palette.wood.place_block(interface, x0, height+1, z0)
        tree.palette.wood.place_block(interface, x0+1, height+1, z0)
        tree.palette.wood.place_block(interface, x0+1, height+1, z0+1)
        tree.palette.wood.place_block(interface, x0, height+1, z0+1)
        tree.palette.wood.place_block(interface, x0, height+2, z0)
        tree.palette.wood.place_block(interface, x0+1, height+2, z0)
        tree.palette.wood.place_block(interface, x0+1, height+2, z0+1)
        tree.palette.wood.place_block(interface, x0, height+2, z0+1)
        tree.palette.wood.place_block(interface, x0, height+3, z0)
        tree.palette.wood.place_block(interface, x0+1, height+3, z0)
        tree.palette.wood.place_block(interface, x0+1, height+3, z0+1)
        tree.palette.wood.place_block(interface, x0, height+3, z0+1)

        #main branch leaves
        tree.palette.leaves.place_block(interface, x0, height+4, z0)
        tree.palette.leaves.place_block(interface, x0+1, height+4, z0+1)
        tree.palette.leaves.place_block(interface, x0+1, height+4, z0)
        tree.palette.leaves.place_block(interface, x0, height+4, z0+1)
        tree.palette.leaves.place_block(interface, x0-1, height+4, z0)
        tree.palette.leaves.place_block(interface, x0+1, height+4, z0+2)
        tree.palette.leaves.place_block(interface, x0+2, height+4, z0)
        tree.palette.leaves.place_block(interface, x0, height+4, z0+2)
        tree.palette.leaves.place_block(interface, x0, height+4, z0-1)
        tree.palette.leaves.place_block(interface, x0+2, height+4, z0+1)
        tree.palette.leaves.place_block(interface, x0+1, height+4, z0-1)
        tree.palette.leaves.place_block(interface, x0-1, height+4, z0+1)

        tree.palette.leaves.place_block(interface, x0-1, height+3, z0)
        tree.palette.leaves.place_block(interface, x0+1, height+3, z0+2)
        tree.palette.leaves.place_block(interface, x0+2, height+3, z0)
        tree.palette.leaves.place_block(interface, x0, height+3, z0+2)
        tree.palette.leaves.place_block(interface, x0, height+3, z0-1)
        tree.palette.leaves.place_block(interface, x0+2, height+3, z0+1)
        tree.palette.leaves.place_block(interface, x0+1, height+3, z0-1)
        tree.palette.leaves.place_block(interface, x0-1, height+3, z0+1)
        tree.palette.leaves.place_block(interface, x0-1, height+3, z0-2)
        tree.palette.leaves.place_block(interface, x0, height+3, z0-2)
        tree.palette.leaves.place_block(interface, x0+1, height+3, z0-2)
        tree.palette.leaves.place_block(interface, x0+2, height+3, z0-2)
        tree.palette.leaves.place_block(interface, x0-2, height+3, z0-1)
        tree.palette.leaves.place_block(interface, x0-2, height+3, z0)
        tree.palette.leaves.place_block(interface, x0-2, height+3, z0+1)
        tree.palette.leaves.place_block(interface, x0-2, height+3, z0+2)
        tree.palette.leaves.place_block(interface, x0-1, height+3, z0+3)
        tree.palette.leaves.place_block(interface, x0, height+3, z0+3)
        tree.palette.leaves.place_block(interface, x0+2, height+3, z0+3)
        tree.palette.leaves.place_block(interface, x0+1, height+3, z0+3)
        tree.palette.leaves.place_block(interface, x0+3, height+3, z0-1)
        tree.palette.leaves.place_block(interface, x0+3, height+3, z0)
        tree.palette.leaves.place_block(interface, x0+3, height+3, z0+1)
        tree.palette.leaves.place_block(interface, x0+3, height+3, z0+2)
        tree.palette.leaves.place_block(interface, x0-1, height+3, z0+2)
        tree.palette.leaves.place_block(interface, x0-1, height+3, z0-1)
        tree.palette.leaves.place_block(interface, x0+2, height+3, z0-1)
        tree.palette.leaves.place_block(interface, x0+2, height+3, z0+2)

        # random branch generation, 1 random branch for each quadrant
        branch_height = randint(height, height+1)
        branch_pos = randint(1, 5)
        if branch_pos == 1:
            branches.append([x0-3,branch_height+1,z0-3])
            tree.palette.wood.place_block(interface, x0-3, branch_height+1, z0-3)
            tree.palette.wood.place_block(interface, x0-2, branch_height, z0-2)
            tree.palette.wood.place_block(interface, x0-1, branch_height, z0-1)
        elif branch_pos == 2:
            branches.append([x0-4,branch_height+1,z0-3])
            tree.palette.wood.place_block(interface, x0-4, branch_height+1, z0-3)
            tree.palette.wood.place_block(interface, x0-3, branch_height, z0-2)
            tree.palette.wood.place_block(interface, x0-2, branch_height, z0-1)
        elif branch_pos == 3:
            branches.append([x0-4,branch_height+1,z0-2])
            tree.palette.wood.place_block(interface, x0-4, branch_height+1, z0-2)
            tree.palette.wood.place_block(interface, x0-3, branch_height, z0-2)
            tree.palette.wood.place_block(interface, x0-2, branch_height, z0-1)
        elif branch_pos == 4:
            branches.append([x0-3,branch_height+1,z0-4])
            tree.palette.wood.place_block(interface, x0-3, branch_height+1, z0-4)
            tree.palette.wood.place_block(interface, x0-2, branch_height, z0-3)
            tree.palette.wood.place_block(interface, x0-1, branch_height, z0-2)
        elif branch_pos == 5:
            branches.append([x0-2,branch_height+1,z0-4])
            tree.palette.wood.place_block(interface, x0-2, branch_height+1, z0-4)
            tree.palette.wood.place_block(interface, x0-2, branch_height, z0-3)
            tree.palette.wood.place_block(interface, x0-1, branch_height, z0-2)
        branch_height = randint(height, height+1)
        branch_pos = randint(1, 5)
        if branch_pos == 1:
            branches.append([x0-3,branch_height+1,z0+4])
            tree.palette.wood.place_block(interface, x0-3, branch_height+1, z0+4)
            tree.palette.wood.place_block(interface, x0-2, branch_height, z0+3)
            tree.palette.wood.place_block(interface, x0-1, branch_height, z0+2)
        elif branch_pos == 2:
            branches.append([x0-4,branch_height+1,z0+4])
            tree.palette.wood.place_block(interface, x0-4, branch_height+1, z0+4)
            tree.palette.wood.place_block(interface, x0-3, branch_height, z0+3)
            tree.palette.wood.place_block(interface, x0-2, branch_height, z0+2)
        elif branch_pos == 3:
            branches.append([x0-4,branch_height+1,z0+3])
            tree.palette.wood.place_block(interface, x0-4, branch_height+1, z0+3)
            tree.palette.wood.place_block(interface, x0-3, branch_height, z0+3)
            tree.palette.wood.place_block(interface, x0-2, branch_height, z0+2)
        elif branch_pos == 4:
            branches.append([x0-3,branch_height+1,z0+5])
            tree.palette.wood.place_block(interface, x0-3, branch_height+1, z0+5)
            tree.palette.wood.place_block(interface, x0-2, branch_height, z0+4)
            tree.palette.wood.place_block(interface, x0-1, branch_height, z0+3)
        elif branch_pos == 5:
            branches.append([x0-2,branch_height+1,z0+5])
            tree.palette.wood.place_block(interface, x0-2, branch_height+1, z0+5)
            tree.palette.wood.place_block(interface, x0-2, branch_height, z0+4)
            tree.palette.wood.place_block(interface, x0-1, branch_height, z0+3)
        branch_height = randint(height, height+1)
        branch_pos = randint(1, 5)
        if branch_pos == 1:
            branches.append([x0+4,branch_height+1,z0-3])
            tree.palette.wood.place_block(interface, x0+4, branch_height+1, z0-3)
            tree.palette.wood.place_block(interface, x0+3, branch_height, z0-2)
            tree.palette.wood.place_block(interface, x0+2, branch_height, z0-1)
        elif branch_pos == 2:
            branches.append([x0+5,branch_height+1,z0-3])
            tree.palette.wood.place_block(interface, x0+5, branch_height+1, z0-3)
            tree.palette.wood.place_block(interface, x0+4, branch_height, z0-2)
            tree.palette.wood.place_block(interface, x0+3, branch_height, z0-1)
        elif branch_pos == 3:
            branches.append([x0+5,branch_height+1,z0-2])
            tree.palette.wood.place_block(interface, x0+5, branch_height+1, z0-2)
            tree.palette.wood.place_block(interface, x0+4, branch_height, z0-2)
            tree.palette.wood.place_block(interface, x0+3, branch_height, z0-1)
        elif branch_pos == 4:
            branches.append([x0+4,branch_height+1,z0-4])
            tree.palette.wood.place_block(interface, x0+4, branch_height+1, z0-4)
            tree.palette.wood.place_block(interface, x0+3, branch_height, z0-3)
            tree.palette.wood.place_block(interface, x0+2, branch_height, z0-2)
        elif branch_pos == 5:
            branches.append([x0+3,branch_height+1,z0-4])
            tree.palette.wood.place_block(interface, x0+3, branch_height+1, z0-4)
            tree.palette.wood.place_block(interface, x0+3, branch_height, z0-3)
            tree.palette.wood.place_block(interface, x0+2, branch_height, z0-2)
        branch_height = randint(height, height+1)
        branch_pos = randint(1, 5)
        if branch_pos == 1:
            branches.append([x0+4,branch_height+1,z0+4])
            tree.palette.wood.place_block(interface, x0+4, branch_height+1, z0+4)
            tree.palette.wood.place_block(interface, x0+3, branch_height, z0+3)
            tree.palette.wood.place_block(interface, x0+2, branch_height, z0+2)
        elif branch_pos == 2:
            branches.append([x0+5,branch_height+1,z0+4])
            tree.palette.wood.place_block(interface, x0+5, branch_height+1, z0+4)
            tree.palette.wood.place_block(interface, x0+4, branch_height, z0+3)
            tree.palette.wood.place_block(interface, x0+3, branch_height, z0+2)
        elif branch_pos == 3:
            branches.append([x0+5,branch_height+1,z0+3])
            tree.palette.wood.place_block(interface, x0+5, branch_height+1, z0+3)
            tree.palette.wood.place_block(interface, x0+4, branch_height, z0+3)
            tree.palette.wood.place_block(interface, x0+3, branch_height, z0+2)
        elif branch_pos == 4:
            branches.append([x0+4,branch_height+1,z0+5])
            tree.palette.wood.place_block(interface, x0+4, branch_height+1, z0+5)
            tree.palette.wood.place_block(interface, x0+3, branch_height, z0+4)
            tree.palette.wood.place_block(interface, x0+2, branch_height, z0+3)
        elif branch_pos == 5:
            branches.append([x0+3,branch_height+1,z0+5])
            tree.palette.wood.place_block(interface, x0+3, branch_height+1, z0+5)
            tree.palette.wood.place_block(interface, x0+3, branch_height, z0+4)
            tree.palette.wood.place_block(interface, x0+2, branch_height, z0+3)
        branch_height = randint(height, height+1)
        branch_pos = randint(1, 4)
        if branch_pos == 1:
            branches.append([x0-1,branch_height+1,z0-4])
            tree.palette.wood.place_block(interface, x0-1, branch_height+1, z0-4)
            tree.palette.wood.place_block(interface, x0, branch_height, z0-3)
            tree.palette.wood.place_block(interface, x0, branch_height, z0-2)
        elif branch_pos == 2:
            branches.append([x0,branch_height+1,z0-4])
            tree.palette.wood.place_block(interface, x0, branch_height+1, z0-4)
            tree.palette.wood.place_block(interface, x0, branch_height, z0-3)
            tree.palette.wood.place_block(interface, x0, branch_height, z0-2)
        elif branch_pos == 3:
            branches.append([x0+1,branch_height+1,z0-4])
            tree.palette.wood.place_block(interface, x0+1, branch_height+1, z0-4)
            tree.palette.wood.place_block(interface, x0+1, branch_height, z0-3)
            tree.palette.wood.place_block(interface, x0+1, branch_height, z0-2)
        elif branch_pos == 4:
            branches.append([x0+2,branch_height+1,z0-4])
            tree.palette.wood.place_block(interface, x0+2, branch_height+1, z0-4)
            tree.palette.wood.place_block(interface, x0+1, branch_height, z0-3)
            tree.palette.wood.place_block(interface, x0+1, branch_height, z0-2)
        branch_height = randint(height, height+1)
        branch_pos = randint(1, 4)
        if branch_pos == 1:
            branches.append([x0-1,branch_height+1,z0+5])
            tree.palette.wood.place_block(interface, x0-1, branch_height+1, z0+5)
            tree.palette.wood.place_block(interface, x0, branch_height, z0+4)
            tree.palette.wood.place_block(interface, x0, branch_height, z0+3)
        elif branch_pos == 2:
            branches.append([x0,branch_height+1,z0+5])
            tree.palette.wood.place_block(interface, x0, branch_height+1, z0+5)
            tree.palette.wood.place_block(interface, x0, branch_height, z0+4)
            tree.palette.wood.place_block(interface, x0, branch_height, z0+3)
        elif branch_pos == 3:
            branches.append([x0+1,branch_height+1,z0+5])
            tree.palette.wood.place_block(interface, x0+1, branch_height+1, z0+5)
            tree.palette.wood.place_block(interface, x0+1, branch_height, z0+4)
            tree.palette.wood.place_block(interface, x0+1, branch_height, z0+3)
        elif branch_pos == 4:
            branches.append([x0+2,branch_height+1,z0+5])
            tree.palette.wood.place_block(interface, x0+2, branch_height+1, z0+5)
            tree.palette.wood.place_block(interface, x0+1, branch_height, z0+4)
            tree.palette.wood.place_block(interface, x0+1, branch_height, z0+3)
        branch_height = randint(height, height+1)
        branch_pos = randint(1, 4)
        if branch_pos == 1:
            branches.append([x0-4,branch_height+1,z0-1])
            tree.palette.wood.place_block(interface, x0-4, branch_height+1, z0-1)
            tree.palette.wood.place_block(interface, x0-3, branch_height, z0)
            tree.palette.wood.place_block(interface, x0-2, branch_height, z0)
        elif branch_pos == 2:
            branches.append([x0-4,branch_height+1,z0])
            tree.palette.wood.place_block(interface, x0-4, branch_height+1, z0)
            tree.palette.wood.place_block(interface, x0-3, branch_height, z0)
            tree.palette.wood.place_block(interface, x0-2, branch_height, z0)
        elif branch_pos == 3:
            branches.append([x0-4,branch_height+1,z0+1])
            tree.palette.wood.place_block(interface, x0-4, branch_height+1, z0+1)
            tree.palette.wood.place_block(interface, x0-3, branch_height, z0+1)
            tree.palette.wood.place_block(interface, x0-2, branch_height, z0+1)
        elif branch_pos == 4:
            branches.append([x0-4,branch_height+1,z0+2])
            tree.palette.wood.place_block(interface, x0-4, branch_height+1, z0+2)
            tree.palette.wood.place_block(interface, x0-3, branch_height, z0+1)
            tree.palette.wood.place_block(interface, x0-2, branch_height, z0+1)
        branch_height = randint(height, height+1)
        branch_pos = randint(1, 4)
        if branch_pos == 1:
            branches.append([x0+5,branch_height+1,z0-1])
            tree.palette.wood.place_block(interface, x0+5, branch_height+1, z0-1)
            tree.palette.wood.place_block(interface, x0+4, branch_height, z0)
            tree.palette.wood.place_block(interface, x0+3, branch_height, z0)
        elif branch_pos == 2:
            branches.append([x0+5,branch_height+1,z0])
            tree.palette.wood.place_block(interface, x0+5, branch_height+1, z0)
            tree.palette.wood.place_block(interface, x0+4, branch_height, z0)
            tree.palette.wood.place_block(interface, x0+3, branch_height, z0)
        elif branch_pos == 3:
            branches.append([x0+5,branch_height+1,z0+1])
            tree.palette.wood.place_block(interface, x0+5, branch_height+1, z0+1)
            tree.palette.wood.place_block(interface, x0+4, branch_height, z0+1)
            tree.palette.wood.place_block(interface, x0+3, branch_height, z0+1)
        elif branch_pos == 4:
            branches.append([x0+5,branch_height+1,z0+2])
            tree.palette.wood.place_block(interface, x0+5, branch_height+1, z0+2)
            tree.palette.wood.place_block(interface, x0+4, branch_height, z0+1)
            tree.palette.wood.place_block(interface, x0+3, branch_height, z0+1)

        for branch in branches:
            x1, y1, z1 = branch[0], branch[1], branch[2]

            tree.palette.leaves.place_block(interface, x1, y1+1, z1, leaf_chance)
            tree.palette.leaves.place_block(interface, x1+1, y1+1, z1, leaf_chance)
            tree.palette.leaves.place_block(interface, x1-1, y1+1, z1, leaf_chance)
            tree.palette.leaves.place_block(interface, x1, y1+1, z1+1, leaf_chance)
            tree.palette.leaves.place_block(interface, x1, y1+1, z1-1, leaf_chance)

            tree.palette.leaves.place_block(interface, x1+1, y1, z1+1, leaf_chance)
            tree.palette.leaves.place_block(interface, x1-1, y1, z1-1, leaf_chance)
            tree.palette.leaves.place_block(interface, x1-1, y1, z1+1, leaf_chance)
            tree.palette.leaves.place_block(interface, x1+1, y1, z1-1, leaf_chance)
            tree.palette.leaves.place_block(interface, x1+1, y1, z1, leaf_chance)
            tree.palette.leaves.place_block(interface, x1-1, y1, z1, leaf_chance)
            tree.palette.leaves.place_block(interface, x1, y1, z1+1, leaf_chance)
            tree.palette.leaves.place_block(interface, x1, y1, z1-1, leaf_chance)
            tree.palette.leaves.place_block(interface, x1+2, y1, z1, leaf_chance)
            tree.palette.leaves.place_block(interface, x1-2, y1, z1, leaf_chance)
            tree.palette.leaves.place_block(interface, x1, y1, z1+2, leaf_chance)
            tree.palette.leaves.place_block(interface, x1, y1, z1-2, leaf_chance)
            tree.palette.leaves.place_block(interface, x1+2, y1, z1+1, leaf_chance)
            tree.palette.leaves.place_block(interface, x1-2, y1, z1+1, leaf_chance)
            tree.palette.leaves.place_block(interface, x1+1, y1, z1+2, leaf_chance)
            tree.palette.leaves.place_block(interface, x1+1, y1, z1-2, leaf_chance)
            tree.palette.leaves.place_block(interface, x1+2, y1, z1-1, leaf_chance)
            tree.palette.leaves.place_block(interface, x1-2, y1, z1-1, leaf_chance)
            tree.palette.leaves.place_block(interface, x1-1, y1, z1+2, leaf_chance)
            tree.palette.leaves.place_block(interface, x1-1, y1, z1-2, leaf_chance)

    def generate_large_baobab(self, tree, interface, leaf_chance: int=100):
        x0, y0, z0 = tree.get_origin()
        seed()
        height = randint(26,40)+y0
        branches = []
        
        for y in range (y0,height+1): #tree stem
            tree.palette.wood.place_block(interface, x0, y, z0)
            tree.palette.wood.place_block(interface, x0+1, y, z0+1)
            tree.palette.wood.place_block(interface, x0+1, y, z0)
            tree.palette.wood.place_block(interface, x0, y, z0+1)
            tree.palette.wood.place_block(interface, x0-1, y, z0)
            tree.palette.wood.place_block(interface, x0+1, y, z0+2)
            tree.palette.wood.place_block(interface, x0+2, y, z0)
            tree.palette.wood.place_block(interface, x0, y, z0+2)
            tree.palette.wood.place_block(interface, x0, y, z0-1)
            tree.palette.wood.place_block(interface, x0+2, y, z0+1)
            tree.palette.wood.place_block(interface, x0+1, y, z0-1)
            tree.palette.wood.place_block(interface, x0-1, y, z0+1)
            tree.palette.wood.place_block(interface, x0+2, y, z0-1)
            tree.palette.wood.place_block(interface, x0-1, y, z0-2)
            tree.palette.wood.place_block(interface, x0, y, z0-2)
            tree.palette.wood.place_block(interface, x0+1, y, z0-2)
            tree.palette.wood.place_block(interface, x0-1, y, z0-1)
            tree.palette.wood.place_block(interface, x0-2, y, z0-1)
            tree.palette.wood.place_block(interface, x0-2, y, z0)
            tree.palette.wood.place_block(interface, x0-2, y, z0+1)
            tree.palette.wood.place_block(interface, x0-1, y, z0+2)

        #main branch/top
        tree.palette.wood.place_block(interface, x0, height+1, z0)
        tree.palette.wood.place_block(interface, x0+1, height+1, z0)
        tree.palette.wood.place_block(interface, x0+1, height+1, z0+1)
        tree.palette.wood.place_block(interface, x0, height+1, z0+1)
        tree.palette.wood.place_block(interface, x0, height+1, z0-1)
        tree.palette.wood.place_block(interface, x0-1, height+1, z0)
        tree.palette.wood.place_block(interface, x0-1, height+1, z0+1)
        tree.palette.wood.place_block(interface, x0+1, height+1, z0-1)
        tree.palette.wood.place_block(interface, x0-1, height+1, z0-1)
        tree.palette.wood.place_block(interface, x0, height+2, z0)
        tree.palette.wood.place_block(interface, x0+1, height+2, z0)
        tree.palette.wood.place_block(interface, x0+1, height+2, z0+1)
        tree.palette.wood.place_block(interface, x0, height+2, z0+1)
        tree.palette.wood.place_block(interface, x0, height+2, z0-1)
        tree.palette.wood.place_block(interface, x0-1, height+2, z0)
        tree.palette.wood.place_block(interface, x0-1, height+2, z0+1)
        tree.palette.wood.place_block(interface, x0+1, height+2, z0-1)
        tree.palette.wood.place_block(interface, x0-1, height+2, z0-1)
        tree.palette.wood.place_block(interface, x0, height+3, z0)
        tree.palette.wood.place_block(interface, x0+1, height+3, z0)
        tree.palette.wood.place_block(interface, x0+1, height+3, z0+1)
        tree.palette.wood.place_block(interface, x0, height+3, z0+1)
        tree.palette.wood.place_block(interface, x0, height+3, z0-1)
        tree.palette.wood.place_block(interface, x0-1, height+3, z0)
        tree.palette.wood.place_block(interface, x0-1, height+3, z0+1)
        tree.palette.wood.place_block(interface, x0+1, height+3, z0-1)
        tree.palette.wood.place_block(interface, x0-1, height+3, z0-1)
        tree.palette.wood.place_block(interface, x0, height+4, z0)
        tree.palette.wood.place_block(interface, x0+1, height+4, z0)
        tree.palette.wood.place_block(interface, x0+1, height+4, z0+1)
        tree.palette.wood.place_block(interface, x0, height+4, z0+1)
        tree.palette.wood.place_block(interface, x0, height+4, z0-1)
        tree.palette.wood.place_block(interface, x0-1, height+4, z0)
        tree.palette.wood.place_block(interface, x0-1, height+4, z0+1)
        tree.palette.wood.place_block(interface, x0+1, height+4, z0-1)
        tree.palette.wood.place_block(interface, x0-1, height+4, z0-1)


        #main branch leaves
        tree.palette.leaves.place_block(interface, x0, height+6, z0)
        tree.palette.leaves.place_block(interface, x0, height+6, z0-1)
        tree.palette.leaves.place_block(interface, x0-1, height+6, z0)
        tree.palette.leaves.place_block(interface, x0, height+6, z0+1)
        tree.palette.leaves.place_block(interface, x0+1, height+6, z0)

        tree.palette.leaves.place_block(interface, x0, height+5, z0)
        tree.palette.leaves.place_block(interface, x0, height+5, z0-1)
        tree.palette.leaves.place_block(interface, x0-1, height+5, z0)
        tree.palette.leaves.place_block(interface, x0, height+5, z0+1)
        tree.palette.leaves.place_block(interface, x0+1, height+5, z0)
        tree.palette.leaves.place_block(interface, x0, height+5, z0-2)
        tree.palette.leaves.place_block(interface, x0-2, height+5, z0)
        tree.palette.leaves.place_block(interface, x0, height+5, z0+2)
        tree.palette.leaves.place_block(interface, x0+2, height+5, z0)
        tree.palette.leaves.place_block(interface, x0-1, height+5, z0-1)
        tree.palette.leaves.place_block(interface, x0-1, height+5, z0+1)
        tree.palette.leaves.place_block(interface, x0+1, height+5, z0+1)
        tree.palette.leaves.place_block(interface, x0+1, height+5, z0-1)
        tree.palette.leaves.place_block(interface, x0+1, height+5, z0-2)
        tree.palette.leaves.place_block(interface, x0-2, height+5, z0+1)
        tree.palette.leaves.place_block(interface, x0+1, height+5, z0+2)
        tree.palette.leaves.place_block(interface, x0+2, height+5, z0+1)
        tree.palette.leaves.place_block(interface, x0-1, height+5, z0-2)
        tree.palette.leaves.place_block(interface, x0-2, height+5, z0-1)
        tree.palette.leaves.place_block(interface, x0-1, height+5, z0+2)
        tree.palette.leaves.place_block(interface, x0+2, height+5, z0-1)

        tree.palette.leaves.place_block(interface, x0, height+4, z0-2)
        tree.palette.leaves.place_block(interface, x0-2, height+4, z0)
        tree.palette.leaves.place_block(interface, x0, height+4, z0+2)
        tree.palette.leaves.place_block(interface, x0+2, height+4, z0)
        tree.palette.leaves.place_block(interface, x0+1, height+4, z0-2)
        tree.palette.leaves.place_block(interface, x0-2, height+4, z0+1)
        tree.palette.leaves.place_block(interface, x0+1, height+4, z0+2)
        tree.palette.leaves.place_block(interface, x0+2, height+4, z0+1)
        tree.palette.leaves.place_block(interface, x0-1, height+4, z0-2)
        tree.palette.leaves.place_block(interface, x0-2, height+4, z0-1)
        tree.palette.leaves.place_block(interface, x0-1, height+4, z0+2)
        tree.palette.leaves.place_block(interface, x0+2, height+4, z0-1)
        tree.palette.leaves.place_block(interface, x0, height+4, z0-3)
        tree.palette.leaves.place_block(interface, x0-3, height+4, z0)
        tree.palette.leaves.place_block(interface, x0, height+4, z0+3)
        tree.palette.leaves.place_block(interface, x0+3, height+4, z0)
        tree.palette.leaves.place_block(interface, x0+1, height+4, z0-3)
        tree.palette.leaves.place_block(interface, x0-3, height+4, z0+1)
        tree.palette.leaves.place_block(interface, x0+1, height+4, z0+3)
        tree.palette.leaves.place_block(interface, x0+3, height+4, z0+1)
        tree.palette.leaves.place_block(interface, x0-1, height+4, z0-3)
        tree.palette.leaves.place_block(interface, x0-3, height+4, z0-1)
        tree.palette.leaves.place_block(interface, x0-1, height+4, z0+3)
        tree.palette.leaves.place_block(interface, x0+3, height+4, z0-1)
        tree.palette.leaves.place_block(interface, x0, height+4, z0-4)
        tree.palette.leaves.place_block(interface, x0-4, height+4, z0)
        tree.palette.leaves.place_block(interface, x0, height+4, z0+4)
        tree.palette.leaves.place_block(interface, x0+4, height+4, z0)
        tree.palette.leaves.place_block(interface, x0+1, height+4, z0-4)
        tree.palette.leaves.place_block(interface, x0-4, height+4, z0+1)
        tree.palette.leaves.place_block(interface, x0+1, height+4, z0+4)
        tree.palette.leaves.place_block(interface, x0+4, height+4, z0+1)
        tree.palette.leaves.place_block(interface, x0-1, height+4, z0-4)
        tree.palette.leaves.place_block(interface, x0-4, height+4, z0-1)
        tree.palette.leaves.place_block(interface, x0-1, height+4, z0+4)
        tree.palette.leaves.place_block(interface, x0+4, height+4, z0-1)
        tree.palette.leaves.place_block(interface, x0-2, height+4, z0-2)
        tree.palette.leaves.place_block(interface, x0-2, height+4, z0+2)
        tree.palette.leaves.place_block(interface, x0+2, height+4, z0+2)
        tree.palette.leaves.place_block(interface, x0+2, height+4, z0-2)
        tree.palette.leaves.place_block(interface, x0-2, height+4, z0-3)
        tree.palette.leaves.place_block(interface, x0-2, height+4, z0+3)
        tree.palette.leaves.place_block(interface, x0+2, height+4, z0+3)
        tree.palette.leaves.place_block(interface, x0+2, height+4, z0-3)
        tree.palette.leaves.place_block(interface, x0-3, height+4, z0-2)
        tree.palette.leaves.place_block(interface, x0-3, height+4, z0+2)
        tree.palette.leaves.place_block(interface, x0+3, height+4, z0+2)
        tree.palette.leaves.place_block(interface, x0+3, height+4, z0-2)
        
        # random branch generation, 1 random branch for each quadrant
        branch_height = randint(height, height+2)
        branch_pos = randint(1, 5)
        if branch_pos == 1:
            branches.append([x0-4,branch_height+1,z0-4])
            tree.palette.wood.place_block(interface, x0-4, branch_height+1, z0-4)
            tree.palette.wood.place_block(interface, x0-3, branch_height, z0-3)
            tree.palette.wood.place_block(interface, x0-2, branch_height, z0-2)
        elif branch_pos == 2:
            branches.append([x0-4,branch_height+1,z0-3])
            tree.palette.wood.place_block(interface, x0-4, branch_height+1, z0-3)
            tree.palette.wood.place_block(interface, x0-3, branch_height, z0-2)
            tree.palette.wood.place_block(interface, x0-2, branch_height, z0-1)
        elif branch_pos == 3:
            branches.append([x0-5,branch_height+1,z0-3])
            tree.palette.wood.place_block(interface, x0-5, branch_height+1, z0-3)
            tree.palette.wood.place_block(interface, x0-4, branch_height, z0-2)
            tree.palette.wood.place_block(interface, x0-3, branch_height, z0-2)
            tree.palette.wood.place_block(interface, x0-2, branch_height, z0-1)
        elif branch_pos == 4:
            branches.append([x0-3,branch_height+1,z0-4])
            tree.palette.wood.place_block(interface, x0-3, branch_height+1, z0-4)
            tree.palette.wood.place_block(interface, x0-2, branch_height, z0-3)
            tree.palette.wood.place_block(interface, x0-1, branch_height, z0-2)
        elif branch_pos == 5:
            branches.append([x0-3,branch_height+1,z0-5])
            tree.palette.wood.place_block(interface, x0-3, branch_height+1, z0-5)
            tree.palette.wood.place_block(interface, x0-2, branch_height, z0-4)
            tree.palette.wood.place_block(interface, x0-2, branch_height, z0-3)
            tree.palette.wood.place_block(interface, x0-1, branch_height, z0-2)
        branch_height = randint(height, height+2)
        branch_pos = randint(1, 5)
        if branch_pos == 1:
            branches.append([x0+4,branch_height+1,z0-4])
            tree.palette.wood.place_block(interface, x0+4, branch_height+1, z0-4)
            tree.palette.wood.place_block(interface, x0+3, branch_height, z0-3)
            tree.palette.wood.place_block(interface, x0+2, branch_height, z0-2)
        elif branch_pos == 2:
            branches.append([x0+4,branch_height+1,z0-3])
            tree.palette.wood.place_block(interface, x0+4, branch_height+1, z0-3)
            tree.palette.wood.place_block(interface, x0+3, branch_height, z0-2)
            tree.palette.wood.place_block(interface, x0+2, branch_height, z0-1)
        elif branch_pos == 3:
            branches.append([x0+5,branch_height+1,z0-3])
            tree.palette.wood.place_block(interface, x0+5, branch_height+1, z0-3)
            tree.palette.wood.place_block(interface, x0+4, branch_height, z0-2)
            tree.palette.wood.place_block(interface, x0+3, branch_height, z0-2)
            tree.palette.wood.place_block(interface, x0+2, branch_height, z0-1)
        elif branch_pos == 4:
            branches.append([x0+3,branch_height+1,z0-4])
            tree.palette.wood.place_block(interface, x0+3, branch_height+1, z0-4)
            tree.palette.wood.place_block(interface, x0+2, branch_height, z0-3)
            tree.palette.wood.place_block(interface, x0+1, branch_height, z0-2)
        elif branch_pos == 5:
            branches.append([x0+3,branch_height+1,z0-5])
            tree.palette.wood.place_block(interface, x0+3, branch_height+1, z0-5)
            tree.palette.wood.place_block(interface, x0+2, branch_height, z0-4)
            tree.palette.wood.place_block(interface, x0+2, branch_height, z0-3)
            tree.palette.wood.place_block(interface, x0+1, branch_height, z0-2)
        branch_height = randint(height, height+2)
        branch_pos = randint(1, 5)
        if branch_pos == 1:
            branches.append([x0-4,branch_height+1,z0+4])
            tree.palette.wood.place_block(interface, x0-4, branch_height+1, z0+4)
            tree.palette.wood.place_block(interface, x0-3, branch_height, z0+3)
            tree.palette.wood.place_block(interface, x0-2, branch_height, z0+2)
        elif branch_pos == 2:
            branches.append([x0-4,branch_height+1,z0+3])
            tree.palette.wood.place_block(interface, x0-4, branch_height+1, z0+3)
            tree.palette.wood.place_block(interface, x0-3, branch_height, z0+2)
            tree.palette.wood.place_block(interface, x0-2, branch_height, z0+1)
        elif branch_pos == 3:
            branches.append([x0-5,branch_height+1,z0+3])
            tree.palette.wood.place_block(interface, x0-5, branch_height+1, z0+3)
            tree.palette.wood.place_block(interface, x0-4, branch_height, z0+2)
            tree.palette.wood.place_block(interface, x0-3, branch_height, z0+2)
            tree.palette.wood.place_block(interface, x0-2, branch_height, z0+1)
        elif branch_pos == 4:
            branches.append([x0-3,branch_height+1,z0+4])
            tree.palette.wood.place_block(interface, x0-3, branch_height+1, z0+4)
            tree.palette.wood.place_block(interface, x0-2, branch_height, z0+3)
            tree.palette.wood.place_block(interface, x0-1, branch_height, z0+2)
        elif branch_pos == 5:
            branches.append([x0-3,branch_height+1,z0+5])
            tree.palette.wood.place_block(interface, x0-3, branch_height+1, z0+5)
            tree.palette.wood.place_block(interface, x0-2, branch_height, z0+4)
            tree.palette.wood.place_block(interface, x0-2, branch_height, z0+3)
            tree.palette.wood.place_block(interface, x0-1, branch_height, z0+2)
        branch_height = randint(height, height+2)
        branch_pos = randint(1, 5)
        if branch_pos == 1:
            branches.append([x0+4,branch_height+1,z0+4])
            tree.palette.wood.place_block(interface, x0+4, branch_height+1, z0+4)
            tree.palette.wood.place_block(interface, x0+3, branch_height, z0+3)
            tree.palette.wood.place_block(interface, x0+2, branch_height, z0+2)
        elif branch_pos == 2:
            branches.append([x0+4,branch_height+1,z0+3])
            tree.palette.wood.place_block(interface, x0+4, branch_height+1, z0+3)
            tree.palette.wood.place_block(interface, x0+3, branch_height, z0+2)
            tree.palette.wood.place_block(interface, x0+2, branch_height, z0+1)
        elif branch_pos == 3:
            branches.append([x0+5,branch_height+1,z0+3])
            tree.palette.wood.place_block(interface, x0+5, branch_height+1, z0+3)
            tree.palette.wood.place_block(interface, x0+4, branch_height, z0+2)
            tree.palette.wood.place_block(interface, x0+3, branch_height, z0+2)
            tree.palette.wood.place_block(interface, x0+2, branch_height, z0+1)
        elif branch_pos == 4:
            branches.append([x0+3,branch_height+1,z0+4])
            tree.palette.wood.place_block(interface, x0+3, branch_height+1, z0+4)
            tree.palette.wood.place_block(interface, x0+2, branch_height, z0+3)
            tree.palette.wood.place_block(interface, x0+1, branch_height, z0+2)
        elif branch_pos == 5:
            branches.append([x0+3,branch_height+1,z0+5])
            tree.palette.wood.place_block(interface, x0+3, branch_height+1, z0+5)
            tree.palette.wood.place_block(interface, x0+2, branch_height, z0+4)
            tree.palette.wood.place_block(interface, x0+2, branch_height, z0+3)
            tree.palette.wood.place_block(interface, x0+1, branch_height, z0+2)

        branch_height = randint(height, height+2)
        branch_pos = randint(1, 5)
        if branch_pos == 1:
            branches.append([x0-1,branch_height+1,z0-5])
            tree.palette.wood.place_block(interface, x0-1, branch_height+1, z0-5)
            tree.palette.wood.place_block(interface, x0-1, branch_height, z0-4)
            tree.palette.wood.place_block(interface, x0, branch_height, z0-3)
            tree.palette.wood.place_block(interface, x0, branch_height, z0-2)
        elif branch_pos == 2:
            branches.append([x0,branch_height+1,z0-5])
            tree.palette.wood.place_block(interface, x0, branch_height+1, z0-5)
            tree.palette.wood.place_block(interface, x0, branch_height, z0-4)
            tree.palette.wood.place_block(interface, x0, branch_height, z0-3)
            tree.palette.wood.place_block(interface, x0, branch_height, z0-2)
        elif branch_pos == 3:
            branches.append([x0+1,branch_height+1,z0-5])
            tree.palette.wood.place_block(interface, x0+1, branch_height+1, z0-5)
            tree.palette.wood.place_block(interface, x0+1, branch_height, z0-4)
            tree.palette.wood.place_block(interface, x0+1, branch_height, z0-3)
            tree.palette.wood.place_block(interface, x0+1, branch_height, z0-2)
        elif branch_pos == 4:
            branches.append([x0+2,branch_height+1,z0-5])
            tree.palette.wood.place_block(interface, x0+2, branch_height+1, z0-5)
            tree.palette.wood.place_block(interface, x0+2, branch_height, z0-4)
            tree.palette.wood.place_block(interface, x0+1, branch_height, z0-3)
            tree.palette.wood.place_block(interface, x0+1, branch_height, z0-2)
        elif branch_pos == 5:
            branches.append([x0-2,branch_height+1,z0-5])
            tree.palette.wood.place_block(interface, x0-2, branch_height+1, z0-5)
            tree.palette.wood.place_block(interface, x0-2, branch_height, z0-4)
            tree.palette.wood.place_block(interface, x0-1, branch_height, z0-3)
            tree.palette.wood.place_block(interface, x0-1, branch_height, z0-2)
        branch_height = randint(height, height+2)
        branch_pos = randint(1, 5)
        if branch_pos == 1:
            branches.append([x0-1,branch_height+1,z0+5])
            tree.palette.wood.place_block(interface, x0-1, branch_height+1, z0+5)
            tree.palette.wood.place_block(interface, x0-1, branch_height, z0+4)
            tree.palette.wood.place_block(interface, x0, branch_height, z0+3)
            tree.palette.wood.place_block(interface, x0, branch_height, z0+2)
        elif branch_pos == 2:
            branches.append([x0,branch_height+1,z0+5])
            tree.palette.wood.place_block(interface, x0, branch_height+1, z0+5)
            tree.palette.wood.place_block(interface, x0, branch_height, z0+4)
            tree.palette.wood.place_block(interface, x0, branch_height, z0+3)
            tree.palette.wood.place_block(interface, x0, branch_height, z0+2)
        elif branch_pos == 3:
            branches.append([x0+1,branch_height+1,z0+5])
            tree.palette.wood.place_block(interface, x0+1, branch_height+1, z0+5)
            tree.palette.wood.place_block(interface, x0+1, branch_height, z0+4)
            tree.palette.wood.place_block(interface, x0+1, branch_height, z0+3)
            tree.palette.wood.place_block(interface, x0+1, branch_height, z0+2)
        elif branch_pos == 4:
            branches.append([x0+2,branch_height+1,z0+5])
            tree.palette.wood.place_block(interface, x0+2, branch_height+1, z0+5)
            tree.palette.wood.place_block(interface, x0+2, branch_height, z0+4)
            tree.palette.wood.place_block(interface, x0+1, branch_height, z0+3)
            tree.palette.wood.place_block(interface, x0+1, branch_height, z0+2)
        elif branch_pos == 5:
            branches.append([x0-2,branch_height+1,z0+5])
            tree.palette.wood.place_block(interface, x0-2, branch_height+1, z0+5)
            tree.palette.wood.place_block(interface, x0-2, branch_height, z0+4)
            tree.palette.wood.place_block(interface, x0-1, branch_height, z0+3)
            tree.palette.wood.place_block(interface, x0-1, branch_height, z0+2)
        branch_height = randint(height, height+2)
        branch_pos = randint(1, 5)
        if branch_pos == 1:
            branches.append([x0-5,branch_height+1,z0-1])
            tree.palette.wood.place_block(interface, x0-5, branch_height+1, z0-1)
            tree.palette.wood.place_block(interface, x0-4, branch_height, z0-1)
            tree.palette.wood.place_block(interface, x0-3, branch_height, z0)
            tree.palette.wood.place_block(interface, x0-2, branch_height, z0)
        elif branch_pos == 2:
            branches.append([x0-5,branch_height+1,z0])
            tree.palette.wood.place_block(interface, x0-5, branch_height+1, z0)
            tree.palette.wood.place_block(interface, x0-4, branch_height, z0)
            tree.palette.wood.place_block(interface, x0-3, branch_height, z0)
            tree.palette.wood.place_block(interface, x0-2, branch_height, z0)
        elif branch_pos == 3:
            branches.append([x0-5,branch_height+1,z0+1])
            tree.palette.wood.place_block(interface, x0-5, branch_height+1, z0+1)
            tree.palette.wood.place_block(interface, x0-4, branch_height, z0+1)
            tree.palette.wood.place_block(interface, x0-3, branch_height, z0+1)
            tree.palette.wood.place_block(interface, x0-2, branch_height, z0+1)
        elif branch_pos == 4:
            branches.append([x0-5,branch_height+1,z0+2])
            tree.palette.wood.place_block(interface, x0-5, branch_height+1, z0+2)
            tree.palette.wood.place_block(interface, x0-4, branch_height, z0+2)
            tree.palette.wood.place_block(interface, x0-3, branch_height, z0+1)
            tree.palette.wood.place_block(interface, x0-2, branch_height, z0+1)
        elif branch_pos == 5:
            branches.append([x0-5,branch_height+1,z0-2])
            tree.palette.wood.place_block(interface, x0-5, branch_height+1, z0-2)
            tree.palette.wood.place_block(interface, x0-4, branch_height, z0-2)
            tree.palette.wood.place_block(interface, x0-3, branch_height, z0-1)
            tree.palette.wood.place_block(interface, x0-2, branch_height, z0-1)
        branch_height = randint(height, height+2)
        branch_pos = randint(1, 5)
        if branch_pos == 1:
            branches.append([x0+5,branch_height+1,z0-1])
            tree.palette.wood.place_block(interface, x0+5, branch_height+1, z0-1)
            tree.palette.wood.place_block(interface, x0+4, branch_height, z0-1)
            tree.palette.wood.place_block(interface, x0+3, branch_height, z0)
            tree.palette.wood.place_block(interface, x0+2, branch_height, z0)
        elif branch_pos == 2:
            branches.append([x0+5,branch_height+1,z0])
            tree.palette.wood.place_block(interface, x0+5, branch_height+1, z0)
            tree.palette.wood.place_block(interface, x0+4, branch_height, z0)
            tree.palette.wood.place_block(interface, x0+3, branch_height, z0)
            tree.palette.wood.place_block(interface, x0+2, branch_height, z0)
        elif branch_pos == 3:
            branches.append([x0+5,branch_height+1,z0+1])
            tree.palette.wood.place_block(interface, x0+5, branch_height+1, z0+1)
            tree.palette.wood.place_block(interface, x0+4, branch_height, z0+1)
            tree.palette.wood.place_block(interface, x0+3, branch_height, z0+1)
            tree.palette.wood.place_block(interface, x0+2, branch_height, z0+1)
        elif branch_pos == 4:
            branches.append([x0+5,branch_height+1,z0+2])
            tree.palette.wood.place_block(interface, x0+5, branch_height+1, z0+2)
            tree.palette.wood.place_block(interface, x0+4, branch_height, z0+2)
            tree.palette.wood.place_block(interface, x0+3, branch_height, z0+1)
            tree.palette.wood.place_block(interface, x0+2, branch_height, z0+1)
        elif branch_pos == 5:
            branches.append([x0+5,branch_height+1,z0-2])
            tree.palette.wood.place_block(interface, x0+5, branch_height+1, z0-2)
            tree.palette.wood.place_block(interface, x0+4, branch_height, z0-2)
            tree.palette.wood.place_block(interface, x0+3, branch_height, z0-1)
            tree.palette.wood.place_block(interface, x0+2, branch_height, z0-1)

        for branch in branches:
            x1, y1, z1 = branch[0], branch[1], branch[2]

            tree.palette.leaves.place_block(interface, x1, y1+1, z1, leaf_chance)
            tree.palette.leaves.place_block(interface, x1+1, y1+1, z1, leaf_chance)
            tree.palette.leaves.place_block(interface, x1-1, y1+1, z1, leaf_chance)
            tree.palette.leaves.place_block(interface, x1, y1+1, z1+1, leaf_chance)
            tree.palette.leaves.place_block(interface, x1, y1+1, z1-1, leaf_chance)
            tree.palette.leaves.place_block(interface, x1+1, y1+1, z1+1, leaf_chance)
            tree.palette.leaves.place_block(interface, x1-1, y1+1, z1-1, leaf_chance)
            tree.palette.leaves.place_block(interface, x1-1, y1+1, z1+1, leaf_chance)
            tree.palette.leaves.place_block(interface, x1+1, y1+1, z1-1, leaf_chance)
            tree.palette.leaves.place_block(interface, x1+2, y1+1, z1, leaf_chance)
            tree.palette.leaves.place_block(interface, x1-2, y1+1, z1, leaf_chance)
            tree.palette.leaves.place_block(interface, x1, y1+1, z1+2, leaf_chance)
            tree.palette.leaves.place_block(interface, x1, y1+1, z1-2, leaf_chance)

            tree.palette.leaves.place_block(interface, x1+1, y1, z1+1, leaf_chance)
            tree.palette.leaves.place_block(interface, x1-1, y1, z1-1, leaf_chance)
            tree.palette.leaves.place_block(interface, x1-1, y1, z1+1, leaf_chance)
            tree.palette.leaves.place_block(interface, x1+1, y1, z1-1, leaf_chance)
            tree.palette.leaves.place_block(interface, x1+1, y1, z1, leaf_chance)
            tree.palette.leaves.place_block(interface, x1-1, y1, z1, leaf_chance)
            tree.palette.leaves.place_block(interface, x1, y1, z1+1, leaf_chance)
            tree.palette.leaves.place_block(interface, x1, y1, z1-1, leaf_chance)
            tree.palette.leaves.place_block(interface, x1+2, y1, z1, leaf_chance)
            tree.palette.leaves.place_block(interface, x1-2, y1, z1, leaf_chance)
            tree.palette.leaves.place_block(interface, x1, y1, z1+2, leaf_chance)
            tree.palette.leaves.place_block(interface, x1, y1, z1-2, leaf_chance)
            tree.palette.leaves.place_block(interface, x1+2, y1, z1+1, leaf_chance)
            tree.palette.leaves.place_block(interface, x1-2, y1, z1+1, leaf_chance)
            tree.palette.leaves.place_block(interface, x1+1, y1, z1+2, leaf_chance)
            tree.palette.leaves.place_block(interface, x1+1, y1, z1-2, leaf_chance)
            tree.palette.leaves.place_block(interface, x1+2, y1, z1-1, leaf_chance)
            tree.palette.leaves.place_block(interface, x1-2, y1, z1-1, leaf_chance)
            tree.palette.leaves.place_block(interface, x1-1, y1, z1+2, leaf_chance)
            tree.palette.leaves.place_block(interface, x1-1, y1, z1-2, leaf_chance)
            tree.palette.leaves.place_block(interface, x1+3, y1, z1, leaf_chance)
            tree.palette.leaves.place_block(interface, x1-3, y1, z1, leaf_chance)
            tree.palette.leaves.place_block(interface, x1, y1, z1+3, leaf_chance)
            tree.palette.leaves.place_block(interface, x1, y1, z1-3, leaf_chance)
            tree.palette.leaves.place_block(interface, x1+3, y1, z1+1, leaf_chance)
            tree.palette.leaves.place_block(interface, x1-3, y1, z1+1, leaf_chance)
            tree.palette.leaves.place_block(interface, x1+1, y1, z1+3, leaf_chance)
            tree.palette.leaves.place_block(interface, x1+1, y1, z1-3, leaf_chance)
            tree.palette.leaves.place_block(interface, x1+3, y1, z1-1, leaf_chance)
            tree.palette.leaves.place_block(interface, x1-3, y1, z1-1, leaf_chance)
            tree.palette.leaves.place_block(interface, x1-1, y1, z1+3, leaf_chance)
            tree.palette.leaves.place_block(interface, x1-1, y1, z1-3, leaf_chance)
            tree.palette.leaves.place_block(interface, x1+2, y1, z1+2, leaf_chance)
            tree.palette.leaves.place_block(interface, x1-2, y1, z1-2, leaf_chance)
            tree.palette.leaves.place_block(interface, x1-2, y1, z1+2, leaf_chance)
            tree.palette.leaves.place_block(interface, x1+2, y1, z1-2, leaf_chance)

    def generate_small_oak(self, tree, interface, leaf_chance: int=100):
        x0, y0, z0 = tree.get_origin()
        seed()
        stem_height = randint(4,7)
        for y in range (y0,stem_height+y0+2):
            if y == stem_height+y0+1:
                tree.palette.leaves.place_block(interface, x0, y, z0, leaf_chance)
                tree.palette.leaves.place_block(interface, x0+1, y, z0, leaf_chance)
                tree.palette.leaves.place_block(interface, x0-1, y, z0, leaf_chance)
                tree.palette.leaves.place_block(interface, x0, y, z0+1, leaf_chance)
                tree.palette.leaves.place_block(interface, x0, y, z0-1, leaf_chance)
                continue
            tree.palette.wood.place_block(interface, x0, y, z0)
            if y == int(stem_height/2 +y0)-1:
                tree.palette.leaves.place_block(interface, x0+1, y, z0, leaf_chance)
                tree.palette.leaves.place_block(interface, x0-1, y, z0, leaf_chance)
                tree.palette.leaves.place_block(interface, x0, y, z0+1, leaf_chance)
                tree.palette.leaves.place_block(interface, x0, y, z0-1, leaf_chance)
            elif y == stem_height+y0 or y == int(stem_height/2 +y0):
                tree.palette.leaves.place_block(interface, x0+2, y, z0, leaf_chance)
                tree.palette.leaves.place_block(interface, x0-2, y, z0, leaf_chance)
                tree.palette.leaves.place_block(interface, x0, y, z0+2, leaf_chance)
                tree.palette.leaves.place_block(interface, x0, y, z0-2, leaf_chance)
                tree.palette.leaves.place_block(interface, x0+1, y, z0+1, leaf_chance)
                tree.palette.leaves.place_block(interface, x0-1, y, z0-1, leaf_chance)
                tree.palette.leaves.place_block(interface, x0-1, y, z0+1, leaf_chance)
                tree.palette.leaves.place_block(interface, x0+1, y, z0-1, leaf_chance)
                tree.palette.leaves.place_block(interface, x0+1, y, z0, leaf_chance)
                tree.palette.leaves.place_block(interface, x0-1, y, z0, leaf_chance)
                tree.palette.leaves.place_block(interface, x0, y, z0+1, leaf_chance)
                tree.palette.leaves.place_block(interface, x0, y, z0-1, leaf_chance)
            elif y>int(stem_height/2 +y0) and y<stem_height+y0:
                tree.palette.leaves.place_block(interface, x0+2, y, z0, leaf_chance)
                tree.palette.leaves.place_block(interface, x0-2, y, z0, leaf_chance)
                tree.palette.leaves.place_block(interface, x0, y, z0+2, leaf_chance)
                tree.palette.leaves.place_block(interface, x0, y, z0-2, leaf_chance)
                tree.palette.leaves.place_block(interface, x0+2, y, z0+1, leaf_chance)
                tree.palette.leaves.place_block(interface, x0-2, y, z0+1, leaf_chance)
                tree.palette.leaves.place_block(interface, x0+1, y, z0+2, leaf_chance)
                tree.palette.leaves.place_block(interface, x0+1, y, z0-2, leaf_chance)
                tree.palette.leaves.place_block(interface, x0+2, y, z0-1, leaf_chance)
                tree.palette.leaves.place_block(interface, x0-2, y, z0-1, leaf_chance)
                tree.palette.leaves.place_block(interface, x0-1, y, z0+2, leaf_chance)
                tree.palette.leaves.place_block(interface, x0-1, y, z0-2, leaf_chance)
                tree.palette.leaves.place_block(interface, x0+1, y, z0+1, leaf_chance)
                tree.palette.leaves.place_block(interface, x0-1, y, z0-1, leaf_chance)
                tree.palette.leaves.place_block(interface, x0-1, y, z0+1, leaf_chance)
                tree.palette.leaves.place_block(interface, x0+1, y, z0-1, leaf_chance)
                tree.palette.leaves.place_block(interface, x0+1, y, z0, leaf_chance)
                tree.palette.leaves.place_block(interface, x0-1, y, z0, leaf_chance)
                tree.palette.leaves.place_block(interface, x0, y, z0+1, leaf_chance)
                tree.palette.leaves.place_block(interface, x0, y, z0-1, leaf_chance)

    def generate_medium_oak(self, tree, interface, leaf_chance: int=100):
        x0, y0, z0 = tree.get_origin()
        seed()
        height = randint(10,15)+y0
        branch_num = randint(3,7)
        branches = []
        branches.append([x0, height-1, z0])
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
            branch_height = randint(int((height-y0)/2+y0)+4, height-1)
            branch_pos = randint(1, 24)
            if branch_pos == 1:
                branches.append([x0+3,branch_height,z0])
                tree.palette.wood.place_block(interface, x0+3, branch_height, z0)
                tree.palette.wood.place_block(interface, x0+2, branch_height-1, z0)
                tree.palette.wood.place_block(interface, x0+1, branch_height-1, z0)
            elif branch_pos == 2:
                branches.append([x0+3,branch_height,z0+1])
                tree.palette.wood.place_block(interface, x0+3,branch_height,z0+1)
                b = randint(1,2)
                if b==1:
                    tree.palette.wood.place_block(interface, x0+2,branch_height-1,z0+1)
                else:
                    tree.palette.wood.place_block(interface, x0+2,branch_height-1,z0)
                tree.palette.wood.place_block(interface, x0+1,branch_height-1,z0)
            elif branch_pos == 3:
                branches.append([x0+3,branch_height,z0+2])
                tree.palette.wood.place_block(interface, x0+3,branch_height,z0+2)
                b = randint(1,2)
                if b==1:
                    tree.palette.wood.place_block(interface, x0+2,branch_height-1,z0+1)
                else:
                    tree.palette.wood.place_block(interface, x0+2,branch_height-1,z0+2)
                tree.palette.wood.place_block(interface, x0+1,branch_height-1,z0+1)
            elif branch_pos == 4:
                branches.append([x0+3,branch_height,z0+3])
                tree.palette.wood.place_block(interface, x0+3, branch_height, z0+3)
                tree.palette.wood.place_block(interface, x0+2, branch_height-1, z0+2)
                tree.palette.wood.place_block(interface, x0+1, branch_height-1, z0+1)  
            elif branch_pos == 5:
                branches.append([x0+2,branch_height,z0+3])
                tree.palette.wood.place_block(interface, x0+2,branch_height,z0+3)
                b = randint(1,2)
                if b==1:
                    tree.palette.wood.place_block(interface, x0+2,branch_height-1,z0+2)
                else:
                    tree.palette.wood.place_block(interface, x0+1,branch_height-1,z0+2)
                tree.palette.wood.place_block(interface, x0+1,branch_height-1,z0+1)
            elif branch_pos == 6:
                branches.append([x0+1,branch_height,z0+3])
                tree.palette.wood.place_block(interface, x0+1,branch_height,z0+3)
                b = randint(1,2)
                if b==1:
                    tree.palette.wood.place_block(interface, x0+1,branch_height-1,z0+2)
                else:
                    tree.palette.wood.place_block(interface, x0,branch_height-1,z0+2)
                tree.palette.wood.place_block(interface, x0,branch_height-1,z0+1)
            elif branch_pos == 7:
                branches.append([x0,branch_height,z0+3])
                tree.palette.wood.place_block(interface, x0, branch_height, z0+3)
                tree.palette.wood.place_block(interface, x0, branch_height-1, z0+2)
                tree.palette.wood.place_block(interface, x0, branch_height-1, z0+1)
            elif branch_pos == 8:
                branches.append([x0-1,branch_height,z0+3])
                tree.palette.wood.place_block(interface, x0-1,branch_height,z0+3)
                b = randint(1,2)
                if b==1:
                    tree.palette.wood.place_block(interface, x0-1,branch_height-1,z0+2)
                else:
                    tree.palette.wood.place_block(interface, x0,branch_height-1,z0+2)
                tree.palette.wood.place_block(interface, x0,branch_height-1,z0+1)
            elif branch_pos == 9:
                branches.append([x0-2,branch_height,z0+3])
                tree.palette.wood.place_block(interface, x0-2,branch_height,z0+3)
                b = randint(1,2)
                if b==1:
                    tree.palette.wood.place_block(interface, x0-2,branch_height-1,z0+2)
                else:
                    tree.palette.wood.place_block(interface, x0-1,branch_height-1,z0+2)
                tree.palette.wood.place_block(interface, x0-1,branch_height-1,z0+1)
            elif branch_pos == 10:
                branches.append([x0-3,branch_height,z0+3])
                tree.palette.wood.place_block(interface, x0-3, branch_height, z0+3)
                tree.palette.wood.place_block(interface, x0-2, branch_height-1, z0+2)
                tree.palette.wood.place_block(interface, x0-1, branch_height-1, z0+1) 
            elif branch_pos == 11:
                branches.append([x0-3,branch_height,z0+2])
                tree.palette.wood.place_block(interface, x0-3,branch_height,z0+2)
                b = randint(1,2)
                if b==1:
                    tree.palette.wood.place_block(interface, x0-2,branch_height-1,z0+1)
                else:
                    tree.palette.wood.place_block(interface, x0-2,branch_height-1,z0+2)
                tree.palette.wood.place_block(interface, x0-1,branch_height-1,z0+1)
            elif branch_pos == 12:
                branches.append([x0-3,branch_height,z0+1])
                tree.palette.wood.place_block(interface, x0-3,branch_height,z0+1)
                b = randint(1,2)
                if b==1:
                    tree.palette.wood.place_block(interface, x0-2,branch_height-1,z0+1)
                else:
                    tree.palette.wood.place_block(interface, x0-2,branch_height-1,z0)
                tree.palette.wood.place_block(interface, x0-1,branch_height-1,z0)
            elif branch_pos == 13:
                branches.append([x0-3,branch_height,z0])
                tree.palette.wood.place_block(interface, x0-3, branch_height, z0)
                tree.palette.wood.place_block(interface, x0-2, branch_height-1, z0)
                tree.palette.wood.place_block(interface, x0-1, branch_height-1, z0)
            elif branch_pos == 14:
                branches.append([x0-3,branch_height,z0-1])
                tree.palette.wood.place_block(interface, x0-3,branch_height,z0-1)
                b = randint(1,2)
                if b==1:
                    tree.palette.wood.place_block(interface, x0-2,branch_height-1,z0-1)
                else:
                    tree.palette.wood.place_block(interface, x0-2,branch_height-1,z0)
                tree.palette.wood.place_block(interface, x0-1,branch_height-1,z0)
            elif branch_pos == 15:
                branches.append([x0-3,branch_height,z0-2])
                tree.palette.wood.place_block(interface, x0-3,branch_height,z0-2)
                b = randint(1,2)
                if b==1:
                    tree.palette.wood.place_block(interface, x0-2,branch_height-1,z0-1)
                else:
                    tree.palette.wood.place_block(interface, x0-2,branch_height-1,z0-2)
                tree.palette.wood.place_block(interface, x0-1,branch_height-1,z0-1)
            elif branch_pos == 16:
                branches.append([x0-3,branch_height,z0-3])
                tree.palette.wood.place_block(interface, x0-3, branch_height, z0-3)
                tree.palette.wood.place_block(interface, x0-2, branch_height-1, z0-2)
                tree.palette.wood.place_block(interface, x0-1, branch_height-1, z0-1) 
            elif branch_pos == 17:
                branches.append([x0-2,branch_height,z0-3])
                tree.palette.wood.place_block(interface, x0-2,branch_height,z0-3)
                b = randint(1,2)
                if b==1:
                    tree.palette.wood.place_block(interface, x0-2,branch_height-1,z0-2)
                else:
                    tree.palette.wood.place_block(interface, x0-1,branch_height-1,z0-2)
                tree.palette.wood.place_block(interface, x0-1,branch_height-1,z0-1)
            elif branch_pos == 18:
                branches.append([x0-1,branch_height,z0-3])
                tree.palette.wood.place_block(interface, x0-1,branch_height,z0-3)
                b = randint(1,2)
                if b==1:
                    tree.palette.wood.place_block(interface, x0-1,branch_height-1,z0-2)
                else:
                    tree.palette.wood.place_block(interface, x0,branch_height-1,z0-2)
                tree.palette.wood.place_block(interface, x0,branch_height-1,z0-1)
            elif branch_pos == 19:
                branches.append([x0,branch_height,z0-3])
                tree.palette.wood.place_block(interface, x0, branch_height, z0-3)
                tree.palette.wood.place_block(interface, x0, branch_height-1, z0-2)
                tree.palette.wood.place_block(interface, x0, branch_height-1, z0-1)
            elif branch_pos == 20:
                branches.append([x0+1,branch_height,z0-3])
                tree.palette.wood.place_block(interface, x0+1,branch_height,z0-3)
                b = randint(1,2)
                if b==1:
                    tree.palette.wood.place_block(interface, x0+1,branch_height-1,z0-2)
                else:
                    tree.palette.wood.place_block(interface, x0,branch_height-1,z0-2)
                tree.palette.wood.place_block(interface, x0,branch_height-1,z0-1)
            elif branch_pos == 21:
                branches.append([x0+2,branch_height,z0-3])
                tree.palette.wood.place_block(interface, x0+2,branch_height,z0-3)
                b = randint(1,2)
                if b==1:
                    tree.palette.wood.place_block(interface, x0+2,branch_height-1,z0-2)
                else:
                    tree.palette.wood.place_block(interface, x0+1,branch_height-1,z0-2)
                tree.palette.wood.place_block(interface, x0+1,branch_height-1,z0-1)
            elif branch_pos == 22:
                branches.append([x0+3,branch_height,z0-3])
                tree.palette.wood.place_block(interface, x0+3, branch_height, z0-3)
                tree.palette.wood.place_block(interface, x0+2, branch_height-1, z0-2)
                tree.palette.wood.place_block(interface, x0+1, branch_height-1, z0-1)
            elif branch_pos == 23:
                branches.append([x0+3,branch_height,z0-2])
                tree.palette.wood.place_block(interface, x0+3,branch_height,z0-2)
                b = randint(1,2)
                if b==1:
                    tree.palette.wood.place_block(interface, x0+2,branch_height-1,z0-1)
                else:
                    tree.palette.wood.place_block(interface, x0+2,branch_height-1,z0-2)
                tree.palette.wood.place_block(interface, x0+1,branch_height-1,z0-1)
            elif branch_pos == 24:
                branches.append([x0+3,branch_height,z0-1])
                tree.palette.wood.place_block(interface, x0+3,branch_height,z0-1)
                b = randint(1,2)
                if b==1:
                    tree.palette.wood.place_block(interface, x0+2,branch_height-1,z0-1)
                else:
                    tree.palette.wood.place_block(interface, x0+2,branch_height-1,z0)
                tree.palette.wood.place_block(interface, x0+1,branch_height-1,z0)
            


        for branch in branches:
            x1, y1, z1 = branch[0], branch[1], branch[2]

            tree.palette.leaves.place_block(interface, x1+1, y1+2, z1, leaf_chance)
            tree.palette.leaves.place_block(interface, x1-1, y1+2, z1, leaf_chance)
            tree.palette.leaves.place_block(interface, x1, y1+2, z1+1, leaf_chance)
            tree.palette.leaves.place_block(interface, x1, y1+2, z1-1, leaf_chance)
            tree.palette.leaves.place_block(interface, x1, y1+2, z1, leaf_chance)

            tree.palette.leaves.place_block(interface, x1, y1+1, z1, leaf_chance)
            tree.palette.leaves.place_block(interface, x1+1, y1+1, z1+1, leaf_chance)
            tree.palette.leaves.place_block(interface, x1-1, y1+1, z1-1, leaf_chance)
            tree.palette.leaves.place_block(interface, x1-1, y1+1, z1+1, leaf_chance)
            tree.palette.leaves.place_block(interface, x1+1, y1+1, z1-1, leaf_chance)
            tree.palette.leaves.place_block(interface, x1+1, y1+1, z1, leaf_chance)
            tree.palette.leaves.place_block(interface, x1-1, y1+1, z1, leaf_chance)
            tree.palette.leaves.place_block(interface, x1, y1+1, z1+1, leaf_chance)
            tree.palette.leaves.place_block(interface, x1, y1+1, z1-1, leaf_chance)
            tree.palette.leaves.place_block(interface, x1+2, y1+1, z1, leaf_chance)
            tree.palette.leaves.place_block(interface, x1-2, y1+1, z1, leaf_chance)
            tree.palette.leaves.place_block(interface, x1, y1+1, z1+2, leaf_chance)
            tree.palette.leaves.place_block(interface, x1, y1+1, z1-2, leaf_chance)
            tree.palette.leaves.place_block(interface, x1+2, y1+1, z1-1, leaf_chance)
            tree.palette.leaves.place_block(interface, x1-2, y1+1, z1-1, leaf_chance)
            tree.palette.leaves.place_block(interface, x1-1, y1+1, z1+2, leaf_chance)
            tree.palette.leaves.place_block(interface, x1-1, y1+1, z1-2, leaf_chance)
            tree.palette.leaves.place_block(interface, x1+2, y1+1, z1+1, leaf_chance)
            tree.palette.leaves.place_block(interface, x1-2, y1+1, z1+1, leaf_chance)
            tree.palette.leaves.place_block(interface, x1+1, y1+1, z1+2, leaf_chance)
            tree.palette.leaves.place_block(interface, x1+1, y1+1, z1-2, leaf_chance)

            tree.palette.leaves.place_block(interface, x1+1, y1, z1+1, leaf_chance)
            tree.palette.leaves.place_block(interface, x1-1, y1, z1-1, leaf_chance)
            tree.palette.leaves.place_block(interface, x1-1, y1, z1+1, leaf_chance)
            tree.palette.leaves.place_block(interface, x1+1, y1, z1-1, leaf_chance)
            tree.palette.leaves.place_block(interface, x1+1, y1, z1, leaf_chance)
            tree.palette.leaves.place_block(interface, x1-1, y1, z1, leaf_chance)
            tree.palette.leaves.place_block(interface, x1, y1, z1+1, leaf_chance)
            tree.palette.leaves.place_block(interface, x1, y1, z1-1, leaf_chance)

    def generate_large_oak(self, tree, interface, leaf_chance: int=100):
        x0, y0, z0 = tree.get_origin()
        seed()
        height = randint(16,23)+y0
        branch_num = randint(5,10)
        branches = []
        branches.append([x0, height-1, z0])
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
            branch_height = randint(int((height-y0)/2+y0)+5, height-1)
            branch_pos = randint(1, 40)
            if branch_pos == 1:
                branches.append([x0+5,branch_height,z0])
                tree.palette.wood.place_block(interface, x0+5, branch_height, z0)
                tree.palette.wood.place_block(interface, x0+4, branch_height-1, z0)
                tree.palette.wood.place_block(interface, x0+3, branch_height-2, z0)
                tree.palette.wood.place_block(interface, x0+2, branch_height-2, z0)
                tree.palette.wood.place_block(interface, x0+1, branch_height-2, z0)
            elif branch_pos == 2:
                branches.append([x0+5,branch_height,z0+1])
                tree.palette.wood.place_block(interface, x0+5,branch_height,z0+1)
                tree.palette.wood.place_block(interface, x0+4, branch_height-1, z0+1)
                b = randint(1,2)
                if b==1:
                    tree.palette.wood.place_block(interface, x0+3,branch_height-2,z0+1)
                else:
                    tree.palette.wood.place_block(interface, x0+3,branch_height-2,z0)
                tree.palette.wood.place_block(interface, x0+2, branch_height-2, z0)
                tree.palette.wood.place_block(interface, x0+1, branch_height-2, z0)
            elif branch_pos == 3:
                branches.append([x0+5,branch_height,z0+2])
                tree.palette.wood.place_block(interface, x0+5, branch_height, z0+2)
                tree.palette.wood.place_block(interface, x0+4, branch_height-1, z0+2)
                tree.palette.wood.place_block(interface, x0+3, branch_height-2, z0+1)
                tree.palette.wood.place_block(interface, x0+2, branch_height-2, z0+1)
                tree.palette.wood.place_block(interface, x0+1, branch_height-2, z0)
            elif branch_pos == 4:
                branches.append([x0+5,branch_height,z0+3])
                tree.palette.wood.place_block(interface, x0+5, branch_height, z0+3)
                tree.palette.wood.place_block(interface, x0+4, branch_height-1, z0+3)
                b = randint(1,3)
                if b==1:
                    tree.palette.wood.place_block(interface, x0+3,branch_height-2,z0+3)
                    tree.palette.wood.place_block(interface, x0+2, branch_height-2, z0+2)
                elif b==2:
                    tree.palette.wood.place_block(interface, x0+3,branch_height-2,z0+2)
                    tree.palette.wood.place_block(interface, x0+2, branch_height-2, z0+2)
                else:
                    tree.palette.wood.place_block(interface, x0+3,branch_height-2,z0+2)
                    tree.palette.wood.place_block(interface, x0+2, branch_height-2, z0+1)
                tree.palette.wood.place_block(interface, x0+1, branch_height-2, z0+1) 
            elif branch_pos == 5:
                branches.append([x0+5,branch_height,z0+4])
                tree.palette.wood.place_block(interface, x0+5, branch_height, z0+4)
                tree.palette.wood.place_block(interface, x0+4, branch_height-1, z0+3)
                b = randint(1,3)
                if b==1:
                    tree.palette.wood.place_block(interface, x0+3,branch_height-2,z0+3)
                    tree.palette.wood.place_block(interface, x0+2, branch_height-2, z0+2)
                elif b==2:
                    tree.palette.wood.place_block(interface, x0+3,branch_height-2,z0+2)
                    tree.palette.wood.place_block(interface, x0+2, branch_height-2, z0+2)
                else:
                    tree.palette.wood.place_block(interface, x0+3,branch_height-2,z0+2)
                    tree.palette.wood.place_block(interface, x0+2, branch_height-2, z0+1)
                tree.palette.wood.place_block(interface, x0+1, branch_height-2, z0+1) 
            elif branch_pos == 6:
                branches.append([x0+5,branch_height,z0+5])
                tree.palette.wood.place_block(interface, x0+5, branch_height, z0+5)
                tree.palette.wood.place_block(interface, x0+4, branch_height-1, z0+4)
                tree.palette.wood.place_block(interface, x0+3, branch_height-2, z0+3)
                tree.palette.wood.place_block(interface, x0+2, branch_height-2, z0+2)
                tree.palette.wood.place_block(interface, x0+1, branch_height-2, z0+1)
            elif branch_pos == 7:
                branches.append([x0+4,branch_height,z0+5])
                tree.palette.wood.place_block(interface, x0+4, branch_height, z0+5)
                tree.palette.wood.place_block(interface, x0+3, branch_height-1, z0+4)
                b = randint(1,3)
                if b==1:
                    tree.palette.wood.place_block(interface, x0+3,branch_height-2,z0+3)
                    tree.palette.wood.place_block(interface, x0+2, branch_height-2, z0+2)
                elif b==2:
                    tree.palette.wood.place_block(interface, x0+2,branch_height-2,z0+3)
                    tree.palette.wood.place_block(interface, x0+2, branch_height-2, z0+2)
                else:
                    tree.palette.wood.place_block(interface, x0+2,branch_height-2,z0+3)
                    tree.palette.wood.place_block(interface, x0+1, branch_height-2, z0+2)
                tree.palette.wood.place_block(interface, x0+1, branch_height-2, z0+1) 
            elif branch_pos == 8:
                branches.append([x0+3,branch_height,z0+5])
                tree.palette.wood.place_block(interface, x0+3, branch_height, z0+5)
                tree.palette.wood.place_block(interface, x0+3, branch_height-1, z0+4)
                b = randint(1,3)
                if b==1:
                    tree.palette.wood.place_block(interface, x0+3,branch_height-2,z0+3)
                    tree.palette.wood.place_block(interface, x0+2, branch_height-2, z0+2)
                elif b==2:
                    tree.palette.wood.place_block(interface, x0+2,branch_height-2,z0+3)
                    tree.palette.wood.place_block(interface, x0+2, branch_height-2, z0+2)
                else:
                    tree.palette.wood.place_block(interface, x0+2,branch_height-2,z0+3)
                    tree.palette.wood.place_block(interface, x0+1, branch_height-2, z0+2)
                tree.palette.wood.place_block(interface, x0+1, branch_height-2, z0+1) 
            elif branch_pos == 9:
                branches.append([x0+2,branch_height,z0+5])
                tree.palette.wood.place_block(interface, x0+2, branch_height, z0+5)
                tree.palette.wood.place_block(interface, x0+2, branch_height-1, z0+4)
                tree.palette.wood.place_block(interface, x0+1, branch_height-2, z0+3)
                tree.palette.wood.place_block(interface, x0+1, branch_height-2, z0+2)
                tree.palette.wood.place_block(interface, x0, branch_height-2, z0+1)
            elif branch_pos == 10:
                branches.append([x0+1,branch_height,z0+5])
                tree.palette.wood.place_block(interface, x0+1,branch_height,z0+5)
                tree.palette.wood.place_block(interface, x0+1, branch_height-1, z0+4)
                b = randint(1,2)
                if b==1:
                    tree.palette.wood.place_block(interface, x0+1,branch_height-2,z0+3)
                else:
                    tree.palette.wood.place_block(interface, x0,branch_height-2,z0+3)
                tree.palette.wood.place_block(interface, x0, branch_height-2, z0+2)
                tree.palette.wood.place_block(interface, x0, branch_height-2, z0+1)
            if branch_pos == 11:
                branches.append([x0,branch_height,z0+5])
                tree.palette.wood.place_block(interface, x0, branch_height, z0+5)
                tree.palette.wood.place_block(interface, x0, branch_height-1, z0+4)
                tree.palette.wood.place_block(interface, x0, branch_height-2, z0+3)
                tree.palette.wood.place_block(interface, x0, branch_height-2, z0+2)
                tree.palette.wood.place_block(interface, x0, branch_height-2, z0+1)
            elif branch_pos == 12:
                branches.append([x0-1,branch_height,z0+5])
                tree.palette.wood.place_block(interface, x0-1,branch_height,z0+5)
                tree.palette.wood.place_block(interface, x0-1, branch_height-1, z0+4)
                b = randint(1,2)
                if b==1:
                    tree.palette.wood.place_block(interface, x0-1,branch_height-2,z0+3)
                else:
                    tree.palette.wood.place_block(interface, x0,branch_height-2,z0+3)
                tree.palette.wood.place_block(interface, x0, branch_height-2, z0+2)
                tree.palette.wood.place_block(interface, x0, branch_height-2, z0+1)
            elif branch_pos == 13:
                branches.append([x0-2,branch_height,z0+5])
                tree.palette.wood.place_block(interface, x0-2, branch_height, z0+5)
                tree.palette.wood.place_block(interface, x0-2, branch_height-1, z0+4)
                tree.palette.wood.place_block(interface, x0-1, branch_height-2, z0+3)
                tree.palette.wood.place_block(interface, x0-1, branch_height-2, z0+2)
                tree.palette.wood.place_block(interface, x0, branch_height-2, z0+1)
            elif branch_pos == 14:
                branches.append([x0-3,branch_height,z0+5])
                tree.palette.wood.place_block(interface, x0-3, branch_height, z0+5)
                tree.palette.wood.place_block(interface, x0-3, branch_height-1, z0+4)
                b = randint(1,3)
                if b==1:
                    tree.palette.wood.place_block(interface, x0-3,branch_height-2,z0+3)
                    tree.palette.wood.place_block(interface, x0-2, branch_height-2, z0+2)
                elif b==2:
                    tree.palette.wood.place_block(interface, x0-2,branch_height-2,z0+3)
                    tree.palette.wood.place_block(interface, x0-2, branch_height-2, z0+2)
                else:
                    tree.palette.wood.place_block(interface, x0-2,branch_height-2,z0+3)
                    tree.palette.wood.place_block(interface, x0-1, branch_height-2, z0+2)
                tree.palette.wood.place_block(interface, x0-1, branch_height-2, z0+1) 
            elif branch_pos == 15:
                branches.append([x0-4,branch_height,z0+5])
                tree.palette.wood.place_block(interface, x0-4, branch_height, z0+5)
                tree.palette.wood.place_block(interface, x0-3, branch_height-1, z0+4)
                b = randint(1,3)
                if b==1:
                    tree.palette.wood.place_block(interface, x0-3,branch_height-2,z0+3)
                    tree.palette.wood.place_block(interface, x0-2, branch_height-2, z0+2)
                elif b==2:
                    tree.palette.wood.place_block(interface, x0-2,branch_height-2,z0+3)
                    tree.palette.wood.place_block(interface, x0-2, branch_height-2, z0+2)
                else:
                    tree.palette.wood.place_block(interface, x0-2,branch_height-2,z0+3)
                    tree.palette.wood.place_block(interface, x0-1, branch_height-2, z0+2)
                tree.palette.wood.place_block(interface, x0-1, branch_height-2, z0+1) 
            elif branch_pos == 16:
                branches.append([x0-5,branch_height,z0+5])
                tree.palette.wood.place_block(interface, x0-5, branch_height, z0+5)
                tree.palette.wood.place_block(interface, x0-4, branch_height-1, z0+4)
                tree.palette.wood.place_block(interface, x0-3, branch_height-2, z0+3)
                tree.palette.wood.place_block(interface, x0-2, branch_height-2, z0+2)
                tree.palette.wood.place_block(interface, x0-1, branch_height-2, z0+1)
            elif branch_pos == 17:
                branches.append([x0-5,branch_height,z0+4])
                tree.palette.wood.place_block(interface, x0-5, branch_height, z0+4)
                tree.palette.wood.place_block(interface, x0-4, branch_height-1, z0+3)
                b = randint(1,3)
                if b==1:
                    tree.palette.wood.place_block(interface, x0-3,branch_height-2,z0+3)
                    tree.palette.wood.place_block(interface, x0-2, branch_height-2, z0+2)
                elif b==2:
                    tree.palette.wood.place_block(interface, x0-3,branch_height-2,z0+2)
                    tree.palette.wood.place_block(interface, x0-2, branch_height-2, z0+2)
                else:
                    tree.palette.wood.place_block(interface, x0-3,branch_height-2,z0+2)
                    tree.palette.wood.place_block(interface, x0-2, branch_height-2, z0+1)
                tree.palette.wood.place_block(interface, x0-1, branch_height-2, z0+1) 
            elif branch_pos == 18:
                branches.append([x0-5,branch_height,z0+3])
                tree.palette.wood.place_block(interface, x0-5, branch_height, z0+3)
                tree.palette.wood.place_block(interface, x0-4, branch_height-1, z0+3)
                b = randint(1,3)
                if b==1:
                    tree.palette.wood.place_block(interface, x0-3,branch_height-2,z0+3)
                    tree.palette.wood.place_block(interface, x0-2, branch_height-2, z0+2)
                elif b==2:
                    tree.palette.wood.place_block(interface, x0-3,branch_height-2,z0+2)
                    tree.palette.wood.place_block(interface, x0-2, branch_height-2, z0+2)
                else:
                    tree.palette.wood.place_block(interface, x0-3,branch_height-2,z0+2)
                    tree.palette.wood.place_block(interface, x0-2, branch_height-2, z0+1)
                tree.palette.wood.place_block(interface, x0-1, branch_height-2, z0+1) 
            elif branch_pos == 19:
                branches.append([x0-5,branch_height,z0+2])
                tree.palette.wood.place_block(interface, x0-5, branch_height, z0+2)
                tree.palette.wood.place_block(interface, x0-4, branch_height-1, z0+2)
                tree.palette.wood.place_block(interface, x0-3, branch_height-2, z0+1)
                tree.palette.wood.place_block(interface, x0-2, branch_height-2, z0+1)
                tree.palette.wood.place_block(interface, x0-1, branch_height-2, z0)
            elif branch_pos == 20:
                branches.append([x0-5,branch_height,z0+1])
                tree.palette.wood.place_block(interface, x0-5,branch_height,z0+1)
                tree.palette.wood.place_block(interface, x0-4, branch_height-1, z0+1)
                b = randint(1,2)
                if b==1:
                    tree.palette.wood.place_block(interface, x0-3,branch_height-2,z0+1)
                else:
                    tree.palette.wood.place_block(interface, x0-3,branch_height-2,z0)
                tree.palette.wood.place_block(interface, x0-2, branch_height-2, z0)
                tree.palette.wood.place_block(interface, x0-1, branch_height-2, z0)
            if branch_pos == 21:
                branches.append([x0-5,branch_height,z0])
                tree.palette.wood.place_block(interface, x0-5, branch_height, z0)
                tree.palette.wood.place_block(interface, x0-4, branch_height-1, z0)
                tree.palette.wood.place_block(interface, x0-3, branch_height-2, z0)
                tree.palette.wood.place_block(interface, x0-2, branch_height-2, z0)
                tree.palette.wood.place_block(interface, x0-1, branch_height-2, z0)
            elif branch_pos == 22:
                branches.append([x0-5,branch_height,z0-1])
                tree.palette.wood.place_block(interface, x0-5,branch_height,z0-1)
                tree.palette.wood.place_block(interface, x0-4, branch_height-1, z0-1)
                b = randint(1,2)
                if b==1:
                    tree.palette.wood.place_block(interface, x0-3,branch_height-2,z0-1)
                else:
                    tree.palette.wood.place_block(interface, x0-3,branch_height-2,z0)
                tree.palette.wood.place_block(interface, x0-2, branch_height-2, z0)
                tree.palette.wood.place_block(interface, x0-1, branch_height-2, z0)
            elif branch_pos == 23:
                branches.append([x0-5,branch_height,z0-2])
                tree.palette.wood.place_block(interface, x0-5, branch_height, z0-2)
                tree.palette.wood.place_block(interface, x0-4, branch_height-1, z0-2)
                tree.palette.wood.place_block(interface, x0-3, branch_height-2, z0-1)
                tree.palette.wood.place_block(interface, x0-2, branch_height-2, z0-1)
                tree.palette.wood.place_block(interface, x0-1, branch_height-2, z0)
            elif branch_pos == 24:
                branches.append([x0-5,branch_height,z0-3])
                tree.palette.wood.place_block(interface, x0-5, branch_height, z0-3)
                tree.palette.wood.place_block(interface, x0-4, branch_height-1, z0-3)
                b = randint(1,3)
                if b==1:
                    tree.palette.wood.place_block(interface, x0-3,branch_height-2,z0-3)
                    tree.palette.wood.place_block(interface, x0-2, branch_height-2, z0-2)
                elif b==2:
                    tree.palette.wood.place_block(interface, x0-3,branch_height-2,z0-2)
                    tree.palette.wood.place_block(interface, x0-2, branch_height-2, z0-2)
                else:
                    tree.palette.wood.place_block(interface, x0-3,branch_height-2,z0-2)
                    tree.palette.wood.place_block(interface, x0-2, branch_height-2, z0-1)
                tree.palette.wood.place_block(interface, x0-1, branch_height-2, z0-1)
            elif branch_pos == 25:
                branches.append([x0-5,branch_height,z0-4])
                tree.palette.wood.place_block(interface, x0-5, branch_height, z0-4)
                tree.palette.wood.place_block(interface, x0-4, branch_height-1, z0-3)
                b = randint(1,3)
                if b==1:
                    tree.palette.wood.place_block(interface, x0-3,branch_height-2,z0-3)
                    tree.palette.wood.place_block(interface, x0-2, branch_height-2, z0-2)
                elif b==2:
                    tree.palette.wood.place_block(interface, x0-3,branch_height-2,z0-2)
                    tree.palette.wood.place_block(interface, x0-2, branch_height-2, z0-2)
                else:
                    tree.palette.wood.place_block(interface, x0-3,branch_height-2,z0-2)
                    tree.palette.wood.place_block(interface, x0-2, branch_height-2, z0-1)
                tree.palette.wood.place_block(interface, x0-1, branch_height-2, z0-1) 
            elif branch_pos == 26:
                branches.append([x0-5,branch_height,z0-5])
                tree.palette.wood.place_block(interface, x0-5, branch_height, z0-5)
                tree.palette.wood.place_block(interface, x0-4, branch_height-1, z0-4)
                tree.palette.wood.place_block(interface, x0-3, branch_height-2, z0-3)
                tree.palette.wood.place_block(interface, x0-2, branch_height-2, z0-2)
                tree.palette.wood.place_block(interface, x0-1, branch_height-2, z0-1)
            elif branch_pos == 27:
                branches.append([x0+5,branch_height,z0-5])
                tree.palette.wood.place_block(interface, x0+5, branch_height, z0-5)
                tree.palette.wood.place_block(interface, x0+4, branch_height-1, z0-4)
                tree.palette.wood.place_block(interface, x0+3, branch_height-2, z0-3)
                tree.palette.wood.place_block(interface, x0+2, branch_height-2, z0-2)
                tree.palette.wood.place_block(interface, x0+1, branch_height-2, z0-1)
            elif branch_pos == 28:
                branches.append([x0+4,branch_height,z0-5])
                tree.palette.wood.place_block(interface, x0+4, branch_height, z0-5)
                tree.palette.wood.place_block(interface, x0+3, branch_height-1, z0-4)
                b = randint(1,3)
                if b==1:
                    tree.palette.wood.place_block(interface, x0+3,branch_height-2,z0-3)
                    tree.palette.wood.place_block(interface, x0+2, branch_height-2, z0-2)
                elif b==2:
                    tree.palette.wood.place_block(interface, x0+2,branch_height-2,z0-3)
                    tree.palette.wood.place_block(interface, x0+2, branch_height-2, z0-2)
                else:
                    tree.palette.wood.place_block(interface, x0+2,branch_height-2,z0-3)
                    tree.palette.wood.place_block(interface, x0+1, branch_height-2, z0-2)
                tree.palette.wood.place_block(interface, x0+1, branch_height-2, z0-1) 
            elif branch_pos == 29:
                branches.append([x0+3,branch_height,z0-5])
                tree.palette.wood.place_block(interface, x0+3, branch_height, z0-5)
                tree.palette.wood.place_block(interface, x0+3, branch_height-1, z0-4)
                b = randint(1,3)
                if b==1:
                    tree.palette.wood.place_block(interface, x0+3,branch_height-2,z0-3)
                    tree.palette.wood.place_block(interface, x0+2, branch_height-2, z0-2)
                elif b==2:
                    tree.palette.wood.place_block(interface, x0+2,branch_height-2,z0-3)
                    tree.palette.wood.place_block(interface, x0+2, branch_height-2, z0-2)
                else:
                    tree.palette.wood.place_block(interface, x0+2,branch_height-2,z0-3)
                    tree.palette.wood.place_block(interface, x0+1, branch_height-2, z0-2)
                tree.palette.wood.place_block(interface, x0+1, branch_height-2, z0-1) 
            elif branch_pos == 30:
                branches.append([x0+2,branch_height,z0-5])
                tree.palette.wood.place_block(interface, x0+2, branch_height, z0-5)
                tree.palette.wood.place_block(interface, x0+2, branch_height-1, z0-4)
                tree.palette.wood.place_block(interface, x0+1, branch_height-2, z0-3)
                tree.palette.wood.place_block(interface, x0+1, branch_height-2, z0-2)
                tree.palette.wood.place_block(interface, x0, branch_height-2, z0-1)
            elif branch_pos == 31:
                branches.append([x0+1,branch_height,z0-5])
                tree.palette.wood.place_block(interface, x0+1,branch_height,z0-5)
                tree.palette.wood.place_block(interface, x0+1, branch_height-1, z0-4)
                b = randint(1,2)
                if b==1:
                    tree.palette.wood.place_block(interface, x0+1,branch_height-2,z0-3)
                else:
                    tree.palette.wood.place_block(interface, x0,branch_height-2,z0-3)
                tree.palette.wood.place_block(interface, x0, branch_height-2, z0-2)
                tree.palette.wood.place_block(interface, x0, branch_height-2, z0-1)
            elif branch_pos == 32:
                branches.append([x0,branch_height,z0-5])
                tree.palette.wood.place_block(interface, x0, branch_height, z0-5)
                tree.palette.wood.place_block(interface, x0, branch_height-1, z0-4)
                tree.palette.wood.place_block(interface, x0, branch_height-2, z0-3)
                tree.palette.wood.place_block(interface, x0, branch_height-2, z0-2)
                tree.palette.wood.place_block(interface, x0, branch_height-2, z0-1)
            elif branch_pos == 33:
                branches.append([x0-1,branch_height,z0-5])
                tree.palette.wood.place_block(interface, x0-1,branch_height,z0-5)
                tree.palette.wood.place_block(interface, x0-1, branch_height-1, z0-4)
                b = randint(1,2)
                if b==1:
                    tree.palette.wood.place_block(interface, x0-1,branch_height-2,z0-3)
                else:
                    tree.palette.wood.place_block(interface, x0,branch_height-2,z0-3)
                tree.palette.wood.place_block(interface, x0, branch_height-2, z0-2)
                tree.palette.wood.place_block(interface, x0, branch_height-2, z0-1)
            elif branch_pos == 34:
                branches.append([x0-2,branch_height,z0-5])
                tree.palette.wood.place_block(interface, x0-2, branch_height, z0-5)
                tree.palette.wood.place_block(interface, x0-2, branch_height-1, z0-4)
                tree.palette.wood.place_block(interface, x0-1, branch_height-2, z0-3)
                tree.palette.wood.place_block(interface, x0-1, branch_height-2, z0-2)
                tree.palette.wood.place_block(interface, x0, branch_height-2, z0-1)
            elif branch_pos == 35:
                branches.append([x0-3,branch_height,z0-5])
                tree.palette.wood.place_block(interface, x0-3, branch_height, z0-5)
                tree.palette.wood.place_block(interface, x0-3, branch_height-1, z0-4)
                b = randint(1,3)
                if b==1:
                    tree.palette.wood.place_block(interface, x0-3,branch_height-2,z0-3)
                    tree.palette.wood.place_block(interface, x0-2, branch_height-2, z0-2)
                elif b==2:
                    tree.palette.wood.place_block(interface, x0-2,branch_height-2,z0-3)
                    tree.palette.wood.place_block(interface, x0-2, branch_height-2, z0-2)
                else:
                    tree.palette.wood.place_block(interface, x0-2,branch_height-2,z0-3)
                    tree.palette.wood.place_block(interface, x0-1, branch_height-2, z0-2)
                tree.palette.wood.place_block(interface, x0-1, branch_height-2, z0-1) 
            elif branch_pos == 36:
                branches.append([x0-4,branch_height,z0-5])
                tree.palette.wood.place_block(interface, x0-4, branch_height, z0-5)
                tree.palette.wood.place_block(interface, x0-3, branch_height-1, z0-4)
                b = randint(1,3)
                if b==1:
                    tree.palette.wood.place_block(interface, x0-3,branch_height-2,z0-3)
                    tree.palette.wood.place_block(interface, x0-2, branch_height-2, z0-2)
                elif b==2:
                    tree.palette.wood.place_block(interface, x0-2,branch_height-2,z0-3)
                    tree.palette.wood.place_block(interface, x0-2, branch_height-2, z0-2)
                else:
                    tree.palette.wood.place_block(interface, x0-2,branch_height-2,z0-3)
                    tree.palette.wood.place_block(interface, x0-1, branch_height-2, z0-2)
                tree.palette.wood.place_block(interface, x0-1, branch_height-2, z0-1)
            elif branch_pos == 37:
                branches.append([x0+5,branch_height,z0-1])
                tree.palette.wood.place_block(interface, x0+5,branch_height,z0-1)
                tree.palette.wood.place_block(interface, x0+4, branch_height-1, z0-1)
                b = randint(1,2)
                if b==1:
                    tree.palette.wood.place_block(interface, x0+3,branch_height-2,z0-1)
                else:
                    tree.palette.wood.place_block(interface, x0+3,branch_height-2,z0)
                tree.palette.wood.place_block(interface, x0+2, branch_height-2, z0)
                tree.palette.wood.place_block(interface, x0+1, branch_height-2, z0)
            elif branch_pos == 38:
                branches.append([x0+5,branch_height,z0-2])
                tree.palette.wood.place_block(interface, x0+5, branch_height, z0-2)
                tree.palette.wood.place_block(interface, x0+4, branch_height-1, z0-2)
                tree.palette.wood.place_block(interface, x0+3, branch_height-2, z0-1)
                tree.palette.wood.place_block(interface, x0+2, branch_height-2, z0-1)
                tree.palette.wood.place_block(interface, x0+1, branch_height-2, z0)
            elif branch_pos == 39:
                branches.append([x0+5,branch_height,z0-3])
                tree.palette.wood.place_block(interface, x0+5, branch_height, z0-3)
                tree.palette.wood.place_block(interface, x0+4, branch_height-1, z0-3)
                b = randint(1,3)
                if b==1:
                    tree.palette.wood.place_block(interface, x0+3,branch_height-2,z0-3)
                    tree.palette.wood.place_block(interface, x0+2, branch_height-2, z0-2)
                elif b==2:
                    tree.palette.wood.place_block(interface, x0+3,branch_height-2,z0-2)
                    tree.palette.wood.place_block(interface, x0+2, branch_height-2, z0-2)
                else:
                    tree.palette.wood.place_block(interface, x0+3,branch_height-2,z0-2)
                    tree.palette.wood.place_block(interface, x0+2, branch_height-2, z0-1)
                tree.palette.wood.place_block(interface, x0+1, branch_height-2, z0-1) 
            elif branch_pos == 40:
                branches.append([x0+5,branch_height,z0-4])
                tree.palette.wood.place_block(interface, x0+5, branch_height, z0-4)
                tree.palette.wood.place_block(interface, x0+4, branch_height-1, z0-3)
                b = randint(1,3)
                if b==1:
                    tree.palette.wood.place_block(interface, x0+3,branch_height-2,z0-3)
                    tree.palette.wood.place_block(interface, x0+2, branch_height-2, z0-2)
                elif b==2:
                    tree.palette.wood.place_block(interface, x0+3,branch_height-2,z0-2)
                    tree.palette.wood.place_block(interface, x0+2, branch_height-2, z0-2)
                else:
                    tree.palette.wood.place_block(interface, x0+3,branch_height-2,z0-2)
                    tree.palette.wood.place_block(interface, x0+2, branch_height-2, z0-1)
                tree.palette.wood.place_block(interface, x0+1, branch_height-2, z0-1) 
             


        for branch in branches:
            x1, y1, z1 = branch[0], branch[1], branch[2]
            if x1 == x0 and z1 == z0:
                #more leaves for the main stem/branch
                tree.palette.leaves.place_block(interface, x1+1, y1+3, z1+1, leaf_chance)
                tree.palette.leaves.place_block(interface, x1-1, y1+3, z1-1, leaf_chance)
                tree.palette.leaves.place_block(interface, x1-1, y1+3, z1+1, leaf_chance)
                tree.palette.leaves.place_block(interface, x1+1, y1+3, z1-1, leaf_chance)

                tree.palette.leaves.place_block(interface, x1+3, y1+2, z1, leaf_chance)
                tree.palette.leaves.place_block(interface, x1-3, y1+2, z1, leaf_chance)
                tree.palette.leaves.place_block(interface, x1, y1+2, z1+3, leaf_chance)
                tree.palette.leaves.place_block(interface, x1, y1+2, z1-3, leaf_chance)
                tree.palette.leaves.place_block(interface, x1+2, y1+2, z1+2, leaf_chance)
                tree.palette.leaves.place_block(interface, x1-2, y1+2, z1-2, leaf_chance)
                tree.palette.leaves.place_block(interface, x1-2, y1+2, z1+2, leaf_chance)
                tree.palette.leaves.place_block(interface, x1+2, y1+2, z1-2, leaf_chance)

                tree.palette.leaves.place_block(interface, x1+4, y1+1, z1+1, leaf_chance)
                tree.palette.leaves.place_block(interface, x1-4, y1+1, z1-1, leaf_chance)
                tree.palette.leaves.place_block(interface, x1-4, y1+1, z1+1, leaf_chance)
                tree.palette.leaves.place_block(interface, x1+4, y1+1, z1-1, leaf_chance)
                tree.palette.leaves.place_block(interface, x1+1, y1+1, z1+4, leaf_chance)
                tree.palette.leaves.place_block(interface, x1-1, y1+1, z1+4, leaf_chance)
                tree.palette.leaves.place_block(interface, x1+1, y1+1, z1-4, leaf_chance)
                tree.palette.leaves.place_block(interface, x1-1, y1+1, z1-4, leaf_chance)
                tree.palette.leaves.place_block(interface, x1+4, y1+1, z1, leaf_chance)
                tree.palette.leaves.place_block(interface, x1-4, y1+1, z1, leaf_chance)
                tree.palette.leaves.place_block(interface, x1, y1+1, z1+4, leaf_chance)
                tree.palette.leaves.place_block(interface, x1, y1+1, z1-4, leaf_chance)
                tree.palette.leaves.place_block(interface, x1+3, y1+1, z1+3, leaf_chance)
                tree.palette.leaves.place_block(interface, x1-3, y1+1, z1-3, leaf_chance)
                tree.palette.leaves.place_block(interface, x1-3, y1+1, z1+3, leaf_chance)
                tree.palette.leaves.place_block(interface, x1+3, y1+1, z1-3, leaf_chance)
                tree.palette.leaves.place_block(interface, x1+2, y1+1, z1+3, leaf_chance)
                tree.palette.leaves.place_block(interface, x1-2, y1+1, z1+3, leaf_chance)
                tree.palette.leaves.place_block(interface, x1+2, y1+1, z1-3, leaf_chance)
                tree.palette.leaves.place_block(interface, x1-2, y1+1, z1-3, leaf_chance)
                tree.palette.leaves.place_block(interface, x1+3, y1+1, z1+2, leaf_chance)
                tree.palette.leaves.place_block(interface, x1-3, y1+1, z1-2, leaf_chance)
                tree.palette.leaves.place_block(interface, x1-3, y1+1, z1+2, leaf_chance)
                tree.palette.leaves.place_block(interface, x1+3, y1+1, z1-2, leaf_chance)

                tree.palette.leaves.place_block(interface, x1+2, y1, z1-1, leaf_chance)
                tree.palette.leaves.place_block(interface, x1-2, y1, z1-1, leaf_chance)
                tree.palette.leaves.place_block(interface, x1-1, y1, z1+2, leaf_chance)
                tree.palette.leaves.place_block(interface, x1-1, y1, z1-2, leaf_chance)
                tree.palette.leaves.place_block(interface, x1+2, y1, z1+1, leaf_chance)
                tree.palette.leaves.place_block(interface, x1-2, y1, z1+1, leaf_chance)
                tree.palette.leaves.place_block(interface, x1+1, y1, z1+2, leaf_chance)
                tree.palette.leaves.place_block(interface, x1+1, y1, z1-2, leaf_chance)

            else:
                tree.palette.leaves.place_block(interface, x1, y1-1, z1, leaf_chance)
            
            tree.palette.leaves.place_block(interface, x1+1, y1+3, z1, leaf_chance)
            tree.palette.leaves.place_block(interface, x1-1, y1+3, z1, leaf_chance)
            tree.palette.leaves.place_block(interface, x1, y1+3, z1+1, leaf_chance)
            tree.palette.leaves.place_block(interface, x1, y1+3, z1-1, leaf_chance)
            tree.palette.leaves.place_block(interface, x1, y1+3, z1, leaf_chance)

            tree.palette.leaves.place_block(interface, x1, y1+2, z1, leaf_chance)
            tree.palette.leaves.place_block(interface, x1+1, y1+2, z1+1, leaf_chance)
            tree.palette.leaves.place_block(interface, x1-1, y1+2, z1-1, leaf_chance)
            tree.palette.leaves.place_block(interface, x1-1, y1+2, z1+1, leaf_chance)
            tree.palette.leaves.place_block(interface, x1+1, y1+2, z1-1, leaf_chance)
            tree.palette.leaves.place_block(interface, x1+1, y1+2, z1, leaf_chance)
            tree.palette.leaves.place_block(interface, x1-1, y1+2, z1, leaf_chance)
            tree.palette.leaves.place_block(interface, x1, y1+2, z1+1, leaf_chance)
            tree.palette.leaves.place_block(interface, x1, y1+2, z1-1, leaf_chance)
            tree.palette.leaves.place_block(interface, x1+2, y1+2, z1, leaf_chance)
            tree.palette.leaves.place_block(interface, x1-2, y1+2, z1, leaf_chance)
            tree.palette.leaves.place_block(interface, x1, y1+2, z1+2, leaf_chance)
            tree.palette.leaves.place_block(interface, x1, y1+2, z1-2, leaf_chance)
            tree.palette.leaves.place_block(interface, x1+2, y1+2, z1-1, leaf_chance)
            tree.palette.leaves.place_block(interface, x1-2, y1+2, z1-1, leaf_chance)
            tree.palette.leaves.place_block(interface, x1-1, y1+2, z1+2, leaf_chance)
            tree.palette.leaves.place_block(interface, x1-1, y1+2, z1-2, leaf_chance)
            tree.palette.leaves.place_block(interface, x1+2, y1+2, z1+1, leaf_chance)
            tree.palette.leaves.place_block(interface, x1-2, y1+2, z1+1, leaf_chance)
            tree.palette.leaves.place_block(interface, x1+1, y1+2, z1+2, leaf_chance)
            tree.palette.leaves.place_block(interface, x1+1, y1+2, z1-2, leaf_chance)

            tree.palette.leaves.place_block(interface, x1, y1+1, z1, leaf_chance)
            tree.palette.leaves.place_block(interface, x1+1, y1+1, z1+1, leaf_chance)
            tree.palette.leaves.place_block(interface, x1-1, y1+1, z1-1, leaf_chance)
            tree.palette.leaves.place_block(interface, x1-1, y1+1, z1+1, leaf_chance)
            tree.palette.leaves.place_block(interface, x1+1, y1+1, z1-1, leaf_chance)
            tree.palette.leaves.place_block(interface, x1+1, y1+1, z1, leaf_chance)
            tree.palette.leaves.place_block(interface, x1-1, y1+1, z1, leaf_chance)
            tree.palette.leaves.place_block(interface, x1, y1+1, z1+1, leaf_chance)
            tree.palette.leaves.place_block(interface, x1, y1+1, z1-1, leaf_chance)
            tree.palette.leaves.place_block(interface, x1+2, y1+1, z1, leaf_chance)
            tree.palette.leaves.place_block(interface, x1-2, y1+1, z1, leaf_chance)
            tree.palette.leaves.place_block(interface, x1, y1+1, z1+2, leaf_chance)
            tree.palette.leaves.place_block(interface, x1, y1+1, z1-2, leaf_chance)
            tree.palette.leaves.place_block(interface, x1+2, y1+1, z1-1, leaf_chance)
            tree.palette.leaves.place_block(interface, x1-2, y1+1, z1-1, leaf_chance)
            tree.palette.leaves.place_block(interface, x1-1, y1+1, z1+2, leaf_chance)
            tree.palette.leaves.place_block(interface, x1-1, y1+1, z1-2, leaf_chance)
            tree.palette.leaves.place_block(interface, x1+2, y1+1, z1+1, leaf_chance)
            tree.palette.leaves.place_block(interface, x1-2, y1+1, z1+1, leaf_chance)
            tree.palette.leaves.place_block(interface, x1+1, y1+1, z1+2, leaf_chance)
            tree.palette.leaves.place_block(interface, x1+1, y1+1, z1-2, leaf_chance)
            tree.palette.leaves.place_block(interface, x1+2, y1+1, z1+2, leaf_chance)
            tree.palette.leaves.place_block(interface, x1-2, y1+1, z1-2, leaf_chance)
            tree.palette.leaves.place_block(interface, x1-2, y1+1, z1+2, leaf_chance)
            tree.palette.leaves.place_block(interface, x1+2, y1+1, z1-2, leaf_chance)
            tree.palette.leaves.place_block(interface, x1+3, y1+1, z1+1, leaf_chance)
            tree.palette.leaves.place_block(interface, x1-3, y1+1, z1-1, leaf_chance)
            tree.palette.leaves.place_block(interface, x1-3, y1+1, z1+1, leaf_chance)
            tree.palette.leaves.place_block(interface, x1+3, y1+1, z1-1, leaf_chance)
            tree.palette.leaves.place_block(interface, x1+1, y1+1, z1+3, leaf_chance)
            tree.palette.leaves.place_block(interface, x1-1, y1+1, z1+3, leaf_chance)
            tree.palette.leaves.place_block(interface, x1+1, y1+1, z1-3, leaf_chance)
            tree.palette.leaves.place_block(interface, x1-1, y1+1, z1-3, leaf_chance)
            tree.palette.leaves.place_block(interface, x1+3, y1+1, z1, leaf_chance)
            tree.palette.leaves.place_block(interface, x1-3, y1+1, z1, leaf_chance)
            tree.palette.leaves.place_block(interface, x1, y1+1, z1+3, leaf_chance)
            tree.palette.leaves.place_block(interface, x1, y1+1, z1-3, leaf_chance)

            tree.palette.leaves.place_block(interface, x1+1, y1, z1+1, leaf_chance)
            tree.palette.leaves.place_block(interface, x1-1, y1, z1-1, leaf_chance)
            tree.palette.leaves.place_block(interface, x1-1, y1, z1+1, leaf_chance)
            tree.palette.leaves.place_block(interface, x1+1, y1, z1-1, leaf_chance)
            tree.palette.leaves.place_block(interface, x1+1, y1, z1, leaf_chance)
            tree.palette.leaves.place_block(interface, x1-1, y1, z1, leaf_chance)
            tree.palette.leaves.place_block(interface, x1, y1, z1+1, leaf_chance)
            tree.palette.leaves.place_block(interface, x1, y1, z1-1, leaf_chance)
            tree.palette.leaves.place_block(interface, x1+2, y1, z1, leaf_chance)
            tree.palette.leaves.place_block(interface, x1-2, y1, z1, leaf_chance)
            tree.palette.leaves.place_block(interface, x1, y1, z1+2, leaf_chance)
            tree.palette.leaves.place_block(interface, x1, y1, z1-2, leaf_chance)
            
    def generate_mega_oak(self, tree, interface, leaf_chance: int=100):
        self.generate_large_oak(tree, interface, leaf_chance)
        x0, y0, z0 = tree.get_origin()
        new_tree = Tree((x0+1, y0, z0), tree.type)
        self.generate_large_oak(new_tree, interface, leaf_chance)
        new_tree = Tree((x0+1, y0, z0+1), tree.type)
        self.generate_large_oak(new_tree, interface, leaf_chance)
        new_tree = Tree((x0, y0, z0+1), tree.type)
        self.generate_large_oak(new_tree, interface, leaf_chance)

    def generate_small_jungle(self, tree, interface, leaf_chance: int=100):
        x0, y0, z0 = tree.get_origin()
        seed()
        height = randint(7,12)+y0
        branches = []
        
        for y in range (y0,height+1): #tree stem
            tree.palette.wood.place_block(interface, x0, y, z0)

        branches.append([x0, height, z0])

        # random branch generation, 1 random branch for each quadrant
        branch_height = randint(height-4, height-2)
        branch_pos = randint(1, 4)
        if branch_pos == 1:
            branches.append([x0-2,branch_height+1,z0])
            tree.palette.wood.place_block(interface, x0-2, branch_height+1, z0)
            tree.palette.wood.place_block(interface, x0-1, branch_height, z0)
        elif branch_pos == 2:
            branches.append([x0-2,branch_height+1,z0-1])
            tree.palette.wood.place_block(interface, x0-2, branch_height+1, z0-1)
            b = randint(1,2)
            if b==1:
                tree.palette.wood.place_block(interface, x0-1,branch_height,z0-1)
            else:
                tree.palette.wood.place_block(interface, x0-1,branch_height,z0)
        elif branch_pos == 3:
            branches.append([x0-2,branch_height+1,z0-2])
            tree.palette.wood.place_block(interface, x0-2, branch_height+1, z0-2)
            tree.palette.wood.place_block(interface, x0-1,branch_height,z0-1)
        elif branch_pos == 4:
            branches.append([x0-1,branch_height+1,z0-2])
            tree.palette.wood.place_block(interface, x0-1, branch_height+1, z0-2)
            b = randint(1,2)
            if b==1:
                tree.palette.wood.place_block(interface, x0-1,branch_height,z0-1)
            else:
                tree.palette.wood.place_block(interface, x0,branch_height,z0-1)
        branch_height = randint(height-4, height-2)
        branch_pos = randint(1, 4)
        if branch_pos == 1:
            branches.append([x0,branch_height+1,z0-2])
            tree.palette.wood.place_block(interface, x0, branch_height+1, z0-2)
            tree.palette.wood.place_block(interface, x0, branch_height, z0-1)
        elif branch_pos == 2:
            branches.append([x0+2,branch_height+1,z0-1])
            tree.palette.wood.place_block(interface, x0+2, branch_height+1, z0-1)
            b = randint(1,2)
            if b==1:
                tree.palette.wood.place_block(interface, x0+1,branch_height,z0-1)
            else:
                tree.palette.wood.place_block(interface, x0+1,branch_height,z0)
        elif branch_pos == 3:
            branches.append([x0+2,branch_height+1,z0-2])
            tree.palette.wood.place_block(interface, x0+2, branch_height+1, z0-2)
            tree.palette.wood.place_block(interface, x0+1,branch_height,z0-1)
        elif branch_pos == 4:
            branches.append([x0+1,branch_height+1,z0-2])
            tree.palette.wood.place_block(interface, x0+1, branch_height+1, z0-2)
            b = randint(1,2)
            if b==1:
                tree.palette.wood.place_block(interface, x0+1,branch_height,z0-1)
            else:
                tree.palette.wood.place_block(interface, x0,branch_height,z0-1)
        branch_height = randint(height-4, height-2)
        branch_pos = randint(1, 4)
        if branch_pos == 1:
            branches.append([x0+2,branch_height+1,z0])
            tree.palette.wood.place_block(interface, x0+2, branch_height+1, z0)
            tree.palette.wood.place_block(interface, x0+1, branch_height, z0)
        elif branch_pos == 2:
            branches.append([x0+2,branch_height+1,z0+1])
            tree.palette.wood.place_block(interface, x0+2, branch_height+1, z0+1)
            b = randint(1,2)
            if b==1:
                tree.palette.wood.place_block(interface, x0+1,branch_height,z0+1)
            else:
                tree.palette.wood.place_block(interface, x0+1,branch_height,z0)
        elif branch_pos == 3:
            branches.append([x0+2,branch_height+1,z0+2])
            tree.palette.wood.place_block(interface, x0+2, branch_height+1, z0+2)
            tree.palette.wood.place_block(interface, x0+1,branch_height,z0+1)
        elif branch_pos == 4:
            branches.append([x0+1,branch_height+1,z0+2])
            tree.palette.wood.place_block(interface, x0+1, branch_height+1, z0+2)
            b = randint(1,2)
            if b==1:
                tree.palette.wood.place_block(interface, x0+1,branch_height,z0+1)
            else:
                tree.palette.wood.place_block(interface, x0,branch_height,z0+1)
        branch_height = randint(height-4, height-2)
        branch_pos = randint(1, 4)
        if branch_pos == 1:
            branches.append([x0,branch_height+1,z0+2])
            tree.palette.wood.place_block(interface, x0, branch_height+1, z0+2)
            tree.palette.wood.place_block(interface, x0, branch_height, z0+1)
        elif branch_pos == 2:
            branches.append([x0-2,branch_height+1,z0+1])
            tree.palette.wood.place_block(interface, x0-2, branch_height+1, z0+1)
            b = randint(1,2)
            if b==1:
                tree.palette.wood.place_block(interface, x0-1,branch_height,z0+1)
            else:
                tree.palette.wood.place_block(interface, x0-1,branch_height,z0)
        elif branch_pos == 3:
            branches.append([x0-2,branch_height+1,z0+2])
            tree.palette.wood.place_block(interface, x0-2, branch_height+1, z0+2)
            tree.palette.wood.place_block(interface, x0-1,branch_height,z0+1)
        elif branch_pos == 4:
            branches.append([x0-1,branch_height+1,z0+2])
            tree.palette.wood.place_block(interface, x0-1, branch_height+1, z0+2)
            b = randint(1,2)
            if b==1:
                tree.palette.wood.place_block(interface, x0-1,branch_height,z0+1)
            else:
                tree.palette.wood.place_block(interface, x0,branch_height,z0+1)

        for branch in branches:
            x1, y1, z1 = branch[0], branch[1], branch[2]

            tree.palette.leaves.place_block(interface, x1, y1+1, z1, leaf_chance)
            tree.palette.leaves.place_block(interface, x1+1, y1+1, z1, leaf_chance)
            tree.palette.leaves.place_block(interface, x1-1, y1+1, z1, leaf_chance)
            tree.palette.leaves.place_block(interface, x1, y1+1, z1+1, leaf_chance)
            tree.palette.leaves.place_block(interface, x1, y1+1, z1-1, leaf_chance)

            tree.palette.leaves.place_block(interface, x1+1, y1, z1+1, leaf_chance)
            tree.palette.leaves.place_block(interface, x1-1, y1, z1-1, leaf_chance)
            tree.palette.leaves.place_block(interface, x1-1, y1, z1+1, leaf_chance)
            tree.palette.leaves.place_block(interface, x1+1, y1, z1-1, leaf_chance)
            tree.palette.leaves.place_block(interface, x1+1, y1, z1, leaf_chance)
            tree.palette.leaves.place_block(interface, x1-1, y1, z1, leaf_chance)
            tree.palette.leaves.place_block(interface, x1, y1, z1+1, leaf_chance)
            tree.palette.leaves.place_block(interface, x1, y1, z1-1, leaf_chance)
            tree.palette.leaves.place_block(interface, x1+2, y1, z1, leaf_chance)
            tree.palette.leaves.place_block(interface, x1-2, y1, z1, leaf_chance)
            tree.palette.leaves.place_block(interface, x1, y1, z1+2, leaf_chance)
            tree.palette.leaves.place_block(interface, x1, y1, z1-2, leaf_chance)

    def generate_medium_jungle(self, tree, interface, leaf_chance: int=100):
        x0, y0, z0 = tree.get_origin()
        seed()
        height = randint(10,18)+y0
        branches = []
        
        for y in range (y0,height+1): #tree stem
            tree.palette.wood.place_block(interface, x0, y, z0)

        branches.append([x0, height, z0])

        # random branch generation, 1 random branch for each quadrant
        branch_height = randint(height-5, height-2)
        branch_pos = randint(1, 3)
        if branch_pos == 1:
            branches.append([x0-3,branch_height+1,z0-3])
            tree.palette.wood.place_block(interface, x0-3, branch_height+1, z0-3)
            tree.palette.wood.place_block(interface, x0-2, branch_height, z0-2)
            tree.palette.wood.place_block(interface, x0-1, branch_height, z0-1)
        elif branch_pos == 2:
            branches.append([x0-2,branch_height+1,z0-3])
            tree.palette.wood.place_block(interface, x0-2, branch_height+1, z0-3)
            tree.palette.wood.place_block(interface, x0-2, branch_height, z0-2)
            tree.palette.wood.place_block(interface, x0-1, branch_height, z0-1)
        elif branch_pos == 3:
            branches.append([x0-3,branch_height+1,z0-2])
            tree.palette.wood.place_block(interface, x0-3, branch_height+1, z0-2)
            tree.palette.wood.place_block(interface, x0-2, branch_height, z0-2)
            tree.palette.wood.place_block(interface, x0-1, branch_height, z0-1)
        branch_height = randint(height-5, height-2)
        branch_pos = randint(1, 3)
        if branch_pos == 1:
            branches.append([x0-3,branch_height+1,z0+3])
            tree.palette.wood.place_block(interface, x0-3, branch_height+1, z0+3)
            tree.palette.wood.place_block(interface, x0-2, branch_height, z0+2)
            tree.palette.wood.place_block(interface, x0-1, branch_height, z0+1)
        elif branch_pos == 2:
            branches.append([x0-2,branch_height+1,z0+3])
            tree.palette.wood.place_block(interface, x0-2, branch_height+1, z0+3)
            tree.palette.wood.place_block(interface, x0-2, branch_height, z0+2)
            tree.palette.wood.place_block(interface, x0-1, branch_height, z0+1)
        elif branch_pos == 3:
            branches.append([x0-3,branch_height+1,z0+2])
            tree.palette.wood.place_block(interface, x0-3, branch_height+1, z0+2)
            tree.palette.wood.place_block(interface, x0-2, branch_height, z0+2)
            tree.palette.wood.place_block(interface, x0-1, branch_height, z0+1)
        branch_height = randint(height-5, height-2)
        branch_pos = randint(1, 3)
        if branch_pos == 1:
            branches.append([x0+3,branch_height+1,z0+3])
            tree.palette.wood.place_block(interface, x0+3, branch_height+1, z0+3)
            tree.palette.wood.place_block(interface, x0+2, branch_height, z0+2)
            tree.palette.wood.place_block(interface, x0+1, branch_height, z0+1)
        elif branch_pos == 2:
            branches.append([x0+2,branch_height+1,z0+3])
            tree.palette.wood.place_block(interface, x0+2, branch_height+1, z0+3)
            tree.palette.wood.place_block(interface, x0+2, branch_height, z0+2)
            tree.palette.wood.place_block(interface, x0+1, branch_height, z0+1)
        elif branch_pos == 3:
            branches.append([x0+3,branch_height+1,z0+2])
            tree.palette.wood.place_block(interface, x0+3, branch_height+1, z0+2)
            tree.palette.wood.place_block(interface, x0+2, branch_height, z0+2)
            tree.palette.wood.place_block(interface, x0+1, branch_height, z0+1)
        branch_height = randint(height-5, height-2)
        branch_pos = randint(1, 3)
        if branch_pos == 1:
            branches.append([x0+3,branch_height+1,z0-3])
            tree.palette.wood.place_block(interface, x0+3, branch_height+1, z0-3)
            tree.palette.wood.place_block(interface, x0+2, branch_height, z0-2)
            tree.palette.wood.place_block(interface, x0+1, branch_height, z0-1)
        elif branch_pos == 2:
            branches.append([x0+2,branch_height+1,z0-3])
            tree.palette.wood.place_block(interface, x0+2, branch_height+1, z0-3)
            tree.palette.wood.place_block(interface, x0+2, branch_height, z0-2)
            tree.palette.wood.place_block(interface, x0+1, branch_height, z0-1)
        elif branch_pos == 3:
            branches.append([x0+3,branch_height+1,z0-2])
            tree.palette.wood.place_block(interface, x0+3, branch_height+1, z0-2)
            tree.palette.wood.place_block(interface, x0+2, branch_height, z0-2)
            tree.palette.wood.place_block(interface, x0+1, branch_height, z0-1)
        branch_height = randint(height-5, height-2)
        branch_pos = randint(1, 3)
        if branch_pos == 1:
            branches.append([x0-3,branch_height+1,z0-1])
            tree.palette.wood.place_block(interface, x0-3, branch_height+1, z0-1)
            tree.palette.wood.place_block(interface, x0-2, branch_height, z0-1)
            tree.palette.wood.place_block(interface, x0-1, branch_height, z0)
        elif branch_pos == 2:
            branches.append([x0-3,branch_height+1,z0])
            tree.palette.wood.place_block(interface, x0-3, branch_height+1, z0)
            tree.palette.wood.place_block(interface, x0-2, branch_height, z0)
            tree.palette.wood.place_block(interface, x0-1, branch_height, z0)
        elif branch_pos == 3:
            branches.append([x0-3,branch_height+1,z0+1])
            tree.palette.wood.place_block(interface, x0-3, branch_height+1, z0+1)
            tree.palette.wood.place_block(interface, x0-2, branch_height, z0+1)
            tree.palette.wood.place_block(interface, x0-1, branch_height, z0)
        branch_height = randint(height-5, height-2)
        branch_pos = randint(1, 3)
        if branch_pos == 1:
            branches.append([x0+3,branch_height+1,z0-1])
            tree.palette.wood.place_block(interface, x0+3, branch_height+1, z0-1)
            tree.palette.wood.place_block(interface, x0+2, branch_height, z0-1)
            tree.palette.wood.place_block(interface, x0+1, branch_height, z0)
        elif branch_pos == 2:
            branches.append([x0+3,branch_height+1,z0])
            tree.palette.wood.place_block(interface, x0+3, branch_height+1, z0)
            tree.palette.wood.place_block(interface, x0+2, branch_height, z0)
            tree.palette.wood.place_block(interface, x0+1, branch_height, z0)
        elif branch_pos == 3:
            branches.append([x0+3,branch_height+1,z0+1])
            tree.palette.wood.place_block(interface, x0+3, branch_height+1, z0+1)
            tree.palette.wood.place_block(interface, x0+2, branch_height, z0+1)
            tree.palette.wood.place_block(interface, x0+1, branch_height, z0)
        branch_height = randint(height-5, height-2)
        branch_pos = randint(1, 3)
        if branch_pos == 1:
            branches.append([x0-1,branch_height+1,z0-3])
            tree.palette.wood.place_block(interface, x0-1, branch_height+1, z0-3)
            tree.palette.wood.place_block(interface, x0-1, branch_height, z0-2)
            tree.palette.wood.place_block(interface, x0, branch_height, z0-1)
        elif branch_pos == 2:
            branches.append([x0,branch_height+1,z0-3])
            tree.palette.wood.place_block(interface, x0, branch_height+1, z0-3)
            tree.palette.wood.place_block(interface, x0, branch_height, z0-2)
            tree.palette.wood.place_block(interface, x0, branch_height, z0-1)
        elif branch_pos == 3:
            branches.append([x0+1,branch_height+1,z0-3])
            tree.palette.wood.place_block(interface, x0+1, branch_height+1, z0-3)
            tree.palette.wood.place_block(interface, x0+1, branch_height, z0-2)
            tree.palette.wood.place_block(interface, x0, branch_height, z0-1)
        branch_height = randint(height-5, height-2)
        branch_pos = randint(1, 3)
        if branch_pos == 1:
            branches.append([x0-1,branch_height+1,z0+3])
            tree.palette.wood.place_block(interface, x0-1, branch_height+1, z0+3)
            tree.palette.wood.place_block(interface, x0-1, branch_height, z0+2)
            tree.palette.wood.place_block(interface, x0, branch_height, z0+1)
        elif branch_pos == 2:
            branches.append([x0,branch_height+1,z0+3])
            tree.palette.wood.place_block(interface, x0, branch_height+1, z0+3)
            tree.palette.wood.place_block(interface, x0, branch_height, z0+2)
            tree.palette.wood.place_block(interface, x0, branch_height, z0+1)
        elif branch_pos == 3:
            branches.append([x0+1,branch_height+1,z0+3])
            tree.palette.wood.place_block(interface, x0+1, branch_height+1, z0+3)
            tree.palette.wood.place_block(interface, x0+1, branch_height, z0+2)
            tree.palette.wood.place_block(interface, x0, branch_height, z0+1)
        
        branch_num = randint(1,3)
        small_branches = []
        #small side branches
        for a in range (0, branch_num):
            branch_height = randint(int((height-y0)/2+y0), height-5)
            branch_pos = randint(1, 16)
            if branch_pos == 1:
                small_branches.append([x0+2,branch_height,z0])
                tree.palette.wood.place_block(interface, x0+2, branch_height, z0)
                tree.palette.wood.place_block(interface, x0+1, branch_height-1, z0)
            elif branch_pos == 2:
                small_branches.append([x0+2,branch_height,z0+1])
                tree.palette.wood.place_block(interface, x0+2,branch_height,z0+1)
                b = randint(1,2)
                if b==1:
                    tree.palette.wood.place_block(interface, x0+1,branch_height-1,z0+1)
                else:
                    tree.palette.wood.place_block(interface, x0+1,branch_height-1,z0)
            elif branch_pos == 3:
                small_branches.append([x0+2,branch_height,z0+2])
                tree.palette.wood.place_block(interface, x0+2,branch_height,z0+2)
                tree.palette.wood.place_block(interface, x0+1,branch_height-1,z0+1)
            elif branch_pos == 4:
                small_branches.append([x0+2,branch_height,z0-1])
                tree.palette.wood.place_block(interface, x0+2, branch_height, z0-1)
                b = randint(1,2)
                if b==1:
                    tree.palette.wood.place_block(interface, x0+1,branch_height-1,z0-1)
                else:
                    tree.palette.wood.place_block(interface, x0+1,branch_height-1,z0)
            elif branch_pos == 5:
                small_branches.append([x0+2,branch_height,z0-2])
                tree.palette.wood.place_block(interface, x0+2, branch_height, z0-2)
                tree.palette.wood.place_block(interface, x0+1,branch_height-1,z0-1)
            elif branch_pos == 6:
                small_branches.append([x0-2,branch_height,z0])
                tree.palette.wood.place_block(interface, x0-2, branch_height, z0)
                tree.palette.wood.place_block(interface, x0-1, branch_height-1, z0)
            elif branch_pos == 7:
                small_branches.append([x0-2,branch_height,z0+1])
                tree.palette.wood.place_block(interface, x0-2,branch_height,z0+1)
                b = randint(1,2)
                if b==1:
                    tree.palette.wood.place_block(interface, x0-1,branch_height-1,z0+1)
                else:
                    tree.palette.wood.place_block(interface, x0-1,branch_height-1,z0)
            elif branch_pos == 8:
                small_branches.append([x0-2,branch_height,z0+2])
                tree.palette.wood.place_block(interface, x0-2,branch_height,z0+2)
                tree.palette.wood.place_block(interface, x0-1,branch_height-1,z0+1)
            elif branch_pos == 9:
                small_branches.append([x0-2,branch_height,z0-1])
                tree.palette.wood.place_block(interface, x0-2, branch_height, z0-1)
                b = randint(1,2)
                if b==1:
                    tree.palette.wood.place_block(interface, x0-1,branch_height-1,z0-1)
                else:
                    tree.palette.wood.place_block(interface, x0-1,branch_height-1,z0)
            elif branch_pos == 10:
                small_branches.append([x0-2,branch_height,z0-2])
                tree.palette.wood.place_block(interface, x0-2, branch_height, z0-2)
                tree.palette.wood.place_block(interface, x0-1,branch_height-1,z0-1)
            elif branch_pos == 11:
                small_branches.append([x0+1,branch_height,z0-2])
                tree.palette.wood.place_block(interface, x0+1, branch_height, z0-2)
                b = randint(1,2)
                if b==1:
                    tree.palette.wood.place_block(interface, x0+1,branch_height-1,z0-1)
                else:
                    tree.palette.wood.place_block(interface, x0,branch_height-1,z0-1)
            elif branch_pos == 12:
                small_branches.append([x0,branch_height,z0-2])
                tree.palette.wood.place_block(interface, x0, branch_height, z0-2)
                tree.palette.wood.place_block(interface, x0, branch_height-1, z0-1)
            elif branch_pos == 13:
                small_branches.append([x0-1,branch_height,z0-2])
                tree.palette.wood.place_block(interface, x0-1, branch_height, z0-2)
                b = randint(1,2)
                if b==1:
                    tree.palette.wood.place_block(interface, x0-1,branch_height-1,z0-1)
                else:
                    tree.palette.wood.place_block(interface, x0,branch_height-1,z0-1)
            elif branch_pos == 14:
                small_branches.append([x0+1,branch_height,z0+2])
                tree.palette.wood.place_block(interface, x0+1, branch_height, z0+2)
                b = randint(1,2)
                if b==1:
                    tree.palette.wood.place_block(interface, x0+1,branch_height-1,z0+1)
                else:
                    tree.palette.wood.place_block(interface, x0,branch_height-1,z0+1)
            elif branch_pos == 15:
                small_branches.append([x0,branch_height,z0+2])
                tree.palette.wood.place_block(interface, x0, branch_height, z0+2)
                tree.palette.wood.place_block(interface, x0, branch_height-1, z0+1)
            elif branch_pos == 16:
                small_branches.append([x0-1,branch_height,z0+2])
                tree.palette.wood.place_block(interface, x0-1, branch_height, z0+2)
                b = randint(1,2)
                if b==1:
                    tree.palette.wood.place_block(interface, x0-1,branch_height-1,z0+1)
                else:
                    tree.palette.wood.place_block(interface, x0,branch_height-1,z0+1)

        for branch in branches:
            x1, y1, z1 = branch[0], branch[1], branch[2]

            tree.palette.leaves.place_block(interface, x1, y1+1, z1, leaf_chance)
            tree.palette.leaves.place_block(interface, x1+1, y1+1, z1, leaf_chance)
            tree.palette.leaves.place_block(interface, x1-1, y1+1, z1, leaf_chance)
            tree.palette.leaves.place_block(interface, x1, y1+1, z1+1, leaf_chance)
            tree.palette.leaves.place_block(interface, x1, y1+1, z1-1, leaf_chance)

            tree.palette.leaves.place_block(interface, x1+1, y1, z1+1, leaf_chance)
            tree.palette.leaves.place_block(interface, x1-1, y1, z1-1, leaf_chance)
            tree.palette.leaves.place_block(interface, x1-1, y1, z1+1, leaf_chance)
            tree.palette.leaves.place_block(interface, x1+1, y1, z1-1, leaf_chance)
            tree.palette.leaves.place_block(interface, x1+1, y1, z1, leaf_chance)
            tree.palette.leaves.place_block(interface, x1-1, y1, z1, leaf_chance)
            tree.palette.leaves.place_block(interface, x1, y1, z1+1, leaf_chance)
            tree.palette.leaves.place_block(interface, x1, y1, z1-1, leaf_chance)
            tree.palette.leaves.place_block(interface, x1+2, y1, z1, leaf_chance)
            tree.palette.leaves.place_block(interface, x1-2, y1, z1, leaf_chance)
            tree.palette.leaves.place_block(interface, x1, y1, z1+2, leaf_chance)
            tree.palette.leaves.place_block(interface, x1, y1, z1-2, leaf_chance)
            tree.palette.leaves.place_block(interface, x1+2, y1, z1+1, leaf_chance)
            tree.palette.leaves.place_block(interface, x1-2, y1, z1+1, leaf_chance)
            tree.palette.leaves.place_block(interface, x1+1, y1, z1+2, leaf_chance)
            tree.palette.leaves.place_block(interface, x1+1, y1, z1-2, leaf_chance)
            tree.palette.leaves.place_block(interface, x1+2, y1, z1-1, leaf_chance)
            tree.palette.leaves.place_block(interface, x1-2, y1, z1-1, leaf_chance)
            tree.palette.leaves.place_block(interface, x1-1, y1, z1+2, leaf_chance)
            tree.palette.leaves.place_block(interface, x1-1, y1, z1-2, leaf_chance)

        for branch in small_branches:
            x1, y1, z1 = branch[0], branch[1], branch[2]

            tree.palette.leaves.place_block(interface, x1, y1+1, z1, leaf_chance)
            tree.palette.leaves.place_block(interface, x1+1, y1+1, z1, leaf_chance)
            tree.palette.leaves.place_block(interface, x1-1, y1+1, z1, leaf_chance)
            tree.palette.leaves.place_block(interface, x1, y1+1, z1+1, leaf_chance)
            tree.palette.leaves.place_block(interface, x1, y1+1, z1-1, leaf_chance)

            tree.palette.leaves.place_block(interface, x1+1, y1, z1+1, leaf_chance)
            tree.palette.leaves.place_block(interface, x1-1, y1, z1-1, leaf_chance)
            tree.palette.leaves.place_block(interface, x1-1, y1, z1+1, leaf_chance)
            tree.palette.leaves.place_block(interface, x1+1, y1, z1-1, leaf_chance)
            tree.palette.leaves.place_block(interface, x1+1, y1, z1, leaf_chance)
            tree.palette.leaves.place_block(interface, x1-1, y1, z1, leaf_chance)
            tree.palette.leaves.place_block(interface, x1, y1, z1+1, leaf_chance)
            tree.palette.leaves.place_block(interface, x1, y1, z1-1, leaf_chance)
        
    def generate_large_jungle(self, tree, interface, leaf_chance: int=100):
        x0, y0, z0 = tree.get_origin()
        seed()
        height = randint(15,25)+y0
        branches = []
        
        for y in range (y0,height+1): #tree stem
            tree.palette.wood.place_block(interface, x0, y, z0)

        branches.append([x0, height, z0])

        # random branch generation, 1 random branch for each quadrant
        branch_height = randint(height-6, height-3)
        branch_pos = randint(1, 5)
        if branch_pos == 1:
            branches.append([x0-4,branch_height+2,z0-4])
            tree.palette.wood.place_block(interface, x0-4, branch_height+2, z0-4)
            tree.palette.wood.place_block(interface, x0-3, branch_height+1, z0-3)
            tree.palette.wood.place_block(interface, x0-2, branch_height, z0-2)
            tree.palette.wood.place_block(interface, x0-1, branch_height, z0-1)
        elif branch_pos == 2:
            branches.append([x0-3,branch_height+2,z0-4])
            tree.palette.wood.place_block(interface, x0-3, branch_height+2, z0-4)
            tree.palette.wood.place_block(interface, x0-3, branch_height+1, z0-3)
            tree.palette.wood.place_block(interface, x0-2, branch_height, z0-2)
            tree.palette.wood.place_block(interface, x0-1, branch_height, z0-1)
        elif branch_pos == 3:
            branches.append([x0-2,branch_height+2,z0-4])
            tree.palette.wood.place_block(interface, x0-2, branch_height+2, z0-4)
            tree.palette.wood.place_block(interface, x0-2, branch_height+1, z0-3)
            tree.palette.wood.place_block(interface, x0-1, branch_height, z0-2)
            tree.palette.wood.place_block(interface, x0-1, branch_height, z0-1)
        elif branch_pos == 4:
            branches.append([x0-4,branch_height+2,z0-3])
            tree.palette.wood.place_block(interface, x0-4, branch_height+2, z0-3)
            tree.palette.wood.place_block(interface, x0-3, branch_height+1, z0-3)
            tree.palette.wood.place_block(interface, x0-2, branch_height, z0-2)
            tree.palette.wood.place_block(interface, x0-1, branch_height, z0-1)
        elif branch_pos == 5:
            branches.append([x0-4,branch_height+2,z0-2])
            tree.palette.wood.place_block(interface, x0-4, branch_height+2, z0-2)
            tree.palette.wood.place_block(interface, x0-3, branch_height+1, z0-2)
            tree.palette.wood.place_block(interface, x0-2, branch_height, z0-1)
            tree.palette.wood.place_block(interface, x0-1, branch_height, z0-1)
        branch_height = randint(height-6, height-3)
        branch_pos = randint(1, 5)
        if branch_pos == 1:
            branches.append([x0+4,branch_height+2,z0-4])
            tree.palette.wood.place_block(interface, x0+4, branch_height+2, z0-4)
            tree.palette.wood.place_block(interface, x0+3, branch_height+1, z0-3)
            tree.palette.wood.place_block(interface, x0+2, branch_height, z0-2)
            tree.palette.wood.place_block(interface, x0+1, branch_height, z0-1)
        elif branch_pos == 2:
            branches.append([x0+3,branch_height+2,z0-4])
            tree.palette.wood.place_block(interface, x0+3, branch_height+2, z0-4)
            tree.palette.wood.place_block(interface, x0+3, branch_height+1, z0-3)
            tree.palette.wood.place_block(interface, x0+2, branch_height, z0-2)
            tree.palette.wood.place_block(interface, x0+1, branch_height, z0-1)
        elif branch_pos == 3:
            branches.append([x0+2,branch_height+2,z0-4])
            tree.palette.wood.place_block(interface, x0+2, branch_height+2, z0-4)
            tree.palette.wood.place_block(interface, x0+2, branch_height+1, z0-3)
            tree.palette.wood.place_block(interface, x0+1, branch_height, z0-2)
            tree.palette.wood.place_block(interface, x0+1, branch_height, z0-1)
        elif branch_pos == 4:
            branches.append([x0+4,branch_height+2,z0-3])
            tree.palette.wood.place_block(interface, x0+4, branch_height+2, z0-3)
            tree.palette.wood.place_block(interface, x0+3, branch_height+1, z0-3)
            tree.palette.wood.place_block(interface, x0+2, branch_height, z0-2)
            tree.palette.wood.place_block(interface, x0+1, branch_height, z0-1)
        elif branch_pos == 5:
            branches.append([x0+4,branch_height+2,z0-2])
            tree.palette.wood.place_block(interface, x0+4, branch_height+2, z0-2)
            tree.palette.wood.place_block(interface, x0+3, branch_height+1, z0-2)
            tree.palette.wood.place_block(interface, x0+2, branch_height, z0-1)
            tree.palette.wood.place_block(interface, x0+1, branch_height, z0-1)
        branch_height = randint(height-6, height-3)
        branch_pos = randint(1, 5)
        if branch_pos == 1:
            branches.append([x0-4,branch_height+2,z0+4])
            tree.palette.wood.place_block(interface, x0-4, branch_height+2, z0+4)
            tree.palette.wood.place_block(interface, x0-3, branch_height+1, z0+3)
            tree.palette.wood.place_block(interface, x0-2, branch_height, z0+2)
            tree.palette.wood.place_block(interface, x0-1, branch_height, z0+1)
        elif branch_pos == 2:
            branches.append([x0-3,branch_height+2,z0+4])
            tree.palette.wood.place_block(interface, x0-3, branch_height+2, z0+4)
            tree.palette.wood.place_block(interface, x0-3, branch_height+1, z0+3)
            tree.palette.wood.place_block(interface, x0-2, branch_height, z0+2)
            tree.palette.wood.place_block(interface, x0-1, branch_height, z0+1)
        elif branch_pos == 3:
            branches.append([x0-2,branch_height+2,z0+4])
            tree.palette.wood.place_block(interface, x0-2, branch_height+2, z0+4)
            tree.palette.wood.place_block(interface, x0-2, branch_height+1, z0+3)
            tree.palette.wood.place_block(interface, x0-1, branch_height, z0+2)
            tree.palette.wood.place_block(interface, x0-1, branch_height, z0+1)
        elif branch_pos == 4:
            branches.append([x0-4,branch_height+2,z0+3])
            tree.palette.wood.place_block(interface, x0-4, branch_height+2, z0+3)
            tree.palette.wood.place_block(interface, x0-3, branch_height+1, z0+3)
            tree.palette.wood.place_block(interface, x0-2, branch_height, z0+2)
            tree.palette.wood.place_block(interface, x0-1, branch_height, z0+1)
        elif branch_pos == 5:
            branches.append([x0-4,branch_height+2,z0+2])
            tree.palette.wood.place_block(interface, x0-4, branch_height+2, z0+2)
            tree.palette.wood.place_block(interface, x0-3, branch_height+1, z0+2)
            tree.palette.wood.place_block(interface, x0-2, branch_height, z0+1)
            tree.palette.wood.place_block(interface, x0-1, branch_height, z0+1)
        branch_height = randint(height-6, height-3)
        branch_pos = randint(1, 5)
        if branch_pos == 1:
            branches.append([x0+4,branch_height+2,z0+4])
            tree.palette.wood.place_block(interface, x0+4, branch_height+2, z0+4)
            tree.palette.wood.place_block(interface, x0+3, branch_height+1, z0+3)
            tree.palette.wood.place_block(interface, x0+2, branch_height, z0+2)
            tree.palette.wood.place_block(interface, x0+1, branch_height, z0+1)
        elif branch_pos == 2:
            branches.append([x0+3,branch_height+2,z0+4])
            tree.palette.wood.place_block(interface, x0+3, branch_height+2, z0+4)
            tree.palette.wood.place_block(interface, x0+3, branch_height+1, z0+3)
            tree.palette.wood.place_block(interface, x0+2, branch_height, z0+2)
            tree.palette.wood.place_block(interface, x0+1, branch_height, z0+1)
        elif branch_pos == 3:
            branches.append([x0+2,branch_height+2,z0+4])
            tree.palette.wood.place_block(interface, x0+2, branch_height+2, z0+4)
            tree.palette.wood.place_block(interface, x0+2, branch_height+1, z0+3)
            tree.palette.wood.place_block(interface, x0+1, branch_height, z0+2)
            tree.palette.wood.place_block(interface, x0+1, branch_height, z0+1)
        elif branch_pos == 4:
            branches.append([x0+4,branch_height+2,z0+3])
            tree.palette.wood.place_block(interface, x0+4, branch_height+2, z0+3)
            tree.palette.wood.place_block(interface, x0+3, branch_height+1, z0+3)
            tree.palette.wood.place_block(interface, x0+2, branch_height, z0+2)
            tree.palette.wood.place_block(interface, x0+1, branch_height, z0+1)
        elif branch_pos == 5:
            branches.append([x0+4,branch_height+2,z0+2])
            tree.palette.wood.place_block(interface, x0+4, branch_height+2, z0+2)
            tree.palette.wood.place_block(interface, x0+3, branch_height+1, z0+2)
            tree.palette.wood.place_block(interface, x0+2, branch_height, z0+1)
            tree.palette.wood.place_block(interface, x0+1, branch_height, z0+1)

        branch_height = randint(height-6, height-3)
        branch_pos = randint(1, 3)
        if branch_pos == 1:
            branches.append([x0-4,branch_height+2,z0-1])
            tree.palette.wood.place_block(interface, x0-4, branch_height+2, z0-1)
            tree.palette.wood.place_block(interface, x0-3, branch_height+1, z0-1)
            tree.palette.wood.place_block(interface, x0-2, branch_height, z0-1)
            tree.palette.wood.place_block(interface, x0-1, branch_height, z0)
        elif branch_pos == 2:
            branches.append([x0-4,branch_height+2,z0])
            tree.palette.wood.place_block(interface, x0-4, branch_height+2, z0)
            tree.palette.wood.place_block(interface, x0-3, branch_height+1, z0)
            tree.palette.wood.place_block(interface, x0-2, branch_height, z0)
            tree.palette.wood.place_block(interface, x0-1, branch_height, z0)
        elif branch_pos == 3:
            branches.append([x0-4,branch_height+2,z0+1])
            tree.palette.wood.place_block(interface, x0-4, branch_height+2, z0+1)
            tree.palette.wood.place_block(interface, x0-3, branch_height+1, z0+1)
            tree.palette.wood.place_block(interface, x0-2, branch_height, z0+1)
            tree.palette.wood.place_block(interface, x0-1, branch_height, z0)
        branch_height = randint(height-6, height-3)
        branch_pos = randint(1, 3)
        if branch_pos == 1:
            branches.append([x0+4,branch_height+2,z0-1])
            tree.palette.wood.place_block(interface, x0+4, branch_height+2, z0-1)
            tree.palette.wood.place_block(interface, x0+3, branch_height+1, z0-1)
            tree.palette.wood.place_block(interface, x0+2, branch_height, z0-1)
            tree.palette.wood.place_block(interface, x0+1, branch_height, z0)
        elif branch_pos == 2:
            branches.append([x0+4,branch_height+2,z0])
            tree.palette.wood.place_block(interface, x0+4, branch_height+2, z0)
            tree.palette.wood.place_block(interface, x0+3, branch_height+1, z0)
            tree.palette.wood.place_block(interface, x0+2, branch_height, z0)
            tree.palette.wood.place_block(interface, x0+1, branch_height, z0)
        elif branch_pos == 3:
            branches.append([x0+4,branch_height+2,z0+1])
            tree.palette.wood.place_block(interface, x0+4, branch_height+2, z0+1)
            tree.palette.wood.place_block(interface, x0+3, branch_height+1, z0+1)
            tree.palette.wood.place_block(interface, x0+2, branch_height, z0+1)
            tree.palette.wood.place_block(interface, x0+1, branch_height, z0)
        branch_height = randint(height-6, height-3)
        branch_pos = randint(1, 3)
        if branch_pos == 1:
            branches.append([x0-1,branch_height+2,z0+4])
            tree.palette.wood.place_block(interface, x0-1, branch_height+2, z0+4)
            tree.palette.wood.place_block(interface, x0-1, branch_height+1, z0+3)
            tree.palette.wood.place_block(interface, x0-1, branch_height, z0+2)
            tree.palette.wood.place_block(interface, x0, branch_height, z0+1)
        elif branch_pos == 2:
            branches.append([x0,branch_height+2,z0+4])
            tree.palette.wood.place_block(interface, x0, branch_height+2, z0+4)
            tree.palette.wood.place_block(interface, x0, branch_height+1, z0+3)
            tree.palette.wood.place_block(interface, x0, branch_height, z0+2)
            tree.palette.wood.place_block(interface, x0, branch_height, z0+1)
        elif branch_pos == 3:
            branches.append([x0+1,branch_height+2,z0+4])
            tree.palette.wood.place_block(interface, x0+1, branch_height+2, z0+4)
            tree.palette.wood.place_block(interface, x0+1, branch_height+1, z0+3)
            tree.palette.wood.place_block(interface, x0+1, branch_height, z0+2)
            tree.palette.wood.place_block(interface, x0, branch_height, z0+1)
        branch_height = randint(height-6, height-3)
        branch_pos = randint(1, 3)
        if branch_pos == 1:
            branches.append([x0-1,branch_height+2,z0-4])
            tree.palette.wood.place_block(interface, x0-1, branch_height+2, z0-4)
            tree.palette.wood.place_block(interface, x0-1, branch_height+1, z0-3)
            tree.palette.wood.place_block(interface, x0-1, branch_height, z0-2)
            tree.palette.wood.place_block(interface, x0, branch_height, z0-1)
        elif branch_pos == 2:
            branches.append([x0,branch_height+2,z0-4])
            tree.palette.wood.place_block(interface, x0, branch_height+2, z0-4)
            tree.palette.wood.place_block(interface, x0, branch_height+1, z0-3)
            tree.palette.wood.place_block(interface, x0, branch_height, z0-2)
            tree.palette.wood.place_block(interface, x0, branch_height, z0-1)
        elif branch_pos == 3:
            branches.append([x0+1,branch_height+2,z0-4])
            tree.palette.wood.place_block(interface, x0+1, branch_height+2, z0-4)
            tree.palette.wood.place_block(interface, x0+1, branch_height+1, z0-3)
            tree.palette.wood.place_block(interface, x0+1, branch_height, z0-2)
            tree.palette.wood.place_block(interface, x0, branch_height, z0-1)

        branch_num = randint(2,5)
        small_branches = []
        #small lower branches
        for a in range (0, branch_num):
            branch_height = randint(int((height-y0)/2+y0), height-7)
            branch_pos = randint(1, 24)
            if branch_pos == 1:
                small_branches.append([x0+3,branch_height,z0])
                tree.palette.wood.place_block(interface, x0+3, branch_height, z0)
                tree.palette.wood.place_block(interface, x0+2, branch_height-1, z0)
                tree.palette.wood.place_block(interface, x0+1, branch_height-1, z0)
            elif branch_pos == 2:
                small_branches.append([x0+3,branch_height,z0+1])
                tree.palette.wood.place_block(interface, x0+3,branch_height,z0+1)
                b = randint(1,2)
                if b==1:
                    tree.palette.wood.place_block(interface, x0+2,branch_height-1,z0+1)
                else:
                    tree.palette.wood.place_block(interface, x0+2,branch_height-1,z0)
                tree.palette.wood.place_block(interface, x0+1,branch_height-1,z0)
            elif branch_pos == 3:
                small_branches.append([x0+3,branch_height,z0+2])
                tree.palette.wood.place_block(interface, x0+3,branch_height,z0+2)
                b = randint(1,2)
                if b==1:
                    tree.palette.wood.place_block(interface, x0+2,branch_height-1,z0+1)
                else:
                    tree.palette.wood.place_block(interface, x0+2,branch_height-1,z0+2)
                tree.palette.wood.place_block(interface, x0+1,branch_height-1,z0+1)
            elif branch_pos == 4:
                small_branches.append([x0+3,branch_height,z0+3])
                tree.palette.wood.place_block(interface, x0+3, branch_height, z0+3)
                tree.palette.wood.place_block(interface, x0+2, branch_height-1, z0+2)
                tree.palette.wood.place_block(interface, x0+1, branch_height-1, z0+1)  
            elif branch_pos == 5:
                small_branches.append([x0+2,branch_height,z0+3])
                tree.palette.wood.place_block(interface, x0+2,branch_height,z0+3)
                b = randint(1,2)
                if b==1:
                    tree.palette.wood.place_block(interface, x0+2,branch_height-1,z0+2)
                else:
                    tree.palette.wood.place_block(interface, x0+1,branch_height-1,z0+2)
                tree.palette.wood.place_block(interface, x0+1,branch_height-1,z0+1)
            elif branch_pos == 6:
                small_branches.append([x0+1,branch_height,z0+3])
                tree.palette.wood.place_block(interface, x0+1,branch_height,z0+3)
                b = randint(1,2)
                if b==1:
                    tree.palette.wood.place_block(interface, x0+1,branch_height-1,z0+2)
                else:
                    tree.palette.wood.place_block(interface, x0,branch_height-1,z0+2)
                tree.palette.wood.place_block(interface, x0,branch_height-1,z0+1)
            elif branch_pos == 7:
                small_branches.append([x0,branch_height,z0+3])
                tree.palette.wood.place_block(interface, x0, branch_height, z0+3)
                tree.palette.wood.place_block(interface, x0, branch_height-1, z0+2)
                tree.palette.wood.place_block(interface, x0, branch_height-1, z0+1)
            elif branch_pos == 8:
                small_branches.append([x0-1,branch_height,z0+3])
                tree.palette.wood.place_block(interface, x0-1,branch_height,z0+3)
                b = randint(1,2)
                if b==1:
                    tree.palette.wood.place_block(interface, x0-1,branch_height-1,z0+2)
                else:
                    tree.palette.wood.place_block(interface, x0,branch_height-1,z0+2)
                tree.palette.wood.place_block(interface, x0,branch_height-1,z0+1)
            elif branch_pos == 9:
                small_branches.append([x0-2,branch_height,z0+3])
                tree.palette.wood.place_block(interface, x0-2,branch_height,z0+3)
                b = randint(1,2)
                if b==1:
                    tree.palette.wood.place_block(interface, x0-2,branch_height-1,z0+2)
                else:
                    tree.palette.wood.place_block(interface, x0-1,branch_height-1,z0+2)
                tree.palette.wood.place_block(interface, x0-1,branch_height-1,z0+1)
            elif branch_pos == 10:
                small_branches.append([x0-3,branch_height,z0+3])
                tree.palette.wood.place_block(interface, x0-3, branch_height, z0+3)
                tree.palette.wood.place_block(interface, x0-2, branch_height-1, z0+2)
                tree.palette.wood.place_block(interface, x0-1, branch_height-1, z0+1) 
            elif branch_pos == 11:
                small_branches.append([x0-3,branch_height,z0+2])
                tree.palette.wood.place_block(interface, x0-3,branch_height,z0+2)
                b = randint(1,2)
                if b==1:
                    tree.palette.wood.place_block(interface, x0-2,branch_height-1,z0+1)
                else:
                    tree.palette.wood.place_block(interface, x0-2,branch_height-1,z0+2)
                tree.palette.wood.place_block(interface, x0-1,branch_height-1,z0+1)
            elif branch_pos == 12:
                small_branches.append([x0-3,branch_height,z0+1])
                tree.palette.wood.place_block(interface, x0-3,branch_height,z0+1)
                b = randint(1,2)
                if b==1:
                    tree.palette.wood.place_block(interface, x0-2,branch_height-1,z0+1)
                else:
                    tree.palette.wood.place_block(interface, x0-2,branch_height-1,z0)
                tree.palette.wood.place_block(interface, x0-1,branch_height-1,z0)
            elif branch_pos == 13:
                small_branches.append([x0-3,branch_height,z0])
                tree.palette.wood.place_block(interface, x0-3, branch_height, z0)
                tree.palette.wood.place_block(interface, x0-2, branch_height-1, z0)
                tree.palette.wood.place_block(interface, x0-1, branch_height-1, z0)
            elif branch_pos == 14:
                small_branches.append([x0-3,branch_height,z0-1])
                tree.palette.wood.place_block(interface, x0-3,branch_height,z0-1)
                b = randint(1,2)
                if b==1:
                    tree.palette.wood.place_block(interface, x0-2,branch_height-1,z0-1)
                else:
                    tree.palette.wood.place_block(interface, x0-2,branch_height-1,z0)
                tree.palette.wood.place_block(interface, x0-1,branch_height-1,z0)
            elif branch_pos == 15:
                small_branches.append([x0-3,branch_height,z0-2])
                tree.palette.wood.place_block(interface, x0-3,branch_height,z0-2)
                b = randint(1,2)
                if b==1:
                    tree.palette.wood.place_block(interface, x0-2,branch_height-1,z0-1)
                else:
                    tree.palette.wood.place_block(interface, x0-2,branch_height-1,z0-2)
                tree.palette.wood.place_block(interface, x0-1,branch_height-1,z0-1)
            elif branch_pos == 16:
                small_branches.append([x0-3,branch_height,z0-3])
                tree.palette.wood.place_block(interface, x0-3, branch_height, z0-3)
                tree.palette.wood.place_block(interface, x0-2, branch_height-1, z0-2)
                tree.palette.wood.place_block(interface, x0-1, branch_height-1, z0-1) 
            elif branch_pos == 17:
                small_branches.append([x0-2,branch_height,z0-3])
                tree.palette.wood.place_block(interface, x0-2,branch_height,z0-3)
                b = randint(1,2)
                if b==1:
                    tree.palette.wood.place_block(interface, x0-2,branch_height-1,z0-2)
                else:
                    tree.palette.wood.place_block(interface, x0-1,branch_height-1,z0-2)
                tree.palette.wood.place_block(interface, x0-1,branch_height-1,z0-1)
            elif branch_pos == 18:
                small_branches.append([x0-1,branch_height,z0-3])
                tree.palette.wood.place_block(interface, x0-1,branch_height,z0-3)
                b = randint(1,2)
                if b==1:
                    tree.palette.wood.place_block(interface, x0-1,branch_height-1,z0-2)
                else:
                    tree.palette.wood.place_block(interface, x0,branch_height-1,z0-2)
                tree.palette.wood.place_block(interface, x0,branch_height-1,z0-1)
            elif branch_pos == 19:
                small_branches.append([x0,branch_height,z0-3])
                tree.palette.wood.place_block(interface, x0, branch_height, z0-3)
                tree.palette.wood.place_block(interface, x0, branch_height-1, z0-2)
                tree.palette.wood.place_block(interface, x0, branch_height-1, z0-1)
            elif branch_pos == 20:
                small_branches.append([x0+1,branch_height,z0-3])
                tree.palette.wood.place_block(interface, x0+1,branch_height,z0-3)
                b = randint(1,2)
                if b==1:
                    tree.palette.wood.place_block(interface, x0+1,branch_height-1,z0-2)
                else:
                    tree.palette.wood.place_block(interface, x0,branch_height-1,z0-2)
                tree.palette.wood.place_block(interface, x0,branch_height-1,z0-1)
            elif branch_pos == 21:
                small_branches.append([x0+2,branch_height,z0-3])
                tree.palette.wood.place_block(interface, x0+2,branch_height,z0-3)
                b = randint(1,2)
                if b==1:
                    tree.palette.wood.place_block(interface, x0+2,branch_height-1,z0-2)
                else:
                    tree.palette.wood.place_block(interface, x0+1,branch_height-1,z0-2)
                tree.palette.wood.place_block(interface, x0+1,branch_height-1,z0-1)
            elif branch_pos == 22:
                small_branches.append([x0+3,branch_height,z0-3])
                tree.palette.wood.place_block(interface, x0+3, branch_height, z0-3)
                tree.palette.wood.place_block(interface, x0+2, branch_height-1, z0-2)
                tree.palette.wood.place_block(interface, x0+1, branch_height-1, z0-1)
            elif branch_pos == 23:
                small_branches.append([x0+3,branch_height,z0-2])
                tree.palette.wood.place_block(interface, x0+3,branch_height,z0-2)
                b = randint(1,2)
                if b==1:
                    tree.palette.wood.place_block(interface, x0+2,branch_height-1,z0-1)
                else:
                    tree.palette.wood.place_block(interface, x0+2,branch_height-1,z0-2)
                tree.palette.wood.place_block(interface, x0+1,branch_height-1,z0-1)
            elif branch_pos == 24:
                small_branches.append([x0+3,branch_height,z0-1])
                tree.palette.wood.place_block(interface, x0+3,branch_height,z0-1)
                b = randint(1,2)
                if b==1:
                    tree.palette.wood.place_block(interface, x0+2,branch_height-1,z0-1)
                else:
                    tree.palette.wood.place_block(interface, x0+2,branch_height-1,z0)
                tree.palette.wood.place_block(interface, x0+1,branch_height-1,z0)

        for branch in branches:
            x1, y1, z1 = branch[0], branch[1], branch[2]

            tree.palette.leaves.place_block(interface, x1, y1+1, z1, leaf_chance)
            tree.palette.leaves.place_block(interface, x1+1, y1+1, z1, leaf_chance)
            tree.palette.leaves.place_block(interface, x1-1, y1+1, z1, leaf_chance)
            tree.palette.leaves.place_block(interface, x1, y1+1, z1+1, leaf_chance)
            tree.palette.leaves.place_block(interface, x1, y1+1, z1-1, leaf_chance)
            tree.palette.leaves.place_block(interface, x1+1, y1+1, z1+1, leaf_chance)
            tree.palette.leaves.place_block(interface, x1-1, y1+1, z1-1, leaf_chance)
            tree.palette.leaves.place_block(interface, x1-1, y1+1, z1+1, leaf_chance)
            tree.palette.leaves.place_block(interface, x1+1, y1+1, z1-1, leaf_chance)
            tree.palette.leaves.place_block(interface, x1+2, y1+1, z1, leaf_chance)
            tree.palette.leaves.place_block(interface, x1-2, y1+1, z1, leaf_chance)
            tree.palette.leaves.place_block(interface, x1, y1+1, z1+2, leaf_chance)
            tree.palette.leaves.place_block(interface, x1, y1+1, z1-2, leaf_chance)

            tree.palette.leaves.place_block(interface, x1+1, y1, z1+1, leaf_chance)
            tree.palette.leaves.place_block(interface, x1-1, y1, z1-1, leaf_chance)
            tree.palette.leaves.place_block(interface, x1-1, y1, z1+1, leaf_chance)
            tree.palette.leaves.place_block(interface, x1+1, y1, z1-1, leaf_chance)
            tree.palette.leaves.place_block(interface, x1+1, y1, z1, leaf_chance)
            tree.palette.leaves.place_block(interface, x1-1, y1, z1, leaf_chance)
            tree.palette.leaves.place_block(interface, x1, y1, z1+1, leaf_chance)
            tree.palette.leaves.place_block(interface, x1, y1, z1-1, leaf_chance)
            tree.palette.leaves.place_block(interface, x1+2, y1, z1, leaf_chance)
            tree.palette.leaves.place_block(interface, x1-2, y1, z1, leaf_chance)
            tree.palette.leaves.place_block(interface, x1, y1, z1+2, leaf_chance)
            tree.palette.leaves.place_block(interface, x1, y1, z1-2, leaf_chance)
            tree.palette.leaves.place_block(interface, x1+2, y1, z1+1, leaf_chance)
            tree.palette.leaves.place_block(interface, x1-2, y1, z1+1, leaf_chance)
            tree.palette.leaves.place_block(interface, x1+1, y1, z1+2, leaf_chance)
            tree.palette.leaves.place_block(interface, x1+1, y1, z1-2, leaf_chance)
            tree.palette.leaves.place_block(interface, x1+2, y1, z1-1, leaf_chance)
            tree.palette.leaves.place_block(interface, x1-2, y1, z1-1, leaf_chance)
            tree.palette.leaves.place_block(interface, x1-1, y1, z1+2, leaf_chance)
            tree.palette.leaves.place_block(interface, x1-1, y1, z1-2, leaf_chance)
            tree.palette.leaves.place_block(interface, x1+3, y1, z1, leaf_chance)
            tree.palette.leaves.place_block(interface, x1-3, y1, z1, leaf_chance)
            tree.palette.leaves.place_block(interface, x1, y1, z1+3, leaf_chance)
            tree.palette.leaves.place_block(interface, x1, y1, z1-3, leaf_chance)
            tree.palette.leaves.place_block(interface, x1+3, y1, z1+1, leaf_chance)
            tree.palette.leaves.place_block(interface, x1-3, y1, z1+1, leaf_chance)
            tree.palette.leaves.place_block(interface, x1+1, y1, z1+3, leaf_chance)
            tree.palette.leaves.place_block(interface, x1+1, y1, z1-3, leaf_chance)
            tree.palette.leaves.place_block(interface, x1+3, y1, z1-1, leaf_chance)
            tree.palette.leaves.place_block(interface, x1-3, y1, z1-1, leaf_chance)
            tree.palette.leaves.place_block(interface, x1-1, y1, z1+3, leaf_chance)
            tree.palette.leaves.place_block(interface, x1-1, y1, z1-3, leaf_chance)
            tree.palette.leaves.place_block(interface, x1+2, y1, z1+2, leaf_chance)
            tree.palette.leaves.place_block(interface, x1-2, y1, z1-2, leaf_chance)
            tree.palette.leaves.place_block(interface, x1-2, y1, z1+2, leaf_chance)
            tree.palette.leaves.place_block(interface, x1+2, y1, z1-2, leaf_chance)

        for branch in small_branches:
            x1, y1, z1 = branch[0], branch[1], branch[2]

            tree.palette.leaves.place_block(interface, x1, y1+1, z1, leaf_chance)
            tree.palette.leaves.place_block(interface, x1+1, y1+1, z1, leaf_chance)
            tree.palette.leaves.place_block(interface, x1-1, y1+1, z1, leaf_chance)
            tree.palette.leaves.place_block(interface, x1, y1+1, z1+1, leaf_chance)
            tree.palette.leaves.place_block(interface, x1, y1+1, z1-1, leaf_chance)

            tree.palette.leaves.place_block(interface, x1+1, y1, z1+1, leaf_chance)
            tree.palette.leaves.place_block(interface, x1-1, y1, z1-1, leaf_chance)
            tree.palette.leaves.place_block(interface, x1-1, y1, z1+1, leaf_chance)
            tree.palette.leaves.place_block(interface, x1+1, y1, z1-1, leaf_chance)
            tree.palette.leaves.place_block(interface, x1+1, y1, z1, leaf_chance)
            tree.palette.leaves.place_block(interface, x1-1, y1, z1, leaf_chance)
            tree.palette.leaves.place_block(interface, x1, y1, z1+1, leaf_chance)
            tree.palette.leaves.place_block(interface, x1, y1, z1-1, leaf_chance)
            tree.palette.leaves.place_block(interface, x1+2, y1, z1, leaf_chance)
            tree.palette.leaves.place_block(interface, x1-2, y1, z1, leaf_chance)
            tree.palette.leaves.place_block(interface, x1, y1, z1+2, leaf_chance)
            tree.palette.leaves.place_block(interface, x1, y1, z1-2, leaf_chance)
            tree.palette.leaves.place_block(interface, x1+2, y1, z1+1, leaf_chance)
            tree.palette.leaves.place_block(interface, x1-2, y1, z1+1, leaf_chance)
            tree.palette.leaves.place_block(interface, x1+1, y1, z1+2, leaf_chance)
            tree.palette.leaves.place_block(interface, x1+1, y1, z1-2, leaf_chance)
            tree.palette.leaves.place_block(interface, x1+2, y1, z1-1, leaf_chance)
            tree.palette.leaves.place_block(interface, x1-2, y1, z1-1, leaf_chance)
            tree.palette.leaves.place_block(interface, x1-1, y1, z1+2, leaf_chance)
            tree.palette.leaves.place_block(interface, x1-1, y1, z1-2, leaf_chance)
        
    def generate_mega_jungle(self, tree, interface, leaf_chance: int=100):
        self.generate_large_jungle(tree, interface, leaf_chance)
        x0, y0, z0 = tree.get_origin()
        new_tree = Tree((x0+1, y0, z0), tree.type)
        self.generate_large_jungle(new_tree, interface, leaf_chance)
        new_tree = Tree((x0+1, y0, z0+1), tree.type)
        self.generate_large_jungle(new_tree, interface, leaf_chance)
        new_tree = Tree((x0, y0, z0+1), tree.type)
        self.generate_large_jungle(new_tree, interface, leaf_chance)