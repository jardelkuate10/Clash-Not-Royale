import pygame
from Health_Bar import HealthBar

size = 60

class MainTower:
    def __init__(self, screen, x, y, color, position):
        self.screen = screen
        self.color = color
        self.position = position
        self.x = x
        self.y = y
        #self.health_x = x + 5
        #self.health_y = 0
        #self.dmg_x = x + 5
        #self.dmg_y = 0
        #self.hp = 75
        #self.max_hp = 100

        #if self.position == 'top':
            #self.health_y = self.y - 20
            #self.dmg_y = self.y - 20
        #elif self.position == 'bottom':
            #self.health_y = self.y + size + 10
            #self.dmg_y = self.y + size + 10

        if self.position == 'top':
            self.health_bar = HealthBar(self.x + 5, self.y - 20, size - 10, 10, 100)
        elif self.position == 'bottom':
            self.health_bar = HealthBar(self.x + 5, self.y + size + 10, size - 10, 10, 100)

        #self.health_bar.hp = 70

        #self.health_bar = HealthBar(self.x + 5, self.y, size - 10, 10, 100)

        self.rect = pygame.Rect(x, y, size, size)

        #ratio = self.hp / self.max_hp
        #self.health = pygame.Rect(self.health_x, self.health_y , 50 * ratio, 10)

        #self.dmg = pygame.Rect(self.dmg_x, self.dmg_y, 50, 10)

    def draw(self):
        pygame.draw.rect(self.screen, self.color, self.rect)
        self.health_bar.draw(self.screen)
        #pygame.draw.rect(self.screen, 'red', self.dmg)
        #pygame.draw.rect(self.screen, 'blue', self.health)



