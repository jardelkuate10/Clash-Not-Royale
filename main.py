import pygame
from side import Side

pygame.init()

width, height = 576, 1000
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('ClashNotRoyal')

running = True

grass = (44, 134, 47)

side = Side(screen,grass, 'top')
side2 = Side(screen, grass, 'bottom')

while running:

    for event in pygame.event.get():
        # exit out of game
        if event.type == pygame.QUIT:
            running = False

    screen.fill('black')
    side.draw()
    side2.draw()

    pygame.display.flip()

pygame.quit()