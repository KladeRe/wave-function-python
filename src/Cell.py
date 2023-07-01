from files import *
import random

class Cell:
    def __init__(self, x, y, board):
        self.x = x
        self.y = y
        self.grid = board
        self.options = list(map(lambda file: file[6:14], find_files("Tiles")))
        self.collapsed = False

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
        self.options = [result]
        self.collapsed = True

        for neighbor in self.neighbors():
            neighbor[0].collapse(self.handshake(neighbor[1]))

    # Used when transfering data about the current cell to the next
    def handshake(self, direction):
        for neighbor in self.neighbors():
            if neighbor[1] == direction:
                receiver = neighbor[0]
        
        all_possibilities = []
        
        if direction % 2 == 0:          
            for option in self.options:
                if option[direction] not in all_possibilities:              
                    all_possibilities.append(option[direction])
            
            result = list(filter(lambda option: option[(direction +4) % 8] in all_possibilities, receiver.options))
            
        elif direction != 7:
            for option in self.options:
                if (option[direction+1], option[direction], option[direction-1]) not in all_possibilities:
                    all_possibilities.append((option[direction+1], option[direction], option[direction-1]))

            result = list(filter(lambda option: (option[(direction + 3) % 8], option[(direction +4) % 8], option[(direction +5) % 8]) in all_possibilities, receiver.options))
            
        else:
            for option in self.options:
                if (option[0], option[7], option[6]) not in all_possibilities:
                    all_possibilities.append((option[0], option[7], option[6]))
            
            result = list(filter(lambda option: (option[2], option[3], option[4]) in all_possibilities, receiver.options))
                
        return result

    # The collapse function in itself
    def collapse(self, value):
        if not self.collapsed and len(value) != len(self.options):          
            self.options = value
            if len(self.options) == 1:
                self.collapsed = True
            for neighbor in self.neighbors():
                neighbor[0].collapse(self.handshake(neighbor[1]))                     