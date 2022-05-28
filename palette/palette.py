from dataclasses import dataclass

from palette.design.design import LOW, STONE_AMOUNT

# domains
WALL_PRIMARY = 'wall_primary'
WALL_SECONDARY = 'wall_secondary'
ROOF_PRIMARY = 'roof_primary'
ROOF_SECONDARY = 'roof_secondary'
FRAME = 'frame'
FLOOR = 'floor'
STONE = 'stone'
STONE_ACCENT = 'stone_accent' # complements the main stone
WOOD = 'wood'
WOOD_ACCENT = 'wood_accent' # complements the main wood

class Palette:
<<<<<<< HEAD
    data : dict

    def __init__(self, data) -> None:
        self.data = data

        if STONE_AMOUNT not in self.data:
            self.data[STONE_AMOUNT] = LOW

    def get_material(self, domain, block):
        order = self.__get_resolution_order(domain)

        for dm in order:
            if dm in self.data and block in self.data[dm]:
                return self.data[dm][block]

    def __get_resolution_order(self, domain):
        base = [STONE, WOOD] if self.data[STONE_AMOUNT] != LOW else [WOOD, STONE]
        base_accent = [STONE_ACCENT, WOOD_ACCENT] if self.data[STONE_AMOUNT] != LOW else [WOOD_ACCENT, STONE_ACCENT]

        if domain == WALL_PRIMARY:
            return [WALL_PRIMARY, WALL_SECONDARY] + base
        if domain == WALL_SECONDARY:
            return [WALL_SECONDARY, WALL_PRIMARY] + base_accent
        if domain == ROOF_PRIMARY:
            return [ROOF_PRIMARY, ROOF_SECONDARY, WOOD] # no stone for primary roof
        if domain == ROOF_SECONDARY:
            return [ROOF_SECONDARY, ROOF_PRIMARY] + base_accent
        if domain == FRAME:
            return [FRAME, WALL_PRIMARY, WALL_SECONDARY] + base
        if domain == FLOOR:
            return [FLOOR, WOOD]
        if domain == STONE:
            return [STONE, WOOD]
        if domain == STONE_ACCENT:
            return [STONE_ACCENT, STONE, WOOD]
        if domain == WOOD:
            return [WOOD]
        if domain == WOOD_ACCENT:
            return [WOOD_ACCENT, WOOD] 

    
    
=======
    fence : Material = BasicMaterial(Block('oak_fence'))
    frame : Material = BasicMaterial(Block('oak_log', is_log=True))
    floor : Material = BasicMaterial(Block('oak_planks'))
    roof : Material = BasicMaterial(Block('oak_log'))
    wall : Material = BasicMaterial(Block('oak_planks'))
    wood : Material = BasicMaterial(Block('jungle_wood'))
    leaves : Material = BasicMaterial(Block(f'jungle_leaves[persistent=true]'))

    colour_list : list[str] = ('red', 'white', 'orange', 'magenta','light_blue', 'yellow', 'lime', 'pink', 'gray', 'light_gray', 'cyan',
    'blue', 'purple', 'brown', 'green', 'black')

    #market related items
    market_base : Material = BasicMaterial(Block('oak_planks'))
    market_fence : Material = BasicMaterial(Block('oak_fence'))
    market_fence_gate : Material = BasicMaterial(Block('oak_fence_gate'))
    market_trapdoor : Material = BasicMaterial(Block('oak_trapdoor'))
    market_campfire : Material = BasicMaterial(Block(f'campfire[lit=false]'))
    market_upside_down_stair : Material = BasicMaterial(Block(f'oak_stairs[half=top]'))
    market_stair : Material = BasicMaterial(Block(f'oak_stairs'))
    market_top_slab : Material = BasicMaterial(Block(f'oak_slab[type=top]'))
>>>>>>> a3980a71e0b167cc2bb6932aa4855d646adecd66
