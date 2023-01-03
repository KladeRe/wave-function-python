import pygame
import os

def find_file(directory):
    files_found = []
    for path, subdirs, files in os.walk(directory):
        for name in files:
            files_found.append(os.path.join(path, name))
    return files_found

file_names = find_file("Tiles")

print(find_file("Tiles"))

pygame.init()

X = 4*32
Y = 4*32

screen = pygame.display.set_mode((X,Y))

pygame.display.set_caption("image")

imps = []
for file_name in file_names:
    imps.append(pygame.image.load(file_name).convert())




status = True

while (status):
    index = 0
    while index < len(imps):
        screen.blit(imps[index], ((index//4)*32, (index%4)*32))
        index += 1


    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            status = False
    pygame.display.update()


