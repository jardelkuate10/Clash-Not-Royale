import pygame

from card_selector import CardSelector
from game_screen import GameScreen
from side import Side

pygame.init()

clock = pygame.time.Clock()
fps = 60
window_width, window_height = 600, 1000
window = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption('ClashNotRoyal')

game_screen = GameScreen(window)


running = True

while running:

    for event in pygame.event.get():
        # exit out of game
        if event.type == pygame.QUIT:
            running = False
        else:
            game_screen.update(event)

    window.fill('black')
    game_screen.draw()

    pygame.display.flip()

    clock.tick(fps)

pygame.quit()
