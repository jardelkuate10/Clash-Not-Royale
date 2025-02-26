import pygame


class HealthBar:
    def __init__(self, tower, x, y, w, h):
        self.tower = tower
        self.x = x
        self.y = y
        self.w = w
        self.h = h

    def draw(self, surface):
        ratio = self.tower.hp / self.tower.max_hp
        pygame.draw.rect(surface, "red", (self.x, self.y, self.w, self.h))
        pygame.draw.rect(surface, "blue", (self.x, self.y, self.w * ratio, self.h))
