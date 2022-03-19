from directions import Axis, Direction
from house.roof.roof_design import RoofDesign
from gdpc.interface import Interface
from house.grid import GridNode

class SlantRoof(RoofDesign):
    def __init__(self, axis) -> None:
        self.axis = axis

    def generate_roof(self, interface: Interface, node: GridNode):
        direction = Direction.x_plus
        neighbours = node.get_neighbour_dict()
        
        if self.axis == Axis.Z:
            direction = Direction.z_plus
        
        low = Direction.left[direction]
        high = Direction.right[direction]

        if neighbours[low]:
            temp = low
            low = high
            high = temp
        
        x0, y0, z0 = node.get_origin()
        x1, x2 = 0, node.width
        z1, z2 = 0, node.depth

        if not neighbours[Direction.x_plus]:
            x2 += 1
        if not neighbours[Direction.x_minus]:
            x1 -= 1
        if not neighbours[Direction.z_plus]:
            z2 += 1
        if not neighbours[Direction.z_minus]:
            z1 -= 1
        
        for x in range(x1, x2):
            for z in range(z1, z2):
                y = node.height + 1

                if high == Direction.x_plus:
                    y += x
                if high == Direction.x_minus:
                    y += (x2 - 2) - x
                if high == Direction.z_plus:
                    y += z
                if high == Direction.z_minus:
                    y += (z2 - 2) - z

                on_x_edge = (not neighbours[Direction.x_plus] and x == node.width - 1) or (not neighbours[Direction.x_minus] and x == 0)
                on_z_edge = (not neighbours[Direction.z_plus] and z == node.depth - 1) or (not neighbours[Direction.z_minus] and z == 0)

                is_lowest = y == node.height
                is_highest = y == node.height + (node.width if self.axis == Axis.X else node.depth)

                if (self.axis == Axis.X and on_x_edge) or (self.axis == Axis.Z and on_z_edge):
                    for py in range(node.height, y):
                        node.palette.wall.place_block(interface, x0 + x, y0 + py, z0 + z)
                elif not (is_lowest or is_highest):
                    # lower stairs
                    node.palette.roof_stairs.place_block(interface, x0 + x, y0 + y - 1, z0 + z, attributes={
                        'facing' : Direction.cardinal_text[low],
                        'half' : 'top',
                    })
            
                if not is_highest:
                    # upper stairs
                    node.palette.roof_stairs.place_block(interface, x0 + x, y0 + y, z0 + z, attributes={
                        'facing' : Direction.cardinal_text[high]
                    })
                else:
                    # top slab
                    node.palette.roof_slab.place_block(interface, x0 + x, y0 + y, z0 + z)

                    # slab stairs
                    if self.axis == Axis.X and x == -1:
                        node.palette.roof_stairs.place_block(interface, x0 + x, y0 + y - 1, z0 + z, attributes={
                            'facing' : Direction.cardinal_text[Direction.x_plus],
                            'half' : 'top'
                        })
                    if self.axis == Axis.X and x == node.width:
                        node.palette.roof_stairs.place_block(interface, x0 + x, y0 + y - 1, z0 + z, attributes={
                            'facing' : Direction.cardinal_text[Direction.x_minus],
                            'half' : 'top'
                        })
                    if self.axis == Axis.Z and z == -1:
                        node.palette.roof_stairs.place_block(interface, x0 + x, y0 + y - 1, z0 + z, attributes={
                            'facing' : Direction.cardinal_text[Direction.z_plus],
                            'half' : 'top'
                        })
                    if self.axis == Axis.Z and z == node.depth:
                        node.palette.roof_stairs.place_block(interface, x0 + x, y0 + y - 1, z0 + z, attributes={
                            'facing' : Direction.cardinal_text[Direction.z_minus],
                            'half' : 'top'
                        })
                            




        

        


