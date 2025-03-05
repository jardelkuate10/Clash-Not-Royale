from card_selector import CardSelector
from side import Side

grass = (44, 134, 47)


class GameScreen:
    def __init__(self, window):
        self.window = window
        self.game_width = 600
        self.game_height = 800
        self.side1 = Side(window, grass, 'top')
        self.side2 = Side(window, grass, 'bottom')
        self.selector = CardSelector(window, self)
        self.characters = []

    def update(self, event):
        self.selector.update(event)

    def draw(self):
        self.side1.draw()
        self.side2.draw()
        self.selector.draw()

        if not len(self.characters) == 0:
            for character in self.characters:
                character.move()

            for character in self.characters:
                character.attack()

            for character in self.characters:
                character.draw()