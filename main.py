import random


class Cell:
    def __init__(self, x, y, board):
        self.x = x
        self.y = y
        self.grid = board.grid
        self.options = [[0, 0, 0,0],[1,1,1,1], [1,1,0,0], [0,0,1,1]]
        self.collapsed = False

    def neighbors(self):
        if self.x > 0:
            yield (self.grid[self.x - 1][self.y], 7)
            if self.y > 0:
                yield (self.grid[self.x - 1][self.y-1], 0)
                yield (self.grid[self.x][self.y - 1], 1)
            if self.y < len(self.grid[0])-1:
                yield (self.grid[self.x - 1][self.y + 1], 6)
                yield (self.grid[self.x][self.y + 1], 5)

        if self.x < len(self.grid)-1:
            yield (self.grid[self.x + 1][self.y], 3)
            if self.y > 0:
                yield (self.grid[self.x + 1][self.y - 1], 2)
            if self.y < len(self.grid[0])-1:
                yield (self.grid[self.x + 1][self.y + 1], 4)
    
    def choose_random_option(self):
        result = random.choice(self.options)

        for option in self.options:
            if option != result:
                self.options.remove(option)
        
        self.collapsed = True

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
                    all_possibilities2.append((second, option[(direction-1)//2]))
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
                        print(self.options)
                        print(self.handshake(neighbor[1]))
                        neighbor[0].collapse((neighbor[1]+4)%8, self.handshake(neighbor[1]))
                    

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
                        print(self.options)
                        print(self.handshake(neighbor[1]))
                        neighbor[0].collapse((neighbor[1]+4)%8, self.handshake(neighbor[1]))   
                    





class Board:
    def __init__(self, grid):
        self.grid = grid

    def get_lowest_entropy(self):
        lowest = [(0, 0, len(self.grid)**2 + 1)]
        for i in range(len(self.grid)):
            for j in range(len(self.grid[0])):
                entropy = len(self.grid[i][j].options)
                if entropy == lowest[0][2]:
                    lowest.append((i, j, entropy))
                elif entropy < lowest[0][2]:
                    lowest.clear()
                    lowest.append((i, j, entropy))
        return random.choice(lowest)[0:2]

    def is_done(self) -> bool:
        for i in range(len(self.grid)):
            for j in range(len(self.grid[0])):
                if self.grid[i][j].collapsed == False:
                    return False
        return True


def main():
    HEIGHT = 3
    WIDTH = 3

    board = Board([]) 
    for i in range(WIDTH):
        board.grid.append([])
        for j in range(HEIGHT):
            board.grid[i].append(Cell(i, j, board))

    board.grid[1][1].collapse(1, [(1,1)])

    for row in board.grid:
        for cell in row:
            print(cell.x, cell.y)
            print(cell.options)



if __name__ == "__main__":
    main()
