import pygame

from card_selector import CardSelector
import main_tower
from base_character import BaseCharacter
from side import Side
from shooter import Shooter

pygame.init()

clock = pygame.time.Clock()
fps = 60
screen_width, game_width, screen_height, game_height = 600, 600, 1000, 800
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('ClashNotRoyal')

running = True

grass = (44, 134, 47)

side1 = Side(screen, grass, 'top')
side2 = Side(screen, grass, 'bottom')
selector = CardSelector(screen, side2, side1)

while running:

    for event in pygame.event.get():
        # exit out of game
        if event.type == pygame.QUIT:
            running = False
        else:
            selector.update(event)

    screen.fill('black')
    side1.draw()
    side2.draw()
    selector.draw()

    pygame.display.flip()

    clock.tick(fps)

pygame.quit()
