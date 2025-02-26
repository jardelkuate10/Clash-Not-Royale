import pygame
from health_bar import HealthBar
from base_tower import BaseTower


class MainTower(BaseTower):
    def __init__(self, screen, x, y, color, position):
        self.size = 60

        super().__init__(screen, x, y, color, position, self.size)

        self.max_hp = 1000
        self.hp = self.max_hp

