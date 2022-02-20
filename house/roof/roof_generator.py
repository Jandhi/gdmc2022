from generator import Generator
from house.grid import Grid, GridNode
from directions import Direction

class RoofGenerator(Generator):
    name = 'Roof Generator'
    block = 'stripped_spruce_log'
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
        # should not generate for bottom nodes
        if node.get_neighbour(Direction.up):
            return

        x0, y0, z0 = node.get_origin()
        x1, x2 = x0 + 1, x0 + node.width - 1
        z1, z2 = z0 + 1, z0 + node.depth - 1

        for x in range(x1, x2):
            for z in range(z1, z2):
                self.interface.placeBlock(x, y0 + node.height - 1, z, self.block)
        
        for direction in Direction.cardinal:
            if not node.get_neighbour(direction):
                self.generate_side(node, direction)
    
    def generate_side(self, node : GridNode, direction):
        points = node.get_side_points([direction, Direction.up])
        for i, (x, y, z) in enumerate(points):
            x0, y0, z0 = node.get_origin()

            position = min(i, len(points) - i - 1) # symmetry
            block = self.block

            if position == 0:
                block = 'polished_andesite'
            elif position == (len(points) - 1) // 2:
                block = f'cobblestone_stairs[facing={Direction.text[direction]}]'
            else:
                block = f'spruce_stairs[facing={Direction.text[direction]}]'

            self.interface.placeBlock(x + x0, y + 1 + y0, z + z0, block)
