import random
from collections import OrderedDict

from deck import Deck, Card

class Player(object):
    def __init__(self) -> None:
        self.hand = OrderedDict()

    def draw(self, deck):
        curr_card = deck.draw()

        if curr_card.val not in self.hand:
            self.hand[curr_card.val] = 0

        self.hand[curr_card.val] += 1

    def check(self, card):
        hand_card_counter = self.hand.get(card.val, 0)

        if hand_card_counter == 0:
            return False

        return True

    def give_card(self, card):
        self.hand[card.val] -= 1

        if self.hand[card.val] <= 0:
            self.hand.pop(card.val)

        return card

    def take_card(self, card, card_num=1):
        if card.val not in self.hand:
            self.hand[card.val] = 0

        self.hand[card.val] += card_num

    def remove_card(self, card):
        self.hand.pop(card.val)

    def get_card_num(self, card):
        return self.hand.get(card.val, 0)

    def get_card_by_val(self, val):
        cards = []

        for card, card_count in self.hand.items():
            if card_count == val:
                cards.append(Card(card))

        return cards


    def print_hand(self):
        print(self.hand)

    def get_greatest_card(self):
        greatest_card = None
        greatest_card_count = 0

        if not self.hand:
            return None, 0

        # return self.hand.popitem(True)

        for card, card_count in self.hand.items():
            if card_count > greatest_card_count:
                greatest_card = card
                greatest_card_count = card_count

        return Card(greatest_card), greatest_card_count

    def get_random_card(self):

        if not self.hand:
            return None

        while True:
            rand_card = random.choice(list(self.hand.items()))
            rand_card_num = rand_card[0]

            if rand_card[1] != 0:
                return Card(rand_card_num)

            self.hand.pop(rand_card_num)


if __name__ == "__main__":
    deck = Deck()
    deck.shuffle()

    p = Player()

    for i in range(6):
        p.draw(deck)

    p.print_hand()
    # p.get_random_card()
    greatest_card, _ = p.get_greatest_card()
    print(greatest_card)
    p.remove_card(greatest_card)
    p.print_hand()






