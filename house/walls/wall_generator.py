from directions import Direction
from house.house import House
from house.walls.pillars_generator import WallPillarDesign
from house.walls.wall_design import BasicWall, RecededWall
from generator import Generator
from house.grid import BUILDING, GridNode
from gdpc.interface import Interface

class WallGenerator(Generator):
    name = 'Wall Generator'
    house : House

    def __get_work_amount__(self) -> int:
        if self.house.grid:
            return len(self.house.grid.nodes)

    def __generate__(self, interface : Interface):
        if self.house is None:
            return
        
        for node in self.house.grid.nodes.values():
            if node.type != BUILDING:
                continue

            self.generate_for_node(node, interface)
            self.bar.next()

    def generate_for_node(self, node : GridNode, interface : Interface):
        for direction in Direction.cardinal:
            if not node.get_neighbour(direction):
                if self.house.has_receded_ground_floor and node.y == 0:
                    RecededWall().generate_wall(interface, node, direction)
                    WallPillarDesign().generate_wall(interface, node, direction)
                else:
                    BasicWall().generate_wall(interface, node, direction)
                