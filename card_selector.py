import pygame
from deck import Deck

window_width, game_width, window_height, game_height = 600, 600, 1000, 800
card_x_buf = 20
card_width = 132.5

grass = (44, 134, 47)


class CardSelector:
    def __init__(self, window, game_screen):
        self.x = 0
        self.y = game_height
        self.height = window_height - game_height
        self.window = window
        self.game_screen = game_screen
        self.my_side = game_screen.side2
        self.enemy_side = game_screen.side1
        self.color = 'blue'
        self.card_width = 132.5
        self.card_height = 160
        self.rect = pygame.Rect(self.x, self.y, game_width, window_height - game_height)

        self.card_1_x = card_x_buf
        self.card_2_x = self.card_1_x + card_width + card_x_buf / 2
        self.card_3_x = self.card_2_x + card_width + card_x_buf / 2
        self.card_4_x = self.card_3_x + card_width + card_x_buf / 2
        self.card_x = [self.card_1_x, self.card_2_x, self.card_3_x, self.card_4_x]
        self.card_y = game_height + self.height / 10

        self.place1 = pygame.Rect(self.card_1_x, self.card_y, self.card_width, self.card_height)
        self.place2 = pygame.Rect(self.card_2_x, self.card_y, self.card_width, self.card_height)
        self.place3 = pygame.Rect(self.card_3_x, self.card_y, self.card_width, self.card_height)
        self.place4 = pygame.Rect(self.card_4_x, self.card_y, self.card_width, self.card_height)
        self.place_holders = [self.place1, self.place2, self.place3, self.place4]

        self.deck = Deck(window)
        self.active_cards = []
        self.load_cards()

    def draw(self):
        pygame.draw.rect(self.window, self.color, self.rect)
        for card in self.active_cards:
            card.draw()

    def update(self, event):
        for card in self.active_cards:
            card.move(event, self.game_screen)

    def load_cards(self):
        self.deck.shuffle()
        for card in self.deck.cards[:4]:
            card.active = True
            #card.color = 'yellow'
            self.active_cards.append(card)
            card.rect.x = self.card_x[self.active_cards.index(card)]
            card.rect.y = self.card_y
