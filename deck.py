import random
from base_card import BaseCard


class Deck:
    def __init__(self, window):
        self.window = window
        self.cards = []

        for i in range(10):
            self.cards.append(BaseCard(self.window, 0, 0))

    def shuffle(self):
        random.shuffle(self.cards)