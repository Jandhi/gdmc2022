from generator import Generator
from house.grid import Grid, GridNode
from directions import Direction
from gdpc.interface import Interface

class TowerRoofGenerator(Generator):
    name = 'Tower Roof Generator'
    node : GridNode = None
    y_offset = 0

    def __generate__(self, interface : Interface):
        if self.node:
            self.generate_for_node(self.node, interface)
    
    def generate_for_node(self, node : GridNode, interface : Interface):
        x0, y0, z0 = node.get_origin()
        tower_height = min(node.width, node.depth) // 2 + 1
        
        for y in range(0, tower_height):
            x1, x2 = y - 1, node.width - y
            z1, z2 = y - 1, node.depth - y

            for x in range(x1, x2 + 1):
                block = 'cobblestone_stairs' if x - x1 == (x2 - x1) // 2 else 'dark_oak_stairs'
                interface.placeBlock(x0 + x, y0 + self.y_offset + y, z0 + z1, f'{block}[facing={Direction.cardinal_text[Direction.z_plus]}]')
                interface.placeBlock(x0 + x, y0 + self.y_offset + y, z0 + z2, f'{block}[facing={Direction.cardinal_text[Direction.z_minus]}]')

            for z in range(z1, z2 + 1):
                block = 'cobblestone_stairs' if z - z1 == (z2 - z1) // 2 else 'dark_oak_stairs'
                interface.placeBlock(x0 + x1, y0 + self.y_offset + y, z0 + z, f'{block}[facing={Direction.cardinal_text[Direction.x_plus]}]')
                interface.placeBlock(x0 + x2, y0 + self.y_offset + y, z0 + z, f'{block}[facing={Direction.cardinal_text[Direction.x_minus]}]')