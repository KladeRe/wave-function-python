from files import *
import random
class Cell:
    def __init__(self, x, y, board):
        self.x = x
        self.y = y
        self.grid = board.grid
        self.options = []
        self.collapsed = False

        for file in find_files("Tiles"):
            self.options.append(file[6:-4])

    # Gives all the neighbors of the cell and their direction
    def neighbors(self):
        if self.x > 0:
            yield (self.grid[self.x - 1][self.y], 7)
            if self.y > 0:
                yield (self.grid[self.x - 1][self.y-1], 0)
                
            if self.y < len(self.grid[0])-1:
                yield (self.grid[self.x - 1][self.y + 1], 6)
                
        if self.y > 0:
            yield (self.grid[self.x][self.y - 1], 1)
        
        if self.y < len(self.grid[0])-1:
            yield (self.grid[self.x][self.y + 1], 5)

        if self.x < len(self.grid)-1:
            yield (self.grid[self.x + 1][self.y], 3)
            if self.y > 0:
                yield (self.grid[self.x + 1][self.y - 1], 2)
            if self.y < len(self.grid[0])-1:
                yield (self.grid[self.x + 1][self.y + 1], 4)

    # Picks a random option from the options attribute
    def choose_random_option(self):
        result = random.choice(self.options)

        index = 0
        while index < len(self.options):
            if self.options[index] != result:
                self.options.remove(self.options[index])
            else:
                index += 1

        self.collapsed = True


        for neighbor in self.neighbors():
            neighbor[0].collapse((neighbor[1]+4) %
                                 8, self.handshake(neighbor[1]))

    # Used when transfering data about the current cell to the next
    def handshake(self, direction):

        if direction % 2 == 0:
            all_possibilities = []
            for option in self.options:
                if option[direction//2] not in all_possibilities:
                    all_possibilities.append(option[direction//2])
            return all_possibilities

        else:
            all_possibilities2 = []
            for option in self.options:
                second = option[0]
                if not (((direction-1)//2)+1) > 3:
                    second = option[((direction-1)//2)+1]
                if (second, option[(direction-1)//2]) not in all_possibilities2:
                    all_possibilities2.append(
                        (second, option[(direction-1)//2]))
            return all_possibilities2

    # The collapse function in itself
    def collapse(self, direction, value):

        if not self.collapsed:
            didNothing = True
            if direction % 2 == 1:

                index = 0
                while index < len(self.options):

                    second2 = self.options[index][0]
                    if ((direction-1)//2)+1 != 4:
                        second2 = self.options[index][((direction-1)//2)+1]
                    if (self.options[index][((direction-1)//2)], second2) not in value:

                        didNothing = False
                        self.options.remove(self.options[index])
                    else:
                        index += 1

                if not didNothing:
                    if len(self.options) == 1:
                        self.collapsed = True

                    for neighbor in self.neighbors():
                        neighbor[0].collapse((neighbor[1]+4) %
                                             8, self.handshake(neighbor[1]))

            else:
                index = 0
                while index < len(self.options):

                    if self.options[index][direction//2] not in value:

                        didNothing = False
                        self.options.remove(self.options[index])
                    else:
                        index += 1

                if not didNothing:
                    if len(self.options) == 1:
                        self.collapsed = True

                    for neighbor in self.neighbors():
                        neighbor[0].collapse((neighbor[1]+4) %
                                             8, self.handshake(neighbor[1]))