import pygame

from health_bar import HealthBar


class BaseTower:
    def __init__(self, screen, x, y, color, position, size):
        x_buf = 5  # move the health bar to the right of the tower
        y_buf = 20  # move the health bar above/below the tower
        w_buf = size - 10  # length of health
        h_buf = 10  # height of health

        self.screen = screen
        self.color = color
        self.position = position
        self.x = x
        self.y = y
        self.hp = None
        self.rect = pygame.Rect(x, y, size, size)

        if self.position == 'top':
            self.health_bar = HealthBar(self, self.x + x_buf, self.y - y_buf, w_buf, h_buf)
        elif self.position == 'bottom':
            self.health_bar = HealthBar(self, self.x + x_buf, self.y + size + y_buf/2 , w_buf, h_buf)

    def draw(self):
        pygame.draw.rect(self.screen, self.color, self.rect)
        self.health_bar.draw(self.screen)

    def take_damage(self, dmg):
        self.hp -= dmg  # Decrease health
        if self.hp <= 0:
            self.hp = 0  # Prevent health from going below 0
