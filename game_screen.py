from card_selector import CardSelector
from side import Side

grass = (44, 134, 47)


class GameScreen:
    def __init__(self, window):
        self.window = window
        self.game_width = 600
        self.game_height = 800
        self.window_width = 600
        self.window_height = 1000
        self.side1 = Side(window, grass, 'top')
        self.side2 = Side(window, grass, 'bottom')
        self.selector = CardSelector(window, self)
        self.characters = []

    # check if card is being moved
    def update(self, event):
        self.selector.update(event)

    def draw(self):
        self.side1.draw()
        self.side2.draw()
        self.selector.draw()

        # draw any characters on the screen
        if not len(self.characters) == 0:
            for character in self.characters:
                character.move()

            for character in self.characters:
                character.attack()

            for character in self.characters:
                character.draw()