from lib2to3.pgen2.pgen import generate_grammar
from generator import Generator
from market.stall import Stall
from gdpc.interface import Interface
from palette.block import Block
from palette.palette import WOOD, Palette
from palette.material import Material
from random import seed
from random import randint
from directions import Direction
from palette.sets.block_types import BLOCK, FENCE, FENCE_GATE, SLAB, STAIRS, TRAPDOOR

class StallGenerator(Generator):
    name = 'Stall Generator'
    stalls : Stall = []

    def __get_work_amount__(self) -> int:
        if self.stalls:
            return len(self.stalls)

    def __generate__(self, interface : Interface):
        if not self.stalls:
            return

        for stall in self.stalls:
            self.generate_stall(stall, interface)
            self.bar.next()

    def generate_stall(self, stall, interface):
        #dealing with directionality
        x0, y0, z0 = stall.get_origin()
        (swap, l0, l_dir, d0, d_dir) = self.setup_direction(stall)

        self.generate_base(stall, interface)
        self.generate_counter(stall, interface)
        self.generate_side(stall, interface)
        self.generate_roof(stall, interface)
        self.generate_overhang(stall, interface)
        if stall.back_counter:
            if swap:
                stall.set_origin((x0+(stall.depth-1)*d_dir,y0,z0+(stall.length-1)*l_dir))
            else:
                stall.set_origin((x0+(stall.length-1)*l_dir,y0,z0+(stall.depth-1)*d_dir))
            stall.set_direction(Direction.opposite[stall.direction])
            self.generate_counter(stall, interface)
            # reseting changes
            stall.set_origin((x0, y0, z0))
            stall.set_direction(Direction.opposite[stall.direction])
        if stall.goods!='none':
            self.generate_goods(stall, interface)
    
    def get_direction(self, direction):
        if direction == Direction.x_plus:
            return (-1,1)
        elif direction == Direction.x_minus:
            return (1,-1)
        elif direction == Direction.z_minus:
            return (1,1)
        elif direction == Direction.z_plus:
            return (-1,-1)

    def setup_direction(self, stall):
        x0, y0, z0 = stall.get_origin()
        (x_dir,z_dir) = self.get_direction(stall.direction)
        swap = (not x_dir==z_dir)
        if swap: #swapping length and depth to deal with east west directional stalls
            l0 = z0
            l_dir = z_dir
            d0 = x0
            d_dir = x_dir 
        else:
            l0 = x0
            l_dir = x_dir
            d0 = z0
            d_dir = z_dir 
        return (swap, l0, l_dir, d0, d_dir)

    def generate_base(self, stall, interface):
        x0, y0, z0 = stall.get_origin()
        (x_dir,z_dir) = self.get_direction(stall.direction)
        swap = (x_dir==z_dir)
        corners = []
        corners.append([x0,y0,z0])
        if swap:
            corners.append([x0+(stall.length-1)*x_dir,y0,z0])
            corners.append([x0,y0,z0+(stall.depth-1)*z_dir])
            corners.append([x0+(stall.length-1)*x_dir,y0,z0+(stall.depth-1)*z_dir])
            stall.add_floor_space((x0,y0,z0-z_dir))
            stall.add_floor_space((x0+(stall.length-1)*x_dir,y0,z0-z_dir))
        else:
            corners.append([x0+(stall.depth-1)*x_dir,y0,z0])
            corners.append([x0,y0,z0+(stall.length-1)*z_dir])
            corners.append([x0+(stall.depth-1)*x_dir,y0,z0+(stall.length-1)*z_dir])
            stall.add_floor_space((x0-x_dir,y0,z0))
            stall.add_floor_space((x0-x_dir,y0,z0+(stall.length-1)*z_dir))
        for corner in corners:
            stall.palette.get_material(WOOD, BLOCK).place_block(interface, corner[0], corner[1], corner[2])
            for a in range(corner[1]+1, corner[1]+stall.height-1):
                stall.palette.get_material(WOOD, FENCE).place_block(interface, corner[0], a, corner[2])

    def generate_counter(self, stall, interface):
        x0, y0, z0 = stall.get_origin()
        (swap, l0, l_dir, d0, d_dir) = self.setup_direction(stall)
        if stall.counter == 'basic':
            for a in range(l0+(1)*l_dir,l0+(stall.length-1)*l_dir, l_dir):
                if swap:
                    stall.palette.get_material(WOOD, BLOCK).place_block(interface, x0, y0, a)
                    stall.add_counter_space((x0,y0+1,a))
                else: 
                    stall.palette.get_material(WOOD, BLOCK).place_block(interface, a, y0, z0)
                    stall.add_counter_space((a,y0+1,z0))
        elif stall.counter == 'half_stair':
            if stall.length%2==0:
                for a in range(l0+(1)*l_dir,l0+(stall.length-1)*l_dir, l_dir):
                    if (a-l0)%2==0 and a<=stall.length-2:
                        if swap:
                            stall.palette.get_material(WOOD, BLOCK).place_block(interface, x0, y0, a)
                            stall.add_counter_space((x0,y0+1,a))
                        else: 
                            stall.palette.get_material(WOOD, BLOCK).place_block(interface, a, y0, z0)
                            stall.add_counter_space((a,y0+1,z0))
                    elif (a-l0)%2==1 and a>=stall.length-2:
                        if swap:
                            stall.palette.get_material(WOOD, BLOCK).place_block(interface, x0, y0, a)
                            stall.add_counter_space((x0,y0+1,a))
                        else: 
                            stall.palette.get_material(WOOD, BLOCK).place_block(interface, a, y0, z0)
                            stall.add_counter_space((a,y0+1,z0))
                    else:
                        if swap:
                            interface.placeBlock(x0, y0, a, f'{stall.palette.get_material(WOOD, STAIRS).block.name}[facing={Direction.cardinal_text[Direction.opposite[stall.direction]]}, half=top]')
                            stall.add_counter_space((x0,y0+1,a))
                        else:
                            interface.placeBlock(a, y0, z0, f'{stall.palette.get_material(WOOD, STAIRS).block.name}[facing={Direction.cardinal_text[Direction.opposite[stall.direction]]}, half=top]')
                            stall.add_counter_space((a,y0+1,z0))
            else:
                for a in range(l0+(1)*l_dir,l0+(stall.length-1)*l_dir, l_dir):
                    if (a-l0)%2==0:
                        if swap:
                            stall.palette.get_material(WOOD, BLOCK).place_block(interface, x0, y0, a)
                            stall.add_counter_space((x0,y0+1,a))
                        else: 
                            stall.palette.get_material(WOOD, BLOCK).place_block(interface, a, y0, z0)
                            stall.add_counter_space((a,y0+1,z0))
                    else:
                        if swap:
                            interface.placeBlock(x0, y0, a, f'{stall.palette.get_material(WOOD, STAIRS).block.name}[facing={Direction.cardinal_text[Direction.opposite[stall.direction]]}, half=top]')
                            stall.add_counter_space((x0,y0+1,a))
                        else:
                            interface.placeBlock(a, y0, z0, f'{stall.palette.get_material(WOOD, STAIRS).block.name}[facing={Direction.cardinal_text[Direction.opposite[stall.direction]]}, half=top]')
                            stall.add_counter_space((a,y0+1,z0))
        elif stall.counter == 'stair':
            for a in range(l0+(1)*l_dir,l0+(stall.length-1)*l_dir, l_dir):
                if swap:
                    interface.placeBlock(x0, y0, a, f'{stall.palette.get_material(WOOD, STAIRS).block.name}[facing={Direction.cardinal_text[Direction.opposite[stall.direction]]}, half=top]')
                    stall.add_counter_space((x0,y0+1,a))
                else:
                    interface.placeBlock(a, y0, z0, f'{stall.palette.get_material(WOOD, STAIRS).block.name}[facing={Direction.cardinal_text[Direction.opposite[stall.direction]]}, half=top]')
                    stall.add_counter_space((a,y0+1,z0))
        elif stall.counter == 'slab':
            for a in range(l0+(1)*l_dir,l0+(stall.length-1)*l_dir, l_dir):
                if swap:
                    stall.palette.get_material(WOOD, SLAB).place_block(interface, x0, y0, a, attributes={'type':'top'})
                    stall.add_counter_space((x0,y0+1,a))
                else:
                    stall.palette.get_material(WOOD, SLAB).place_block(interface, a, y0, z0, attributes={'type':'top'})
                    stall.add_counter_space((a,y0+1,z0))
        elif stall.counter == 'half_slab':
            if stall.length%2==0:
                for a in range(l0+(1)*l_dir,l0+(stall.length-1)*l_dir, l_dir):
                    if (a-l0)%2==0 and a<=stall.length-2:
                        if swap:
                            stall.palette.get_material(WOOD, BLOCK).place_block(interface, x0, y0, a)
                            stall.add_counter_space((x0,y0+1,a))
                        else: 
                            stall.palette.get_material(WOOD, BLOCK).place_block(interface, a, y0, z0)
                            stall.add_counter_space((a,y0+1,z0))
                    elif (a-l0)%2==1 and a>=stall.length-2:
                        if swap:
                            stall.palette.get_material(WOOD, BLOCK).place_block(interface, x0, y0, a)
                            stall.add_counter_space((x0,y0+1,a))
                        else: 
                            stall.palette.get_material(WOOD, BLOCK).place_block(interface, a, y0, z0)
                            stall.add_counter_space((a,y0+1,z0))
                    else:
                        if swap:
                            stall.palette.get_material(WOOD, SLAB).place_block(interface, x0, y0, a, attributes={'type':'top'})
                            stall.add_counter_space((x0,y0+1,a))
                        else:
                            stall.palette.get_material(WOOD, SLAB).place_block(interface, a, y0, z0, attributes={'type':'top'})
                            stall.add_counter_space((a,y0+1,z0))
            else:
                for a in range(l0+(1)*l_dir,l0+(stall.length-1)*l_dir, l_dir):
                    if (a-l0)%2==0:
                        if swap:
                            stall.palette.get_material(WOOD, BLOCK).place_block(interface, x0, y0, a)
                            stall.add_counter_space((x0,y0+1,a))
                        else: 
                            stall.palette.get_material(WOOD, BLOCK).place_block(interface, a, y0, z0)
                            stall.add_counter_space((a,y0+1,z0))
                    else:
                        if swap:
                            stall.palette.get_material(WOOD, SLAB).place_block(interface, x0, y0, a, attributes={'type':'top'})
                            stall.add_counter_space((x0,y0+1,a))
                        else:
                            stall.palette.get_material(WOOD, SLAB).place_block(interface, a, y0, z0, attributes={'type':'top'})
                            stall.add_counter_space((a,y0+1,z0))
        elif stall.counter == 'stair_slab':
            if stall.length%2==0:
                for a in range(l0+(1)*l_dir,l0+(stall.length-1)*l_dir, l_dir):
                    if (a-l0)%2==0 and a<=stall.length-2:
                        if swap:
                            interface.placeBlock(x0, y0, a, f'{stall.palette.get_material(WOOD, STAIRS).block.name}[facing={Direction.cardinal_text[Direction.opposite[stall.direction]]}, half=top]')
                            stall.add_counter_space((x0,y0+1,a))
                        else:
                            interface.placeBlock(a, y0, z0, f'{stall.palette.get_material(WOOD, STAIRS).block.name}[facing={Direction.cardinal_text[Direction.opposite[stall.direction]]}, half=top]')
                            stall.add_counter_space((a,y0+1,z0))
                    elif (a-l0)%2==1 and a>=stall.length-2:
                        if swap:
                            interface.placeBlock(x0, y0, a, f'{stall.palette.get_material(WOOD, STAIRS).block.name}[facing={Direction.cardinal_text[Direction.opposite[stall.direction]]}, half=top]')
                            stall.add_counter_space((x0,y0+1,a))
                        else:
                            interface.placeBlock(a, y0, z0, f'{stall.palette.get_material(WOOD, STAIRS).block.name}[facing={Direction.cardinal_text[Direction.opposite[stall.direction]]}, half=top]')
                            stall.add_counter_space((a,y0+1,z0))
                    else:
                        if swap:
                            stall.palette.get_material(WOOD, SLAB).place_block(interface, x0, y0, a, attributes={'type':'top'})
                            stall.add_counter_space((x0,y0+1,a))
                        else:
                            stall.palette.get_material(WOOD, SLAB).place_block(interface, a, y0, z0, attributes={'type':'top'})
                            stall.add_counter_space((a,y0+1,z0))
            else:
                for a in range(l0+(1)*l_dir,l0+(stall.length-1)*l_dir, l_dir):
                    if (a-l0)%2==0:
                        if swap:
                            interface.placeBlock(x0, y0, a, f'{stall.palette.get_material(WOOD, STAIRS).block.name}[facing={Direction.cardinal_text[Direction.opposite[stall.direction]]}, half=top]')
                            stall.add_counter_space((x0,y0+1,a))
                        else:
                            interface.placeBlock(a, y0, z0, f'{stall.palette.get_material(WOOD, STAIRS).block.name}[facing={Direction.cardinal_text[Direction.opposite[stall.direction]]}, half=top]')
                            stall.add_counter_space((a,y0+1,z0))
                    else:
                        if swap:
                            stall.palette.get_material(WOOD, SLAB).place_block(interface, x0, y0, a, attributes={'type':'top'})
                            stall.add_counter_space((x0,y0+1,a))
                        else:
                            stall.palette.get_material(WOOD, SLAB).place_block(interface, a, y0, z0, attributes={'type':'top'})
                            stall.add_counter_space((a,y0+1,z0))

    def generate_side(self, stall, interface):
        x0, y0, z0 = stall.get_origin()
        (swap, l0, l_dir, d0, d_dir) = self.setup_direction(stall)
        if stall.side == 'none':
            return
        elif stall.side == 'basic': 
            for a in range(d0+1*d_dir,d0+(stall.depth-1)*d_dir, d_dir):
                if swap:
                    stall.palette.get_material(WOOD, BLOCK).place_block(interface, a, y0, z0)
                    stall.palette.get_material(WOOD, BLOCK).place_block(interface, a, y0, z0+(stall.length-1)*l_dir)
                    stall.add_counter_space((a,y0+1,z0))
                    stall.add_counter_space((a,y0+1,z0+(stall.length-1)*l_dir))
                else:
                    stall.palette.get_material(WOOD, BLOCK).place_block(interface, x0, y0, a)
                    stall.palette.get_material(WOOD, BLOCK).place_block(interface, x0+(stall.length-1)*l_dir, y0, a)
                    stall.add_counter_space((x0,y0+1,a))
                    stall.add_counter_space((x0+(stall.length-1)*l_dir,y0+1,a))
        elif stall.side == 'fence': 
            for a in range(d0+1*d_dir,d0+(stall.depth-1)*d_dir, d_dir):
                if swap:
                    interface.placeBlock(a, y0, z0, f'{stall.palette.get_material(WOOD, FENCE).block.name}[{Direction.cardinal_text[Direction.opposite[stall.direction]]}=true,{Direction.cardinal_text[stall.direction]}=true]')
                    interface.placeBlock(a, y0, z0+(stall.length-1)*l_dir, f'{stall.palette.get_material(WOOD, FENCE).block.name}[{Direction.cardinal_text[Direction.opposite[stall.direction]]}=true,{Direction.cardinal_text[stall.direction]}=true]')
                else:
                    interface.placeBlock(x0, y0, a, f'{stall.palette.get_material(WOOD, FENCE).block.name}[{Direction.cardinal_text[Direction.opposite[stall.direction]]}=true,{Direction.cardinal_text[stall.direction]}=true]')
                    interface.placeBlock(x0+(stall.length-1)*l_dir, y0, a, f'{stall.palette.get_material(WOOD, FENCE).block.name}[{Direction.cardinal_text[Direction.opposite[stall.direction]]}=true,{Direction.cardinal_text[stall.direction]}=true]')
        elif stall.side == 'fence_gate': 
            for a in range(d0+1*d_dir,d0+(stall.depth-1)*d_dir, d_dir):
                if swap:
                    interface.placeBlock(a, y0, z0, f'{stall.palette.get_material(WOOD, FENCE_GATE).block.name}[facing={Direction.cardinal_text[Direction.right[stall.direction]]}]')
                    interface.placeBlock(a, y0, z0+(stall.length-1)*l_dir, f'{stall.palette.get_material(WOOD, FENCE_GATE).block.name}[facing={Direction.cardinal_text[Direction.left[stall.direction]]}]')
                else:
                    interface.placeBlock(x0, y0, a, f'{stall.palette.get_material(WOOD, FENCE_GATE).block.name}[facing={Direction.cardinal_text[Direction.right[stall.direction]]}]')
                    interface.placeBlock(x0+(stall.length-1)*l_dir, y0, a, f'{stall.palette.get_material(WOOD, FENCE_GATE).block.name}[facing={Direction.cardinal_text[Direction.left[stall.direction]]}]')
        elif stall.side == 'trapdoor':
            for a in range(d0+1*d_dir,d0+(stall.depth-1)*d_dir, d_dir):
                if swap:
                    interface.placeBlock(a, y0, z0, f'{stall.palette.get_material(WOOD, TRAPDOOR).block.name}[facing={Direction.cardinal_text[Direction.opposite[stall.direction]]}, half=top]')
                    interface.placeBlock(a, y0, z0+(stall.length-1)*l_dir, f'{stall.palette.get_material(WOOD, TRAPDOOR).block.name}[facing={Direction.cardinal_text[stall.direction]}, half=top]')
                else: 
                    interface.placeBlock(x0, y0, a, f'{stall.palette.get_material(WOOD, TRAPDOOR).block.name}[facing={Direction.cardinal_text[Direction.opposite[stall.direction]]}, half=top]')
                    interface.placeBlock(x0+(stall.length-1)*l_dir, y0, a, f'{stall.palette.get_material(WOOD, TRAPDOOR).block.name}[facing={Direction.cardinal_text[stall.direction]}, half=top]')
        elif stall.side == 'stair': 
            for a in range(d0+1*d_dir,d0+(stall.depth-1)*d_dir, d_dir):
                if swap:
                    interface.placeBlock(a, y0, z0, f'{stall.palette.get_material(WOOD, STAIRS).block.name}[facing={Direction.cardinal_text[Direction.right[stall.direction]]}, half=top]')
                    interface.placeBlock(a, y0, z0+(stall.length-1)*l_dir, f'{stall.palette.get_material(WOOD, STAIRS).block.name}[facing={Direction.cardinal_text[Direction.left[stall.direction]]}, half=top]')
                    stall.add_counter_space((a,y0+1,z0))
                    stall.add_counter_space((a,y0+1,z0+(stall.length-1)*l_dir))
                else:
                    interface.placeBlock(x0, y0, a, f'{stall.palette.get_material(WOOD, STAIRS).block.name}[facing={Direction.cardinal_text[Direction.right[stall.direction]]}, half=top]')
                    interface.placeBlock(x0+(stall.length-1)*l_dir, y0, a, f'{stall.palette.get_material(WOOD, STAIRS).block.name}[facing={Direction.cardinal_text[Direction.left[stall.direction]]}, half=top]')
                    stall.add_counter_space((x0,y0+1,a))
                    stall.add_counter_space((x0+(stall.length-1)*l_dir,y0+1,a))
        elif stall.side == 'slab': 
            for a in range(d0+1*d_dir,d0+(stall.depth-1)*d_dir, d_dir):
                if swap:
                    stall.palette.get_material(WOOD, SLAB).place_block(interface, a, y0, z0, attributes={'type':'top'})
                    stall.palette.get_material(WOOD, SLAB).place_block(interface, a, y0, z0+(stall.length-1)*l_dir, attributes={'type':'top'})
                    stall.add_counter_space((a,y0+1,z0))
                    stall.add_counter_space((a,y0+1,z0+(stall.length-1)*l_dir))
                else:
                    stall.palette.get_material(WOOD, SLAB).place_block(interface, x0, y0, a, attributes={'type':'top'})
                    stall.palette.get_material(WOOD, SLAB).place_block(interface, x0+(stall.length-1)*l_dir, y0, a, attributes={'type':'top'})
                    stall.add_counter_space((x0,y0+1,a))
                    stall.add_counter_space((x0+(stall.length-1)*l_dir,y0+1,a))

    def generate_roof(self, stall, interface):
        x0, y0, z0 = stall.get_origin()
        (swap, l0, l_dir, d0, d_dir) = self.setup_direction(stall)
        if stall.roof == 'basic':
            for a in range(l0,l0+stall.length*l_dir, l_dir):
                for b in range(d0,d0+stall.depth*d_dir, d_dir):
                    if (a-l0)%2==0:
                        if swap:
                            stall.palette.market_wool_1.place_block(interface, b, y0+stall.height-1, a)
                        else:
                            stall.palette.market_wool_1.place_block(interface, a, y0+stall.height-1, b)
                    else:
                        if swap:
                            stall.palette.market_wool_2.place_block(interface, b, y0+stall.height-1, a)
                        else:
                            stall.palette.market_wool_2.place_block(interface, a, y0+stall.height-1, b)
        elif stall.roof == 'back_down':
            for a in range(l0,l0+stall.length*l_dir, l_dir):
                for b in range(d0,d0+stall.depth*d_dir, d_dir):
                    if (a-l0)%2==0:
                        if b == (stall.depth-1)*l_dir:
                            if swap:
                                stall.palette.market_wool_1.place_block(interface, b, y0+stall.height-2, a)
                            else:
                                stall.palette.market_wool_1.place_block(interface, a, y0+stall.height-2, b)
                        else:
                            if swap:
                                stall.palette.market_wool_1.place_block(interface, b, y0+stall.height-1, a)
                            else:
                                stall.palette.market_wool_1.place_block(interface, a, y0+stall.height-1, b)
                    else:
                        if b == (stall.depth-1)*l_dir:
                            if swap:
                                stall.palette.market_wool_2.place_block(interface, b, y0+stall.height-2, a)
                            else:
                                stall.palette.market_wool_2.place_block(interface, a, y0+stall.height-2, b)
                        else:
                            if swap:
                                stall.palette.market_wool_2.place_block(interface, b, y0+stall.height-1, a)
                            else:
                                stall.palette.market_wool_2.place_block(interface, a, y0+stall.height-1, b)
        elif stall.roof == 'sides_down':
            for a in range(l0,l0+stall.length*l_dir, l_dir):
                for b in range(d0,d0+stall.depth*d_dir, d_dir):
                    if (a-l0)%2==0:
                        if a == l0+(stall.length-1)*l_dir or a==l0:
                            if swap:
                                stall.palette.market_wool_1.place_block(interface, b, y0+stall.height-2, a)
                            else:
                                stall.palette.market_wool_1.place_block(interface, a, y0+stall.height-2, b)
                        else:
                            if swap:
                                stall.palette.market_wool_1.place_block(interface, b, y0+stall.height-1, a)
                            else:
                                stall.palette.market_wool_1.place_block(interface, a, y0+stall.height-1, b)
                    else:
                        if a == l0+(stall.length-1)*l_dir or a==l0:
                            if swap:
                                stall.palette.market_wool_2.place_block(interface, b, y0+stall.height-2, a)
                            else:
                                stall.palette.market_wool_2.place_block(interface, a, y0+stall.height-2, b)
                        else:
                            if swap:
                                stall.palette.market_wool_2.place_block(interface, b, y0+stall.height-1, a)
                            else:
                                stall.palette.market_wool_2.place_block(interface, a, y0+stall.height-1, b)
        elif stall.roof == 'front_down':
            for a in range(l0,l0+stall.length*l_dir, l_dir):
                for b in range(d0,d0+stall.depth*d_dir, d_dir):
                    if (a-l0)%2==0:
                        if b==d0:
                            if swap:
                                stall.palette.market_wool_1.place_block(interface, b, y0+stall.height-2, a)
                            else:
                                stall.palette.market_wool_1.place_block(interface, a, y0+stall.height-2, b)
                        else:
                            if swap:
                                stall.palette.market_wool_1.place_block(interface, b, y0+stall.height-1, a)
                            else:
                                stall.palette.market_wool_1.place_block(interface, a, y0+stall.height-1, b)
                    else:
                        if b==d0:
                            if swap:
                                stall.palette.market_wool_2.place_block(interface, b, y0+stall.height-2, a)
                            else:
                                stall.palette.market_wool_2.place_block(interface, a, y0+stall.height-2, b)
                        else:
                            if swap:
                                stall.palette.market_wool_2.place_block(interface, b, y0+stall.height-1, a)
                            else:
                                stall.palette.market_wool_2.place_block(interface, a, y0+stall.height-1, b)
        elif stall.roof == 'front_back_down':
            for a in range(l0,l0+stall.length*l_dir, l_dir):
                for b in range(d0,d0+stall.depth*d_dir, d_dir):
                    if (a-l0)%2==0:
                        if b == d0+(stall.depth-1)*l_dir or b==d0:
                            if swap:
                                stall.palette.market_wool_1.place_block(interface, b, y0+stall.height-2, a)
                            else:
                                stall.palette.market_wool_1.place_block(interface, a, y0+stall.height-2, b)
                        else:
                            if swap:
                                stall.palette.market_wool_1.place_block(interface, b, y0+stall.height-1, a)
                            else:
                                stall.palette.market_wool_1.place_block(interface, a, y0+stall.height-1, b)
                    else:
                        if b == d0+(stall.depth-1)*l_dir or b==d0:
                            if swap:
                                stall.palette.market_wool_2.place_block(interface, b, y0+stall.height-2, a)
                            else:
                                stall.palette.market_wool_2.place_block(interface, a, y0+stall.height-2, b)
                        else:
                            if swap:
                                stall.palette.market_wool_2.place_block(interface, b, y0+stall.height-1, a)
                            else:
                                stall.palette.market_wool_2.place_block(interface, a, y0+stall.height-1, b)


    def generate_overhang(self, stall, interface):
        x0, y0, z0 = stall.get_origin()
        (swap, l0, l_dir, d0, d_dir) = self.setup_direction(stall)
        if stall.overhang == 'none':
            return
        elif stall.overhang == 'trapdoor':
            for a in range(l0,l0+stall.length*l_dir, l_dir):
                if stall.roof == 'front_back_down' or stall.roof == 'front_down' or (stall.roof == 'sides_down' and (a == l0 or a == l0+(stall.length-1)*l_dir)):
                    if swap:
                        interface.placeBlock(x0-1*d_dir, y0+stall.height-2, a, f'{stall.palette.get_material(WOOD, TRAPDOOR).block.name}[facing={Direction.cardinal_text[stall.direction]}]')
                    else:
                        interface.placeBlock(a, y0+stall.height-2, z0-1*d_dir, f'{stall.palette.get_material(WOOD, TRAPDOOR).block.name}[facing={Direction.cardinal_text[stall.direction]}]')
                else:
                    if swap:
                        interface.placeBlock(x0-1*d_dir, y0+stall.height-1, a, f'{stall.palette.get_material(WOOD, TRAPDOOR).block.name}[facing={Direction.cardinal_text[stall.direction]}]')
                    else:
                        interface.placeBlock(a, y0+stall.height-1, z0-1*d_dir, f'{stall.palette.get_material(WOOD, TRAPDOOR).block.name}[facing={Direction.cardinal_text[stall.direction]}]')
        elif stall.overhang == 'banner':
            for a in range(l0,l0+stall.length*l_dir, l_dir):
                if (a-x0)%2==0:
                    if stall.roof == 'front_back_down' or stall.roof == 'front_down' or (stall.roof == 'sides_down' and (a == l0 or a == l0+(stall.length-1)*l_dir)):
                        if swap:
                            interface.placeBlock(x0-1*d_dir, y0+stall.height-2, a, f'{stall.palette.market_banner_1.block.name}[facing={Direction.cardinal_text[stall.direction]}]')
                        else:
                            interface.placeBlock(a, y0+stall.height-2, z0-1*d_dir, f'{stall.palette.market_banner_1.block.name}[facing={Direction.cardinal_text[stall.direction]}]')
                    else:
                        if swap:
                            interface.placeBlock(x0-1*d_dir, y0+stall.height-1, a, f'{stall.palette.market_banner_1.block.name}[facing={Direction.cardinal_text[stall.direction]}]')
                        else:
                            interface.placeBlock(a, y0+stall.height-1, z0-1*d_dir, f'{stall.palette.market_banner_1.block.name}[facing={Direction.cardinal_text[stall.direction]}]')
                else:
                    if stall.roof == 'front_back_down' or stall.roof == 'front_down' or (stall.roof == 'sides_down' and (a == l0 or a == l0+(stall.length-1)*l_dir)):
                        if swap:
                            interface.placeBlock(x0-1*d_dir, y0+stall.height-2, a, f'{stall.palette.market_banner_2.block.name}[facing={Direction.cardinal_text[stall.direction]}]')
                        else:
                            interface.placeBlock(a, y0+stall.height-2, z0-1*d_dir, f'{stall.palette.market_banner_2.block.name}[facing={Direction.cardinal_text[stall.direction]}]')
                    else:
                        if swap:
                            interface.placeBlock(x0-1*d_dir, y0+stall.height-1, a, f'{stall.palette.market_banner_2.block.name}[facing={Direction.cardinal_text[stall.direction]}]')
                        else:
                            interface.placeBlock(a, y0+stall.height-1, z0-1*d_dir, f'{stall.palette.market_banner_2.block.name}[facing={Direction.cardinal_text[stall.direction]}]')
        elif stall.overhang == 'campfire':
            campfire_block = 'campfire[lit=false]'
            for a in range(l0,l0+stall.length*l_dir, l_dir):
                if stall.roof == 'front_back_down' or stall.roof == 'front_down' or (stall.roof == 'sides_down' and (a == l0 or a == l0+(stall.length-1)*l_dir)):
                    if swap:
                        interface.place_block(x0-1*d_dir, y0+stall.height-2, a, campfire_block)
                    else:
                        interface.place_block(a, y0+stall.height-2, z0-1*d_dir, campfire_block)
                else:
                    if swap:
                        interface.place_block(x0-1*d_dir, y0+stall.height-1, a, campfire_block)
                    else:
                        interface.place_block(a, y0+stall.height-1, z0-1*d_dir, campfire_block)

    def generate_goods(self, stall, interface):
        seed()
        for point in stall.counter_space:
            x, y, z = point
            generation_chance = randint(1, 4)
            if generation_chance < 4:
                good = stall.get_counter_good()
                if good.block.name[:11] == 'player_head': #player head direction
                    good.place_block(interface, x, y, z, stall.direction)
                else:
                    good.place_block(interface, x, y, z)
        
        if stall.has_floor_goods():
            for point in stall.floor_space:
                x, y, z = point
                generation_chance = randint(1, 4)
                if generation_chance < 4:
                    good = stall.get_floor_good()
                    if good.block.name == 'armor_stand': #armour stand rotation
                        good.place_block(interface, x, y, z, stall.direction)
                    else:
                        good.place_block(interface, x, y, z)