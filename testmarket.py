from house.decoration.flag_generator import FlagGenerator
from house.grid import Grid
from house.frame_generator import FrameGenerator
from house.floor_generator import FloorGenerator
from clear import Clear
from checkerboard import CheckerBoardGenerator
from house.house import House
from house.roof.roof_generator import RoofGenerator
from house.roof.tower_roof import TowerRoofGenerator
from house.walls.wall_generator import WallGenerator
from misc.tree import Tree
from city.city import City
from misc.tree_generator import TreeGenerator
from market.stall_generator import StallGenerator
from market.stall import Stall
from gdpc.interface import requestPlayerArea, Interface, setBuildArea, runCommand

size_x = 200
size_z = 200

area = list(requestPlayerArea(size_x, size_z))
area[1] = 3
area[4] = 210
setBuildArea(*area)

interface = Interface(area[0], 0, area[2], True)

city = City((1,1), 3, (200,200))
#city.add_stall((100, 4, 100))
#city.stalls.append(Stall((100, 4, 100), 'basic','none','basic','none','z_plus'))
#city.add_stalls2()
#city.stalls.append(Stall((100, 4, 100), 'basic','none','basic','none','z_minus'))
city.add_stalls()

#city.add_random_trees(150, 5)
#CheckerBoardGenerator(tile_width=5, tile_depth=5, area=(1, 1, size_x, size_z), y=3).generate(interface)

StallGenerator(stalls=city.stalls).generate(interface)

#runCommand('/summon minecraft:armor_stand -233 10 -557 {ShowArms:1b,NoBasePlate:1b,ArmorItems:[{id:"minecraft:leather_boots",Count:1b},{id:"minecraft:leather_leggings",Count:1b},{id:"minecraft:leather_chestplate",Count:1b},{id:"minecraft:player_head",Count:1b,tag:{SkullOwner:{Id:[I;440871046,979259357,-1150162889,656058295],Properties:{textures:[{Value:"eyJ0ZXh0dXJlcyI6eyJTS0lOIjp7InVybCI6Imh0dHA6Ly90ZXh0dXJlcy5taW5lY3JhZnQubmV0L3RleHR1cmUvM2U4MGM3M2I3NjVkOWYyZTJhMWFlNmQ5ZGY5NmM1ZmJjNjEyNmVlNTRmOWRmMGE0NmJiMWYwMGVmMGIwMjc5ZSJ9fX0="}]}}}}]}')
#runCommand('setblock -180 10 -480 minecraft:player_head[rotation=0]{SkullOwner:{Id:[I;440871046,979259357,-1150162889,656058295],Properties:{textures:[{Value:"eyJ0ZXh0dXJlcyI6eyJTS0lOIjp7InVybCI6Imh0dHA6Ly90ZXh0dXJlcy5taW5lY3JhZnQubmV0L3RleHR1cmUvM2U4MGM3M2I3NjVkOWYyZTJhMWFlNmQ5ZGY5NmM1ZmJjNjEyNmVlNTRmOWRmMGE0NmJiMWYwMGVmMGIwMjc5ZSJ9fX0="}]}}} replace')
#runCommand('time set day')