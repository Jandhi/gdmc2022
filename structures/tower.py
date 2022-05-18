
from directions import Direction
from structures.structure import SMALL, Structure
from gdpc.interface import Interface

class Tower(Structure):
    name = 'Tower'
    dimensions = SMALL
    tower_height = 20
    max_water = 1.1

    def __generate__(self, interface: Interface):

        x, z = self.origin
        y = self.y
        width, depth = self.dimensions

        cx, cz = x + 3, z + 3 

        # supports
        for dx, dz, dir in (
            (3, 0, Direction.x_plus),
            (0, 3, Direction.z_plus),
            (-3, 0, Direction.x_minus),
            (0, -3, Direction.z_minus)
        ):
            for dy in range(1, 9):
                block = 'stone_bricks'

                if dy == 1:
                    block = 'polished_andesite'
                elif dy == 8:
                    block = f'stone_brick_stairs[facing={Direction.cardinal_text[Direction.opposite[dir]]}]'

                interface.placeBlock(cx + dx, y + dy, cz + dz, block)

        # tube
        for dy in range(1, self.tower_height):
            for dx, dz in (
                (2, 1), (2, 0), (2, -1),
                (1, 2), (0, 2), (-1, 2),
                (-2, 1), (-2, 0), (-2, -1),
                (1, -2), (0, -2), (-1, -2)
            ):
                block = 'cobblestone'

                if dy % 7 == 1:
                    block = 'polished_andesite'
                elif dx == 0 or dz == 0:
                    block = 'stone_bricks'

                interface.placeBlock(cx + dx, y + dy, cz + dz, block)
        
        # bottom of flair
        for dx, dz, dir in (
            (3, 1, Direction.x_plus), (3, 0, Direction.x_plus), (3, -1, Direction.x_plus),
            (1, 3, Direction.z_plus), (0, 3, Direction.z_plus), (-1, 3, Direction.z_plus),
            (-3, 1, Direction.x_minus), (-3, 0, Direction.x_minus), (-3, -1, Direction.x_minus),
            (1, -3, Direction.z_minus), (0, -3, Direction.z_minus), (-1, -3, Direction.z_minus),
            (2, 2, None), (2, -2, None), (-2, 2, None), (-2, -2, None),
        ):
            if abs(dx) == 3 or abs(dz) == 3:
                block = 'cobblestone_stairs'
                
                if dx == 0 or dz == 0:
                    block = 'stone_brick_stairs'

                block += f'[facing={Direction.cardinal_text[Direction.opposite[dir]]},half=top]'

                interface.placeBlock(cx + dx, y + self.tower_height - 1, cz + dz, block)
            else:
                interface.placeBlock(cx + dx, y + self.tower_height - 1, cz + dz, 'cobblestone')

        # top of flair
        for dx, dz, dir in (
            (3, 1, Direction.x_plus), (3, 0, Direction.x_plus), (3, -1, Direction.x_plus),
            (1, 3, Direction.z_plus), (0, 3, Direction.z_plus), (-1, 3, Direction.z_plus),
            (-3, 1, Direction.x_minus), (-3, 0, Direction.x_minus), (-3, -1, Direction.x_minus),
            (1, -3, Direction.z_minus), (0, -3, Direction.z_minus), (-1, -3, Direction.z_minus),
            (2, 2, None), (2, -2, None), (-2, 2, None), (-2, -2, None),
        ):
            if abs(dx) == 3 or abs(dz) == 3:
                block = 'cobblestone'
                
                if dx == 0 or dz == 0:
                    block = 'stone_bricks'

                interface.placeBlock(cx + dx, y + self.tower_height, cz + dz, block)
            else:
                interface.placeBlock(cx + dx, y + self.tower_height, cz + dz, 'stone_bricks')

        # slabs
        for dx, dz, dir in (
            (3, 0, Direction.x_plus),
            (0, 3, Direction.z_plus),
            (-3, 0, Direction.x_minus),
            (0, -3, Direction.z_minus),
            (2, 2, None), (2, -2, None), (-2, 2, None), (-2, -2, None),
        ):
            interface.placeBlock(cx + dx, y + self.tower_height + 1, cz + dz, 'stone_brick_slab')