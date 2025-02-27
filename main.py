import pygame

from character_selector import CharacterSelector
import main_tower
from base_character import BaseCharacter
from side import Side
from shooter import Shooter

pygame.init()

clock = pygame.time.Clock()
fps = 60
screen_width, game_width, height = 1100, 600, 1000
screen = pygame.display.set_mode((screen_width, height))
pygame.display.set_caption('ClashNotRoyal')

running = True

grass = (44, 134, 47)

side1 = Side(screen, grass, 'top')
side2 = Side(screen, grass, 'bottom')
selector = CharacterSelector(screen, side2, side1)

#dps = Shooter(screen, game_width/2, game_width/2, 'black', side2, side1)

while running:

    for event in pygame.event.get():
        # exit out of game
        if event.type == pygame.QUIT:
            running = False

    selector.update()
    # selector.dps.move()
    # selector.dps.fire_projectile()
    # selector.dps.update()

    screen.fill('black')
    side1.draw()
    side2.draw()
    selector.draw()
    #guy.draw()
    #dps.draw()

    # pygame.display.update()
    pygame.display.flip()

    clock.tick(fps)

pygame.quit()
