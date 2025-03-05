import pygame
from side_tower import SideTower
from main_tower import MainTower

window_width, game_width, window_height, game_height = 600, 600, 1000, 800
main_gap = 100
side_gap = 175
main_size = 60
side_size = 30
tower_gap = 2*main_size

class Side:

    def __init__(self, window, color, position):
        self.window = window
        self.rect = None
        self.color = color
        self.position = position
        self.towers = []
        self.main_x = game_width/2 - main_size/2
        self.s1_x = self.main_x - tower_gap - side_size
        self.s2_x = self.main_x + tower_gap + main_size
        self.main_y = 0
        self.s_y = 0

        if self.position == 'top':
            self.main_y = main_gap
            self.s_y = side_gap
            self.rect = pygame.Rect(0, 0, game_width, game_height/2)
        elif self.position == 'bottom':
            self.main_y = game_height - main_gap - main_size
            self.s_y = game_height - side_gap - side_size
            self.rect = pygame.Rect(0, game_height/2, game_width, game_height/2)

        self.main_tower = MainTower(self.window, self.main_x, self.main_y, 'white', self.position)
        self.side_tower_1 = SideTower(self.window, self.s1_x, self.s_y, 'white', self.position)
        self.side_tower_2 = SideTower(self.window, self.s2_x, self.s_y, 'white', self.position)

        self.towers.append(self.main_tower)
        self.towers.append(self.side_tower_1)
        self.towers.append(self.side_tower_2)

    def draw(self):
        pygame.draw.rect(self.window, self.color, self.rect)
        for tower in self.towers:
            tower.draw()

    def update(self):
        for tower in self.towers:
            tower.take_damage()