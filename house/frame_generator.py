from directions import Direction
from generator import Generator
from house.grid import Grid, GridNode
from gdpc.interface import Interface

class FrameGenerator(Generator):
    name = 'FrameGenerator'
    grid : Grid = None

    def __get_work_amount__(self) -> int:
        if self.house.grid:
            return len(self.house.grid.nodes)

    def __generate__(self, interface : Interface):
        if not self.house:
            return
        
        for node in self.house.grid.nodes.values():
            self.generate_for_node(node, interface)
            self.bar.next()

    def generate_for_node(self, node : GridNode, interface : Interface):
        x0, y0, z0 = node.get_origin()

        # pillars
        for x in (0, node.width - 1):
            for y in range(node.height):
                for z in (0, node.depth - 1):
                    node.palette.frame.place_block(interface, x + x0, y + y0, z + z0, Direction.y_plus)
        
        # sides
        for x in (0, node.width - 1):
            for y in (0, node.height - 1):
                for z in range(1, node.depth - 1):
                    node.palette.frame.place_block(interface, x + x0, y + y0, z + z0, Direction.z_plus)
        
        for x in range(1, node.width - 1):
            for y in (0, node.height - 1):
                for z in (0, node.depth - 1):
                    node.palette.frame.place_block(interface, x + x0, y + y0, z + z0, Direction.x_plus)