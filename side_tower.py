import pygame

size = 30

class SideTower:
    def __init__(self, screen, x, y, color, position):
        self.screen = screen
        self.rect = pygame.Rect(x, y, 30, 30)
        self.color = color
        self.x = x
        self.y = y
        self.position = position
        self.health_x = x + 5
        self.health_y = 0

        if self.position == 'top':
            self.health_y = self.y - 20
        elif self.position == 'bottom':
            self.health_y = self.y + size + 10


        self.health = pygame.Rect(self.health_x, self.health_y , 20, 10)


    def draw(self):
        pygame.draw.rect(self.screen, self.color, self.rect)
        pygame.draw.rect(self.screen, 'blue', self.health)
