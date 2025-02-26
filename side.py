import pygame
from side_tower import SideTower
from main_tower import MainTower

length = 1000
main_gap = 100
side_gap = 175


class Side:

    def __init__(self, screen, color, position):
        self.screen = screen
        self.rect = None
        self.color = color
        self.position = position
        self.towers = []
        self.main_x = 258
        self.s1_x = 129
        self.s2_x = 417
        self.main_y = 0
        self.s_y = 0

        if self.position == 'top':
            self.main_y = main_gap
            self.s_y = side_gap
            self.rect = pygame.Rect(0, 0, 576, 500)
        elif self.position == 'bottom':
            self.main_y = length - main_gap
            self.s_y = length - side_gap
            self.rect = pygame.Rect(0, 500, 576, 500)

        self.main_tower = MainTower(self.screen, self.main_x, self.main_y, 'white', self.position)
        self.side_tower_1 = SideTower(self.screen, self.s1_x, self.s_y, 'white', self.position)
        self.side_tower_2 = SideTower(self.screen, self.s2_x, self.s_y, 'white', self.position)

        self.towers.append(self.main_tower)
        self.towers.append(self.side_tower_1)
        self.towers.append(self.side_tower_2)

    def draw(self):
        pygame.draw.rect(self.screen, self.color, self.rect)
        for tower in self.towers:
            tower.draw()

    def update(self):
        for tower in self.towers:
            tower.take_damage()