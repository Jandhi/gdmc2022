from generator import Generator

SMALL = (7, 7)
MEDIUM = (13, 17)
LARGE = (25, 33)
dimensions = [SMALL, MEDIUM, LARGE]

structures = []
structures_by_dim = {
    dim : [] for dim in dimensions
}

def add_structure(cls):
    structures.append(cls)
    structures_by_dim[cls.dimensions].append(cls)

class Structure_meta(type):
    def __new__(cls, name, bases, dct):
        struct = super().__new__(cls, name, bases, dct)

        if name == 'Structure':
            return struct

        if struct.dimensions is None:
            raise ValueError(f"Structure {struct.__name__} does not have dimensions defined!")

        struct.count = 0

        old_generate_function = struct.generate

        def generate_override(self, interface):
            print(f'Generating a {struct.__name__}!')
            struct.count += 1

            # used to determine ground block
            block = self.slice.getBlockAt(
                self.origin[0] + interface.offset[0], 
                self.hmap[self.origin[0]][self.origin[1]] - 1,
                self.origin[1] + interface.offset[2])

            # clear
            if struct.clear_area:
                for dx in range(struct.dimensions[0]):
                    for dz in range(struct.dimensions[1]):
                        x = self.origin[0] + dx
                        z = self.origin[1] + dz
                        y = self.hmap[x][z] - 1

                        if y > self.y:
                            for py in range(self.y + 1, y):
                                interface.placeBlock(x, py, z, 'air')
                        else:
                            for py in range(y + 1, self.y):
                                interface.placeBlock(x, py, z, block) # GROUND BLOCK!


            old_generate_function(self, interface)
            
        setattr(struct, 'generate', generate_override)

        return struct

class Structure(Generator, metaclass=Structure_meta):
    dimensions = None
    clear_area = True
    max_roughness = 2.0
    max_water = 0.25