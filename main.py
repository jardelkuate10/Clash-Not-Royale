import pygame
from side import Side

pygame.init()

width, height = 576, 1000
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Blokduku')

running = True

side = Side(screen,'red', 'top')
side2 = Side(screen, 'green', 'bottom')

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