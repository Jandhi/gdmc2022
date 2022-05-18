from directions import Direction
from noise.noise import shuffle
from noise.random import recursive_hash
from structures.structure import dimensions as dimensions_list, structures_by_dim
from generator import Generator
from gdpc.interface import Interface
from structures.load_structures import load_structures

from terrain.buildmap import NOTHING, STRUCTURE

DEBUG_GROUND = True

load_structures()

class StructurePlacer(Generator):
    name = 'Structure Placer'

    def __init__(self, **kwargs) -> None:
        super().__init__(**kwargs)

    def __generate__(self, interface: Interface):
        self.attempt_placement(self.point, interface)

    def attempt_placement(self, point, interface):
        x, z = point
        y = self.hmap[x][z] - 1
        for direction in shuffle(recursive_hash(*point), list(Direction.cardinal)):

            # largest first
            for dms in dimensions_list[::-1]:
                origin = get_origin(point, direction, dms)

                if not is_in_bounds(origin, dms, self.hmap):
                    continue

                if is_blocked(origin, dms, self.bmap):
                    continue
                
                roughness = get_average_roughness(origin, y, dms, self.hmap)
                water_amount = get_water_amount(origin, dms, self.wmap)

                for structure in shuffle(recursive_hash(*point, hash('structures')), structures_by_dim[dms]):
                    if roughness > structure.max_roughness or water_amount > structure.max_water:
                        continue

                    
                    for dx in range(dms[0]):
                        for dz in range(dms[1]):
                            px = origin[0] + dx
                            pz = origin[1] + dz
                            self.bmap[px][pz] = STRUCTURE

                            if DEBUG_GROUND:
                                interface.placeBlock(px, y, pz, 'warped_planks')
                    
                    structure(
                        origin=origin,
                        y=y,
                        area=self.area, 
                        hmap=self.hmap, 
                        wmap=self.wmap,
                        bmap=self.bmap,
                        slice=self.slice,
                    ).generate(interface)

                    return


def get_origin(road_point, direction, dimensions):
    x, z = road_point
    dx, dz = dimensions

    return {
        Direction.x_plus  : (x + 1, z - dz//2),
        Direction.x_minus : (x - dx, z - dz//2),
        Direction.z_plus  : (x - dx//2, z + 1),
        Direction.z_minus : (x - dx//2, z - dz),
    }[direction]

def is_in_bounds(origin, dimensions, hmap):
    x, z = origin
    dx, dz = dimensions

    return 0 <= x and x + dx <= len(hmap) and 0 <= z and z + dz <= len(hmap[0])

def is_blocked(origin, dimensions, bmap):
    x, z = origin

    for dx in range(dimensions[0]):
        for dz in range(dimensions[1]):
            px = x + dx
            pz = z + dz

            if bmap[px][pz] != NOTHING:
                return True
    
    return False

def get_average_roughness(origin, y, dimensions, hmap):
    total_roughness = 0.0

    for dx in range(dimensions[0]):
        for dz in range(dimensions[1]):
            x = origin[0] + dx
            z = origin[1] + dz

            dy = y - (hmap[x][z] - 1)
            # we double the cost if we need to carve into terrain
            # the cost is also squared
            total_roughness += dy ** 2 if dy >= 0 else (dy ** 2) * 2 

    return total_roughness / (dimensions[0] * dimensions[1])

def get_water_amount(origin, dimensions, wmap):
    water_count = 0

    for dx in range(dimensions[0]):
        for dz in range(dimensions[1]):
            x = origin[0] + dx
            z = origin[1] + dz
            
            if wmap[x][z]:
                water_count += 1
    
    return water_count / (dimensions[0] * dimensions[1])
