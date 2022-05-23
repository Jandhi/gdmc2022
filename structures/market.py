
from directions import Direction
from structures.structure import MEDIUM, LARGE, Structure
from gdpc.interface import Interface
from market.stall_generator import StallGenerator
from market.stall import Stall

class Small_Market(Structure):
    name = 'Small Market'
    dimensions = MEDIUM

    def __generate__(self, interface: Interface):

        x, z = self.origin
        y = self.y
        width, depth = self.dimensions
        self.stalls = []
        self.stalls.append(Stall((x+9, y+1, z+4),'half_stair','trapdoor','sides_down','trapdoor','x_minus'))
        self.stalls.append(Stall((x+9, y+1, z+10),'half_stair','trapdoor','sides_down','trapdoor','x_minus'))
        self.stalls.append(Stall((x+9, y+1, z+16),'half_stair','trapdoor','sides_down','trapdoor','x_minus'))
        self.stalls.append(Stall((x+3, y+1, z),'half_stair','trapdoor','sides_down','trapdoor','x_plus'))
        self.stalls.append(Stall((x+3, y+1, z+6),'half_stair','trapdoor','sides_down','trapdoor','x_plus'))
        self.stalls.append(Stall((x+3, y+1, z+12),'half_stair','trapdoor','sides_down','trapdoor','x_plus'))
        
        StallGenerator(stalls=self.stalls).generate(interface)

class Market(Structure):
    name = 'Market'
    dimensions = LARGE

    def __generate__(self, interface: Interface):

        x, z = self.origin
        y = self.y
        width, depth = self.dimensions
        self.stalls = []
        self.stalls.append(Stall((x+5, y+1, z+4),'random','trapdoor','sides_down','trapdoor','z_plus'))
        self.stalls.append(Stall((x+15, y+1, z+4),'random','trapdoor','sides_down','trapdoor','z_plus', 7))
        self.stalls.append(Stall((x+23, y+1, z+4),'random','trapdoor','sides_down','trapdoor','z_plus'))

        self.stalls.append(Stall((x+1, y+1, z+28),'random','trapdoor','sides_down','trapdoor','z_minus'))
        self.stalls.append(Stall((x+9, y+1, z+28),'random','trapdoor','sides_down','trapdoor','z_minus', 7))
        self.stalls.append(Stall((x+19, y+1, z+28),'random','trapdoor','sides_down','trapdoor','z_minus'))

        self.stalls.append(Stall((x+14, y+1, z+11),'random','trapdoor','sides_down','trapdoor','x_minus'))
        self.stalls.append(Stall((x+14, y+1, z+19),'random','trapdoor','sides_down','trapdoor','x_minus', 7))
        self.stalls.append(Stall((x+14, y+1, z+25),'random','trapdoor','sides_down','trapdoor','x_minus'))
        self.stalls.append(Stall((x+20, y+1, z+11),'random','trapdoor','sides_down','trapdoor','x_minus'))
        self.stalls.append(Stall((x+20, y+1, z+19),'random','trapdoor','sides_down','trapdoor','x_minus', 7))
        self.stalls.append(Stall((x+20, y+1, z+25),'random','trapdoor','sides_down','trapdoor','x_minus'))

        self.stalls.append(Stall((x+4, y+1, z+7),'random','trapdoor','sides_down','trapdoor','x_plus'))
        self.stalls.append(Stall((x+4, y+1, z+13),'random','trapdoor','sides_down','trapdoor','x_plus', 7))
        self.stalls.append(Stall((x+4, y+1, z+21),'random','trapdoor','sides_down','trapdoor','x_plus'))
        self.stalls.append(Stall((x+10, y+1, z+7),'random','trapdoor','sides_down','trapdoor','x_plus'))
        self.stalls.append(Stall((x+10, y+1, z+13),'random','trapdoor','sides_down','trapdoor','x_plus', 7))
        self.stalls.append(Stall((x+10, y+1, z+21),'random','trapdoor','sides_down','trapdoor','x_plus'))
        
        StallGenerator(stalls=self.stalls).generate(interface)
