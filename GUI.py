import pygame
from files import *
from Board import *

def makeGUI(HEIGHT, WIDTH, board):

    grid = board.grid

    clock = pygame.time.Clock()

    image_WIDTH = 24
    image_HEIGHT = image_WIDTH

    pygame.init()

    X = WIDTH*image_WIDTH
    Y = HEIGHT*image_HEIGHT

    screen = pygame.display.set_mode((X, Y))

    pygame.display.set_caption("Map")

    running = True

    while running:
        clock.tick(30)

        if not board.is_done():
            target = board.get_lowest_entropy()
            board.grid[target[0]][target[1]].choose_random_option()
        

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j].collapsed:
                    image = pygame.image.load(f"Tiles/{grid[i][j].options[0]}.png").convert()
                    transformed  = pygame.transform.scale(image, (image_WIDTH, image_HEIGHT))
                    screen.blit(transformed, (i*image_WIDTH, j*image_HEIGHT))


        for i in pygame.event.get():
            if i.type == pygame.QUIT:
                running = False
        pygame.display.update()
    pygame.quit()
