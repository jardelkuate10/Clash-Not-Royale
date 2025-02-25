import pygame

import main_tower
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

    # Check keyboard state
    keys = pygame.key.get_pressed()

    if keys[pygame.K_SPACE]:
        side.main_tower.health_bar.hp -= 0.01 # Decrease health by 10
        if side.main_tower.health_bar.hp <= 0:
            side.main_tower.health_bar.hp = 0  # Prevent health from going below 0


    screen.fill('black')
    side.draw()
    side2.draw()

    #pygame.display.update()
    pygame.display.flip()

pygame.quit()