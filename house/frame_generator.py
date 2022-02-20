from directions import Direction
from generator import Generator
from house.grid import Grid, GridNode
from palette.palette import Palette
from noise.random import hash_vector

class FrameGenerator(Generator):
    name = 'FrameGenerator'
    grid : Grid = None
    palette = Palette()

    def __get_work_amount__(self) -> int:
        if self.grid:
            return len(self.grid.nodes)

    def __generate__(self):
        if not self.grid:
            return
        
        for node in self.grid.nodes.values():
            self.generate_for_node(node)
            self.bar.next()

    def generate_for_node(self, node : GridNode):
        x0, y0, z0 = node.get_origin()

        # pillars
        for x in (0, node.width - 1):
            for y in range(node.height):
                for z in (0, node.depth - 1):
                    self.palette.frame.place_block(self.interface, hash_vector((x + x0, y + y0, z + z0)), x + x0, y + y0, z + z0, Direction.y_plus)
        
        # sides
        for x in (0, node.width - 1):
            for y in (0, node.height - 1):
                for z in range(1, node.depth - 1):
                    self.palette.frame.place_block(self.interface, hash_vector((x + x0, y + y0, z + z0)), x + x0, y + y0, z + z0, Direction.z_plus)
        
        for x in range(1, node.width - 1):
            for y in (0, node.height - 1):
                for z in (0, node.depth - 1):
                    self.palette.frame.place_block(self.interface, hash_vector((x + x0, y + y0, z + z0)), x + x0, y + y0, z + z0, Direction.x_plus)