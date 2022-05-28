from directions import Direction
from house.house import House
from generator import Generator
from house.grid import BUILDING, GridNode
from gdpc.interface import Interface
from noise.random import odds, recursive_hash
from palette.palette import WOOD_ACCENT
from palette.sets.block_types import FENCE, TRAPDOOR

from vector import sum_vectors

class WindowGenerator(Generator):
    name = 'Window Generator'
    house : House

    def __get_work_amount__(self) -> int:
        if self.house.grid:
            return len(self.house.grid.nodes)

    def __generate__(self, interface : Interface):
        if not self.house:
            return
        
        for node in self.house.grid.nodes.values():
            if node.type != BUILDING:
                continue

            self.generate_for_node(node, interface)
            self.bar.next()

    def generate_for_node(self, node : GridNode, interface : Interface):
        for direction in Direction.cardinal:
            if node.y > 0 and not node.get_neighbour(direction):
                x0, y0, z0 = node.get_origin()
                x = node.width // 2
                z = node.depth // 2

                if direction == Direction.x_plus:
                    x = node.width - 1
                elif direction == Direction.x_minus:
                    x = 0
                elif direction == Direction.z_plus:
                    z = node.depth - 1
                elif direction == Direction.z_minus:
                    z = 0

                node.palette.get_material(WOOD_ACCENT, FENCE).place_block(interface, x0 + x, y0 + 2, z0 + z)
                node.palette.get_material(WOOD_ACCENT, FENCE).place_block(interface, x0 + x, y0 + 3, z0 + z)

                px, py, pz = sum_vectors(
                    (x0 + x, y0, z0 + z), 
                    Direction.vectors[direction], 
                )

                # one in four is covered
                if odds(recursive_hash(hash('uncovered'), px, py, pz), 3, 4):
                    px, py, pz = sum_vectors(
                        (px, py, pz),
                        Direction.vectors[Direction.left[direction]]
                    )

                node.palette.get_material(WOOD_ACCENT, TRAPDOOR).place_block(interface, px, py + 2, pz, attributes={
                    'facing' : Direction.cardinal_text[direction],
                    'half' : 'bottom',
                    'open' : 'true'
                })
                node.palette.get_material(WOOD_ACCENT, TRAPDOOR).place_block(interface, px, py + 3, pz, attributes={
                    'facing' : Direction.cardinal_text[direction],
                    'half' : 'top',
                    'open' : 'true'
                })
                