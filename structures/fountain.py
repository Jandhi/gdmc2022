from operator import ge
from stat import ST_INO
from statistics import geometric_mean
from directions import Direction
from palette.palette import STONE_ACCENT, Palette, WOOD
from noise.random import recursive_hash
from palette.sets.block_types import DECORATED, BLOCK, SLAB, STAIRS, TRAPDOOR, FENCE
from palette.sets.set_categories import STONE
from noise.random import choose
from structures.structure import LARGE, SMALL, Structure
from gdpc.interface import Interface
from vector import sum_vectors, multiply_vector
import numpy as np

from shapely.geometry import Point

class Fountain(Structure):
    palette: Palette
    dimensions = (19, 19)


    def __generate__(self, interface: Interface):
        x, z = self.origin
        y = self.y
        width, depth = self.dimensions

        cx, cz = x + width // 2, z + depth // 2
        cy = y - 1

        decorated = self.palette.get_material(STONE_ACCENT, DECORATED)

        
        material = self.palette.get_material(STONE, BLOCK)
        material.place_block(interface, cx, cy, cz)

        for i in [-1, 1]:
            for j in [-1, 1]:
                for dx in range(width):
                    for dz in range(depth):
                        px, pz = cx + dx * i, cz + dz * j
                        py = cy
                        if int(np.sqrt((px - cx)**2 + (pz - cz)**2)) <= 5:
                            material = self.palette.get_material(STONE, BLOCK)
                            material.place_block(interface, px, py, pz)




        for dir in Direction.cardinal:
            for sv in(Direction.vectors[Direction.right[dir]], Direction.vectors[Direction.left[dir]]):
                pv = Direction.vectors[dir]
                (px, py, pz) = sum_vectors((cx, cy, cz) , multiply_vector(pv, 6))

                material = self.palette.get_material(STONE_ACCENT, BLOCK)
                material.place_block(interface, px, py + 1, pz)
                self.palette.get_material(WOOD, TRAPDOOR).place_block(interface, px, py + 2, pz, attributes = {
                    'facing' : Direction.cardinal_text[dir],
                    'half' : 'bottom',
                    'open' : 'false'
                })

                self.palette.get_material(WOOD, TRAPDOOR).place_block(interface, *sum_vectors((px, py + 1, pz), pv), attributes = {
                    'facing' : Direction.cardinal_text[dir],
                    'half' : 'top',
                    'open' : 'true'
                })

                px,py,pz = sum_vectors((px, py, pz), sv)
                decorated.place_block(interface, px, py + 1, pz)

                px,py,pz = sum_vectors((px, py, pz), sv)
                attrs = {'facing' : Direction.cardinal_text[Direction.opposite[dir]], 'half' : 'top'}
                self.palette.get_material(STONE_ACCENT, STAIRS).place_block(interface, px, py + 1, pz, attributes = attrs)
                self.palette.get_material(STONE_ACCENT, SLAB).place_block(interface, px, py + 2, pz)

                for i in range(1, 3):
                    px,py,pz = sum_vectors((px, py, pz), sv)
                    material = self.palette.get_material(STONE, BLOCK)
                    material.place_block(interface, *sum_vectors((px, py + 1, pz), multiply_vector(pv, -1)))

                if sv == Direction.vectors[Direction.right[dir]]:
                    interface.placeBlock(*sum_vectors((px, py + 1, pz), multiply_vector(pv, -2)), 'grass_block')
                    interface.placeBlock(*sum_vectors((px, py + 2, pz), multiply_vector(pv, -2)), choose(recursive_hash(hash('fountain'), px, pz), ['red_tulip', 'orange_tulip', 'white_tulip', 'pink_tulip']))
                    
        # middle pillar

        for i in range(1, 9):
            material = self.palette.get_material(STONE_ACCENT, BLOCK)
            material.place_block(interface, cx, cy + i, cz)

            if i < 4:
                for dir in Direction.cardinal:
                    pv = Direction.vectors[dir]
                    (px, py, pz) = sum_vectors((cx, cy + i, cz) , multiply_vector(pv, 1))
                    material = self.palette.get_material(STONE, FENCE)
                    material.place_block(interface, px, py, pz)

            if i == 4:
                for dir in Direction.cardinal:
                    pv = Direction.vectors[dir]
                    sv = Direction.vectors[Direction.right[dir]]
                    px, py, pz = sum_vectors((cx, cy + i, cz) , multiply_vector(pv, 1))
                    interface.placeBlock(px, py, pz, 'grass_block')
                    px,py,pz = sum_vectors((px, py, pz), sv)
                    interface.placeBlock(px, py, pz, 'grass_block')
                    interface.placeBlock(px, py + 1, pz, 'rose_bush[half = lower]')
                    interface.placeBlock(px, py + 2, pz, 'rose_bush[half = upper]')
                    interface.placeBlock(px, py - 1, pz, 'lantern')

                    for sv in(Direction.vectors[Direction.right[dir]], Direction.vectors[Direction.left[dir]]):
                        px, py, pz = sum_vectors((cx, cy + i, cz) , multiply_vector(pv, 2))
                        decorated.place_block(interface, px, py, pz)
                        attrs = {'facing' : Direction.cardinal_text[Direction.opposite[dir]], 'half' : 'top'}
                        px,py,pz = sum_vectors((px, py, pz), sv)
                        self.palette.get_material(STONE_ACCENT, STAIRS).place_block(interface, px, py, pz, attributes = attrs)
                        self.palette.get_material(STONE_ACCENT, SLAB).place_block(interface, px, py + 1, pz)
            
            if i == 8:
                for dir in Direction.cardinal:
                    pv = Direction.vectors[dir]
                    px, py, pz = sum_vectors((cx, cy + i, cz) , multiply_vector(pv, 1))
                    attrs = {'facing' : Direction.cardinal_text[Direction.opposite[dir]], 'half' : 'top'}
                    self.palette.get_material(STONE_ACCENT, STAIRS).place_block(interface, px, py, pz, attributes = attrs)
                    sv = Direction.vectors[Direction.right[dir]]
                    px,py,pz = sum_vectors((px, py, pz), sv)
                    self.palette.get_material(STONE_ACCENT, SLAB).place_block(interface, px, py, pz, attributes = {'type' : 'top'})
                
                material = self.palette.get_material(STONE, FENCE)
                material.place_block(interface, cx, cy + i + 1, cz, attributes = {'waterlogged' : 'true'})

