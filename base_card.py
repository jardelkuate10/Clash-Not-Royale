import random

import pygame

from shooter import Shooter

colors = [
    (255, 0, 0),    # Red
    (0, 255, 0),    # Green
    (128, 0, 128),  # Purple
    (255, 255, 255),# White
    (0, 0, 0),      # Black
    (255, 255, 0),  # Yellow
    (0, 255, 255),  # Cyan
    (255, 0, 255),  # Magenta
    (128, 128, 128),# Gray
    (255, 165, 0)   # Orange
]

# characters = [shooter]

class BaseCard:
    def __init__(self, window, x, y):
        self.width = 132.5
        self.height = 160
        self.window = window
        self.color = colors[random.randint(0, 9)]
        self.x = x
        self.y = y
        self.rect = pygame.Rect(x, y, self.width, self.height)
        self.character = None
        self.active = False
        self.selected = False
        self.hold = None
        self.can_move = True

    def draw(self):
        if self.active:
            pygame.draw.rect(self.window, self.color, self.rect)

    def move(self, event, game_screen):
        if self.can_move:
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                if self.rect.collidepoint(event.pos):
                    self.selected = True

                    for holder in game_screen.selector.place_holders:
                        if self.rect.colliderect(holder):
                            self.hold = holder
            elif event.type == pygame.MOUSEBUTTONUP:
                if self.selected:
                    if self.rect.colliderect(game_screen.selector):
                        self.rect.clamp_ip(self.hold)
                        self.selected = False
                    elif self.rect.colliderect(game_screen.selector.my_side):
                        self.can_move = False
                        self.active = False

                        self.character = Shooter(self.window, self.rect.x + self.width / 2, self.rect.y + self.height / 2, 'black', game_screen)
                        game_screen.characters.append(self.character)
            elif event.type == pygame.MOUSEMOTION:
                if self.selected:
                    self.rect.x += event.rel[0]
                    self.rect.y += event.rel[1]