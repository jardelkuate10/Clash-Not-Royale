import pygame
from shooter import Shooter
from deck import Deck

screen_width, game_width, screen_height, game_height = 600, 600, 1000, 800
card_x_buf = 20
card_width = 132.5

grass = (44, 134, 47)


class CardSelector:
    def __init__(self, screen, my_side, enemy_side):
        self.x = 0
        self.y = game_height
        self.height = screen_height - game_height
        self.screen = screen
        self.my_side = my_side
        self.enemy_side = enemy_side
        self.color = 'blue'  # grass
        self.rect = pygame.Rect(self.x, self.y, game_width, screen_height - game_height)

        self.card_1_x = card_x_buf
        self.card_2_x = self.card_1_x + card_width + card_x_buf / 2
        self.card_3_x = self.card_2_x + card_width + card_x_buf / 2
        self.card_4_x = self.card_3_x + card_width + card_x_buf / 2
        self.card_x = [self.card_1_x, self.card_2_x, self.card_3_x, self.card_4_x]

        self.card_y = game_height + self.height / 10
        self.deck = Deck(screen)
        self.active_cards = []
        self.load_cards()

    def draw(self):
        pygame.draw.rect(self.screen, self.color, self.rect)
        for card in self.active_cards:
            card.draw()

    def update(self, event):
        for card in self.active_cards:
            card.move(event)

    def load_cards(self):
        self.deck.shuffle()
        for card in self.deck.cards[:4]:
            card.active = True
            card.color = 'yellow'
            self.active_cards.append(card)
            card.rect.x = self.card_x[self.active_cards.index(card)]
            card.rect.y = self.card_y
