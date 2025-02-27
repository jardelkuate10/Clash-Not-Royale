import pygame
from shooter import Shooter

screen_width, game_width, height = 1100, 600, 1000


class CharacterSelector:
    def __init__(self, screen, my_side, enemy_side):
        self.x = game_width
        self.y = 0
        self.screen = screen
        self.my_side = my_side
        self.enemy_side = enemy_side
        #self.deck = deck
        self.dps = Shooter(screen, self.x + 100, height/2, 'black', my_side, enemy_side)
        self.color = 'gray'
        self.rect = pygame.Rect(self.x, self.y, screen_width - game_width, height)

    def draw(self):
        pygame.draw.rect(self.screen, self.color, self.rect)
        self.dps.draw()

    def update(self):
        self.dps.move()
        if self.dps.rect.colliderect(self.enemy_side.rect):
            self.dps.fire_projectile()
            self.dps.update()