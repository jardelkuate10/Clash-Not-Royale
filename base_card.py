import pygame


class BaseCard:
    def __init__(self, screen, x, y, color):
        self.width = 132.5
        self.height = 160
        self.screen = screen
        self.color = color
        self.x = x
        self.y = y
        self.rect = pygame.Rect(x, y, self.width, self.height)
        self.active = False
        self.selected = False

    def draw(self):
        if self.active:
            pygame.draw.rect(self.screen, self.color, self.rect)

    def move(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if self.rect.collidepoint(event.pos):
                self.selected = True
        elif event.type == pygame.MOUSEBUTTONUP:
            self.selected = False
        elif event.type == pygame.MOUSEMOTION:
            if self.selected:
                print('motion')
                self.rect.x += event.rel[0]
                self.rect.y += event.rel[1]