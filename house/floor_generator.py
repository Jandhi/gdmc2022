from generator import Generator
from house.grid import Grid, GridNode

class FloorGenerator(Generator):
    name = 'Floor Generator'
    block = 'spruce_planks'
    grid : Grid = None

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
        x1, x2 = x0 + 1, x0 + node.width - 1
        z1, z2 = z0 + 1, z0 + node.depth - 1

        for x in range(x1, x2):
            for z in range(z1, z2):
                self.interface.placeBlock(x, y0, z, self.block)
        