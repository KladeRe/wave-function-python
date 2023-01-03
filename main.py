import random
import os
import pygame


def find_files(directory):
    files_found = []
    for path, subdirs, files in os.walk(directory):
        for name in files:
            files_found.append(os.path.join(path, name))
    return files_found

def find_file(file_name, directory):
    file_found = ""
    for path, subdirs, files in os.walk(directory):
        for name in files:
            if(file_name == name):
                file_found = os.path.join(path,name)

    return file_found


class Cell:
    def __init__(self, x, y, board):
        self.x = x
        self.y = y
        self.grid = board.grid
        self.options = []
        self.collapsed = False

        for file in find_files("Tiles"):
            self.options.append(file[6:-4])

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

    def choose_random_option(self):
        result = random.choice(self.options)

        index = 0
        while index < len(self.options):
            if self.options[index] != result:
                self.options.remove(self.options[index])
            else:
                index += 1

        self.collapsed = True

        print(self.x, self.y)

        for neighbor in self.neighbors():
            neighbor[0].collapse((neighbor[1]+4) %
                                 8, self.handshake(neighbor[1]))

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
        


class Board:
    def __init__(self, grid):
        self.grid = grid

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
        print(f"I chose {lowest}")
        return random.choice(lowest)[0:2]

    def is_done(self) -> bool:
        for i in range(len(self.grid)):
            for j in range(len(self.grid[0])):
                if self.grid[i][j].collapsed == False:
                    return False
        return True

    def wave_function(self):
        while not self.is_done():
            target = self.get_lowest_entropy()
            self.grid[target[0]][target[1]].choose_random_option()



def main():
    HEIGHT = 10
    WIDTH = 10

    board = Board([])
    for i in range(WIDTH):
        board.grid.append([])
        for j in range(HEIGHT):
            board.grid[i].append(Cell(i, j, board))

    board.wave_function()


    pygame.init()


    X = HEIGHT*32
    Y = WIDTH*32

    screen = pygame.display.set_mode((X, Y))

    pygame.display.set_caption("Map")

    imps = []
    for file_name in find_files("Tiles"):
        imps.append(pygame.image.load(file_name).convert())
    
    running = True

    while running:
        for i in range(len(board.grid)):
            for j in range(len(board.grid[0])):
                screen.blit(pygame.image.load(find_file(f"{board.grid[i][j].options[0]}.png", "Tiles")).convert(), (i*32, j*32))


        for i in pygame.event.get():
            if i.type == pygame.QUIT:
                running = False
        pygame.display.update()


if __name__ == "__main__":
    main()
