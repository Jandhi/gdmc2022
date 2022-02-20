from directions import Direction
from house.walls.wall_design import BasicWall
from generator import Generator
from house.grid import Grid, GridNode

class WallGenerator(Generator):
    name = 'Wall Generator'
    grid : Grid = None
    design = None

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
        for direction in Direction.cardinal:
            if not node.get_neighbour(direction):
                if not self.design:
                    self.design = BasicWall()

                self.design.generate_wall(self.interface, node, direction)