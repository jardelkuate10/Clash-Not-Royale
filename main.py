import pygame

import main_tower
from base_character import BaseCharacter
from side import Side

pygame.init()

clock = pygame.time.Clock()
fps = 60
width, height = 576, 1000
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('ClashNotRoyal')

running = True

grass = (44, 134, 47)

side1 = Side(screen, grass, 'top')
side2 = Side(screen, grass, 'bottom')
guy = BaseCharacter(screen, width/2, height/2, 'black', side2, side1)

while running:

    for event in pygame.event.get():
        # exit out of game
        if event.type == pygame.QUIT:
            running = False

        guy.move()

    screen.fill('black')
    side1.draw()
    side2.draw()
    guy.draw()

    # pygame.display.update()
    pygame.display.flip()

    clock.tick(fps)

pygame.quit()
