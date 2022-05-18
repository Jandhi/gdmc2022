from generator import Generator
from house.grid import Grid, GridNode
from directions import Axis, Direction
from gdpc.interface import Interface

from house.house import House
from house.roof.basic_roof import BasicRoof
from house.roof.slant_roof import SlantRoof

class RoofGenerator(Generator):
    name = 'Roof Generator'

    def __get_work_amount__(self) -> int:
        if self.house.grid:
            return len(self.house.grid.nodes)

    def __generate__(self, interface : Interface):
        if not self.house.grid:
            return
        
        for node in self.house.grid.nodes.values():
            self.generate_for_node(node, interface)
            self.bar.next()

    def generate_for_node(self, node : GridNode, interface : Interface):
        # should not generate for bottom nodes
        if node.get_neighbour(Direction.up):
            return
        
        BasicRoof().generate_roof(interface, node)

        # SlantRoof(axis=Axis.X).generate_roof(interface, node)
    
    