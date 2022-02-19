
from gdpc.interface import Interface
from gdpc.worldLoader import WorldSlice

USE_BATCHING = True

area = (0, 0, 128, 128)  # default build area
interface = Interface(buffering=True)

def setBlock(x, y, z, block):
    interface.placeBlockBuffered(x, y, z, block)

def sendBlocks():
    interface.sendBlocks()