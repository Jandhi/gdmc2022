from gdpc.interface import Interface
from directions import Direction
from house.grid import GridNode
from house.roof.roof_design import RoofDesign

class BasicRoof(RoofDesign):
    def generate_roof(self, interface: Interface, node: GridNode):
        x0, y0, z0 = node.get_origin()
        x1, x2 = x0 + 1, x0 + node.width - 1
        z1, z2 = z0 + 1, z0 + node.depth - 1

        for x in range(x1, x2):
            for z in range(z1, z2):
                interface.placeBlock(x, y0 + node.height - 1, z, 'stripped_spruce_log')
        
        for direction in Direction.cardinal:
            if not node.get_neighbour(direction):
                self.generate_side(node, direction, interface)

    def generate_side(self, node : GridNode, direction, interface : Interface):
        points = node.get_side_points([direction, Direction.up])
        for i, (x, y, z) in enumerate(points):
            x0, y0, z0 = node.get_origin()

            position = min(i, len(points) - i - 1) # symmetry
            block = 'stripped_spruce_log'

            if position == 0:
                block = 'polished_andesite'
            elif position == (len(points) - 1) // 2:
                block = f'cobblestone_stairs[facing={Direction.cardinal_text[direction]}]'
            else:
                block = f'spruce_stairs[facing={Direction.cardinal_text[direction]}]'

            interface.placeBlock(x + x0, y + 1 + y0, z + z0, block)