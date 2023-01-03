from Board import *
from GUI import *
def main():
    # These define how many tiles we are going to have
    HEIGHT = 10
    WIDTH = 10

    # The board is inizialized here
    board = Board([])
    for i in range(WIDTH):
        board.grid.append([])
        for j in range(HEIGHT):
            board.grid[i].append(Cell(i, j, board))

    # This does what is says
    board.wave_function()

    # This makes the end result visible
    makeGUI(HEIGHT, WIDTH, board.grid)

if __name__ == "__main__":
    main()