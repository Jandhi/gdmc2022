from directions import Direction
from generator import Generator
from house.grid import BUILDING, Grid, GridNode
from gdpc.interface import Interface

from house.house import House
from palette.palette import FLOOR
from palette.sets.block_types import BLOCK

class FloorGenerator(Generator):
    name = 'Floor Generator'

    def __get_work_amount__(self) -> int:
        if self.house.grid:
            return len(self.house.grid.nodes)

    def __generate__(self, interface : Interface):
        if not self.house.grid:
            return
        
        for node in self.house.grid.nodes.values():
            if node.type != BUILDING:
                continue

            self.generate_for_node(node, interface)
            self.bar.next()

    def generate_for_node(self, node : GridNode, interface : Interface):
        x0, y0, z0 = node.get_origin()
        x1, x2 = x0 + 1, x0 + node.width - 1
        z1, z2 = z0 + 1, z0 + node.depth - 1

        if node.get_neighbour(Direction.x_plus):
            x2 += 1
        if node.get_neighbour(Direction.x_minus):
            x1 -= 1
        if node.get_neighbour(Direction.z_plus):
            z2 += 1
        if node.get_neighbour(Direction.z_minus):
            z1 -= 1

        for x in range(x1, x2):
            for z in range(z1, z2):
                node.palette.get_material(FLOOR, BLOCK).place_block(interface, x, y0, z)
        