import random
from Cell import *

class Board:
    def __init__(self, width, height):
        self.grid = []
        self.width = width
        self.height = height
        for i in range(width):
            self.grid.append([])
            for j in range(height):
                self.grid[i].append(Cell(i, j, self.grid))

    # Finds and picks the cell with the lowest entropy (least amount of options)
    def get_lowest_entropy(self):
        lowest = [(0, 0, 100)]
        for i in range(len(self.grid)):
            for j in range(len(self.grid[0])):
                entropy = len(self.grid[i][j].options)
                if entropy == lowest[0][2]:
                    lowest.append((i, j, entropy))
                elif entropy < lowest[0][2] and entropy > 1:
                    lowest.clear()
                    lowest.append((i, j, entropy))

        return random.choice(lowest)[0:2]

    # Checks whether the wave-function-collapse is completed
    def is_done(self) -> bool:
        for i in range(len(self.grid)):
            for j in range(len(self.grid[0])):
                if self.grid[i][j].collapsed == False:
                    return False
        return True

    
    """ def wave_function(self):
        while not self.is_done():
            target = self.get_lowest_entropy()
            self.grid[target[0]][target[1]].choose_random_option() """

