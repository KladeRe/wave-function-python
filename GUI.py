import pygame
from files import *

def makeGUI(HEIGHT, WIDTH, grid):

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
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                screen.blit(pygame.image.load(f"Tiles/{grid[i][j].options[0]}.png").convert(), (i*32, j*32))

        for i in pygame.event.get():
            if i.type == pygame.QUIT:
                running = False
        pygame.display.update()
