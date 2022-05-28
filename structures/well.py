
from random import randint, seed
from directions import Direction
from palette.block import Block
from palette.material import BasicMaterial, SetBlockMaterial
from palette.palette import STONE_ACCENT, Palette
from palette.sets.block_types import DECORATED, BLOCK, FENCE, SLAB, STAIRS
from palette.sets.set_categories import STONE, WOOD, ROOF
from structures.structure import SMALL, Structure
from gdpc.interface import Interface

class Well(Structure):
    palette : Palette
    name = 'Well'
    dimensions = SMALL

    def __generate__(self, interface: Interface):

        x, z = self.origin
        y = self.y

        cx, cz = x + 3, z + 3
        
        #surrounding the water hole with wall
        for dx, dz in ((-1,0), (0,-1), (0,1), (1,0)):
            for dy in range(-2, 0):
                material = self.palette.get_material(STONE, BLOCK)
                material.place_block(interface, dx+cx, y + dy, dz+cz)

        #bottom block of well
        material = self.palette.get_material(STONE, BLOCK)
        material.place_block(interface, cx, y -3, cz)

        #well sides
        for dx, dz, dir in ((-1,0, Direction.x_minus), (0,-1, Direction.z_minus), (0,1, Direction.z_plus), 
            (1,0, Direction.x_plus), (1,1, Direction.x_plus), (1,-1, Direction.x_plus), 
            (-1,1, Direction.x_minus), (-1,-1, Direction.x_minus)
        ):
            material = self.palette.get_material(STONE, STAIRS)
            attrs = {'facing' : Direction.cardinal_text[dir], 'waterlogged' : 'true'}
            material.place_block(interface, dx+cx, y, dz+cz, attributes=attrs)

        #corners
        for dx, dz in ((1,1), (1,-1), (-1,1), (-1,-1)):
            for dy in range(1, 4):
                if dy == 3:
                    material = self.palette.get_material(STONE, BLOCK)
                else:
                    material = self.palette.get_material(STONE, FENCE)
                material.place_block(interface, dx+cx, y + dy, dz+cz)

        #add water
        for dy in range(-2, 1):
            material = BasicMaterial(Block('water'))
            material.place_block(interface, cx, y + dy, cz)

        #roof
        for dx, dz in (
                (2, 1), (2, -1),
                (1, 2),  (-1, 2),
                (-2, 1), (-2, -1),
                (1, -2), (-1, -2)
            ):
            material = self.palette.get_material(STONE, SLAB)
            material.place_block(interface, cx+dx, y+3, cz+dz)

        for dx, dz in ((-1,0), (0,-1), (0,1), (1,0)):
            material = self.palette.get_material(STONE, SLAB)
            attrs = {'type' : 'top'}
            material.place_block(interface, cx+dx, y+3, cz+dz, attributes=attrs)

        material = self.palette.get_material(STONE, SLAB)
        material.place_block(interface, cx, y+4, cz)

        for dx, dz, dir in (
            (2, 0, Direction.x_plus), (0, 2, Direction.z_plus), (-2, 0, Direction.x_minus), (0, -2, Direction.z_minus)
            ):
            material = self.palette.get_material(STONE, STAIRS)
            attrs = {'facing' : Direction.cardinal_text[Direction.opposite[dir]]}
            material.place_block(interface, dx+cx, y + 3, dz+cz, attributes=attrs)

        #chain and bucket
        material = BasicMaterial(Block('chain'))
        material.place_block(interface, cx, y + 2, cz)
        material.place_block(interface, cx, y + 3, cz)
        material = BasicMaterial(Block('cauldron'))
        seed()
        a = randint(0,3)
        attrs = {'level' : f'{a}'}
        material.place_block(interface, cx, y + 1, cz, attributes=attrs)

        #random bucket
        seed()
        a = 1
        if a==1:
            pos = randint(0,15)
            places = [(2, 1), (2, 0), (2, -1), (2, 2), 
                (1, 2), (0, 2), (-1, 2), (2, -2), 
                (-2, 1), (-2, 0), (-2, -1), (-2, 2), 
                (1, -2), (0, -2), (-1, -2), (-2, -2)]
            dx, dz = places[pos]
            material = SetBlockMaterial(Block('player_head{SkullOwner:{Id:[I;-1748225354,-1609481680,-1708141395,1310692466],Properties:{textures:[{Value:"eyJ0ZXh0dXJlcyI6eyJTS0lOIjp7InVybCI6Imh0dHA6Ly90ZXh0dXJlcy5taW5lY3JhZnQubmV0L3RleHR1cmUvNjAyYzk5Y2I5NjY3NDZiMGUzZDE2OTczZmMyY2RjZTRlNDBiODdhODZjMDVlMGE1MDIxZjM1YTAxOTJhNDBiMiJ9fX0="}]}}}'))
            material.place_block(interface, cx+dx, y, cz+dz)