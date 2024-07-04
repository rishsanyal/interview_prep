import random

class Card:
    def __init__(self, val):
        self.val = val

    def __eq__(self, value):
        return self.val == value.val

    def __hash__(self):
        return hash(self.val)

    def __str__(self):
        return str(self.val)

    def __repr__(self) -> str:
        return str(self.val)

class Deck(object):

    def __init__(self) -> None:
        self.cards = []

        self.create_deck()

    def create_deck(self):
        for i in range(1, 14):
            for _ in range(4):
                self.cards.append(Card(i))

    def shuffle(self):
        random.shuffle(self.cards)

    def isEmpty(self):
        return len(self.cards) == 0

    def draw(self):
        if len(self.cards) == 0 or not self.cards:
            raise IndexError("The deck is empty.")

        return self.cards.pop()



