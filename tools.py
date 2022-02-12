from http_client import interfaceUtils, mapUtils
from http_client.worldLoader import WorldSlice

USE_BATCHING = True

area = (0, 0, 128, 128)  # default build area
worldSlice = WorldSlice(area)
heightmap = mapUtils.calcGoodHeightmap(worldSlice)

def heightAt(x, z):
    """Access height using local coordinates."""
    # Warning:
    # Heightmap coordinates are not equal to world coordinates!
    return heightmap[(x - area[0], z - area[1])]

def setBlock(x, y, z, block):
    """Place blocks or add them to batch."""
    if USE_BATCHING:
        # add block to buffer, send once buffer has 100 items in it
        interfaceUtils.placeBlockBatched(x, y, z, block, 100)
    else:
        interfaceUtils.setBlock(x, y, z, block)