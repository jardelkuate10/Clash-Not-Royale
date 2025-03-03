import pygame
import random
from base_card import BaseCard

class Deck:
    def __init__(self, screen):
        self.screen = screen
        self.cards = []

        for i in range(10):
            self.cards.append(BaseCard(self.screen, 0, 0, 'gray'))

    def shuffle(self):
        random.shuffle(self.cards)