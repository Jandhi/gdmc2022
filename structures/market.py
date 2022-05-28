
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
        self.stalls.append(Stall(self.palette, (x+9, y, z+4),'half_stair','trapdoor','sides_down','trapdoor','x_minus'))
        self.stalls.append(Stall(self.palette, (x+9, y, z+10),'half_stair','trapdoor','sides_down','trapdoor','x_minus'))
        self.stalls.append(Stall(self.palette, (x+9, y, z+16),'half_stair','trapdoor','sides_down','trapdoor','x_minus'))
        self.stalls.append(Stall(self.palette, (x+3, y, z),'half_stair','trapdoor','sides_down','trapdoor','x_plus'))
        self.stalls.append(Stall(self.palette, (x+3, y, z+6),'half_stair','trapdoor','sides_down','trapdoor','x_plus'))
        self.stalls.append(Stall(self.palette, (x+3, y, z+12),'half_stair','trapdoor','sides_down','trapdoor','x_plus'))
        
        StallGenerator(stalls=self.stalls).generate(interface)

class Market(Structure):
    name = 'Market'
    dimensions = LARGE

    def __generate__(self, interface: Interface):

        x, z = self.origin
        y = self.y
        width, depth = self.dimensions
        self.stalls = []
        self.stalls.append(Stall(self.palette, (x+5, y, z+4),'random','trapdoor','sides_down','trapdoor','z_plus'))
        self.stalls.append(Stall(self.palette, (x+15, y, z+4),'random','trapdoor','sides_down','trapdoor','z_plus', 7))
        self.stalls.append(Stall(self.palette, (x+23, y, z+4),'random','trapdoor','sides_down','trapdoor','z_plus'))

        self.stalls.append(Stall(self.palette, (x+1, y, z+28),'random','trapdoor','sides_down','trapdoor','z_minus'))
        self.stalls.append(Stall(self.palette, (x+9, y, z+28),'random','trapdoor','sides_down','trapdoor','z_minus', 7))
        self.stalls.append(Stall(self.palette, (x+19, y, z+28),'random','trapdoor','sides_down','trapdoor','z_minus'))

        self.stalls.append(Stall(self.palette, (x+14, y, z+11),'random','trapdoor','sides_down','trapdoor','x_minus'))
        self.stalls.append(Stall(self.palette, (x+14, y, z+19),'random','trapdoor','sides_down','trapdoor','x_minus', 7))
        self.stalls.append(Stall(self.palette, (x+14, y, z+25),'random','trapdoor','sides_down','trapdoor','x_minus'))
        self.stalls.append(Stall(self.palette, (x+20, y, z+11),'random','trapdoor','sides_down','trapdoor','x_minus'))
        self.stalls.append(Stall(self.palette, (x+20, y, z+19),'random','trapdoor','sides_down','trapdoor','x_minus', 7))
        self.stalls.append(Stall(self.palette, (x+20, y, z+25),'random','trapdoor','sides_down','trapdoor','x_minus'))

        self.stalls.append(Stall(self.palette, (x+4, y, z+7),'random','trapdoor','sides_down','trapdoor','x_plus'))
        self.stalls.append(Stall(self.palette, (x+4, y, z+13),'random','trapdoor','sides_down','trapdoor','x_plus', 7))
        self.stalls.append(Stall(self.palette, (x+4, y, z+21),'random','trapdoor','sides_down','trapdoor','x_plus'))
        self.stalls.append(Stall(self.palette, (x+10, y, z+7),'random','trapdoor','sides_down','trapdoor','x_plus'))
        self.stalls.append(Stall(self.palette, (x+10, y, z+13),'random','trapdoor','sides_down','trapdoor','x_plus', 7))
        self.stalls.append(Stall(self.palette, (x+10, y, z+21),'random','trapdoor','sides_down','trapdoor','x_plus'))
        
        StallGenerator(stalls=self.stalls).generate(interface)
