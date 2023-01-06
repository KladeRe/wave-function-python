from Board import *
from GUI import *
def main():
    # These define how many tiles we are going to have
    HEIGHT = 20
    WIDTH = 20

    # The board is inizialized here
    board = Board(WIDTH, HEIGHT)

    # This makes the end result visible
    makeGUI(HEIGHT, WIDTH, board)

if __name__ == "__main__":
    main()