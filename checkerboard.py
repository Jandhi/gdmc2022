from tools import area, heightAt, setBlock
from generator import Generator

class CheckerBoardGenerator(Generator):
    name      = 'checkerboard'
    tile_width = 1
    tile_depth = 1
    height    = 3
    block1    = 'red_terracotta'
    block2    = 'green_terracotta'
    boundary  = 'orange_terracotta'
    y = 0

    def __get_work_amount__(self) -> int:
        return self.width * self.depth

    def __generate__(self):
        # subtract one for overlapping edges
        width = self.tile_width - 1 
        depth = self.tile_depth - 1

        for x in range(self.x1, self.x2):
            for z in range(self.z1, self.z2):
                self.bar.next()
                block = self.block1

                board_x = x // width
                board_z = z // depth

                if x % width == 0 or z % depth == 0:
                    block = self.boundary
                elif (board_x + board_z) % 2 == 1:
                    block = self.block2

                setBlock(x, self.y, z, block)

if __name__ == '__main__':
    CheckerBoardGenerator(tile_width=5, tile_depth=5, area=area, y=3).generate()