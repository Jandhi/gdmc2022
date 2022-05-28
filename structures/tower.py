
from directions import Direction
from palette.palette import STONE_ACCENT, Palette
from palette.sets.block_types import DECORATED, BLOCK, SLAB, STAIRS
from palette.sets.set_categories import STONE
from structures.structure import SMALL, Structure
from gdpc.interface import Interface

class Tower(Structure):
    palette : Palette
    name = 'Tower'
    dimensions = SMALL
    tower_height = 20
    max_water = 1.1

    def __generate__(self, interface: Interface):
        x, z = self.origin
        y = self.y
        width, depth = self.dimensions

        cx, cz = x + width//2, z + depth//2 

        # supports
        for dx, dz, dir in (
            (3, 0, Direction.x_plus),
            (0, 3, Direction.z_plus),
            (-3, 0, Direction.x_minus),
            (0, -3, Direction.z_minus)
        ):
            for dy in range(1, 9):
                material = self.palette.get_material(STONE_ACCENT, BLOCK)
                attrs = {}

                if dy == 1:
                    material = self.palette.get_material(STONE, DECORATED)
                elif dy == 8:
                    material = self.palette.get_material(STONE_ACCENT, STAIRS)
                    attrs = {'facing' : Direction.cardinal_text[Direction.opposite[dir]]}

                material.place_block(interface, cx + dx, y + dy, cz + dz, attributes=attrs)

        # tube
        for dy in range(1, self.tower_height):
            for dx, dz in (
                (2, 1), (2, 0), (2, -1),
                (1, 2), (0, 2), (-1, 2),
                (-2, 1), (-2, 0), (-2, -1),
                (1, -2), (0, -2), (-1, -2)
            ):
                material = self.palette.get_material(STONE, BLOCK)

                if dy % 7 == 1:
                    material = self.palette.get_material(STONE, DECORATED)
                elif dx == 0 or dz == 0:
                    material = self.palette.get_material(STONE_ACCENT, BLOCK)

                material.place_block(interface, cx + dx, y + dy, cz + dz)
        
        # bottom of flair
        for dx, dz, dir in (
            (3, 1, Direction.x_plus), (3, 0, Direction.x_plus), (3, -1, Direction.x_plus),
            (1, 3, Direction.z_plus), (0, 3, Direction.z_plus), (-1, 3, Direction.z_plus),
            (-3, 1, Direction.x_minus), (-3, 0, Direction.x_minus), (-3, -1, Direction.x_minus),
            (1, -3, Direction.z_minus), (0, -3, Direction.z_minus), (-1, -3, Direction.z_minus),
            (2, 2, None), (2, -2, None), (-2, 2, None), (-2, -2, None),
        ):
            if abs(dx) == 3 or abs(dz) == 3:
                material = self.palette.get_material(STONE, STAIRS)
                
                if dx == 0 or dz == 0:
                    material = self.palette.get_material(STONE_ACCENT, STAIRS)

                attrs = {'facing' : Direction.cardinal_text[Direction.opposite[dir]], 'half' : 'top'}

                material.place_block(interface, cx + dx, y + self.tower_height - 1, cz + dz, attributes=attrs)
            else:
                self.palette.get_material(STONE, BLOCK).place_block(interface, cx + dx, y + self.tower_height - 1, cz + dz)

        # top of flair
        for dx, dz, dir in (
            (3, 1, Direction.x_plus), (3, 0, Direction.x_plus), (3, -1, Direction.x_plus),
            (1, 3, Direction.z_plus), (0, 3, Direction.z_plus), (-1, 3, Direction.z_plus),
            (-3, 1, Direction.x_minus), (-3, 0, Direction.x_minus), (-3, -1, Direction.x_minus),
            (1, -3, Direction.z_minus), (0, -3, Direction.z_minus), (-1, -3, Direction.z_minus),
            (2, 2, None), (2, -2, None), (-2, 2, None), (-2, -2, None),
        ):
            if abs(dx) == 3 or abs(dz) == 3:
                material = self.palette.get_material(STONE, BLOCK)
                
                if dx == 0 or dz == 0:
                    material = self.palette.get_material(STONE_ACCENT, BLOCK)

                material.place_block(interface, cx + dx, y + self.tower_height, cz + dz)
            else:
                self.palette.get_material(STONE_ACCENT, BLOCK).place_block(interface, cx + dx, y + self.tower_height, cz + dz)

        # slabs
        for dx, dz, dir in (
            (3, 0, Direction.x_plus),
            (0, 3, Direction.z_plus),
            (-3, 0, Direction.x_minus),
            (0, -3, Direction.z_minus),
            (2, 2, None), (2, -2, None), (-2, 2, None), (-2, -2, None),
        ):
            self.palette.get_material(STONE_ACCENT, SLAB).place_block(interface, cx + dx, y + self.tower_height + 1, cz + dz)