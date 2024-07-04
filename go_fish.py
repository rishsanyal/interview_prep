import random

from deck import Deck
from player import Player

NUM_DISTRUBTE_CARDS = {
   2: 7,
   3: 7,
   4: 5,
   5: 5
}

class GoFish(object):
    def __init__(self, num_players=5) -> None:
        self.book_counter = 0
        self.num_turns = 0

        self.deck = Deck()
        self.deck.shuffle()

        self.players = num_players

        self.player_hands = []

        for _ in range(self.players):
            self.player_hands.append(
                Player()
            )

    # def __play(self):

    def game(self):

        ## Everyone draws cards
        for player in self.player_hands:
            for _ in range(NUM_DISTRUBTE_CARDS[self.players]):
                player.draw(self.deck)

        for player in self.player_hands:
            cards = player.get_card_by_val(4)

            for card in cards:
                player.remove_card(card)
                self.book_counter += 1

            player.print_hand()

        print("Start playing the game")

        ## Start playing from the first player
        curr_player_index = 0
        next_player_index = curr_player_index + 1

        while self.book_counter <= 13 and self.num_turns < 3000:
            self.num_turns += 1

            ## If next_player doesn't have it
            ## move curr_player_index and next_player_index by 1

            ## If next_player has it,
            ## We check for book_counter in player_hand
            ## we keep asking the next_player for a diff card

            curr_player = self.player_hands[curr_player_index]
            next_player = self.player_hands[next_player_index]

            # print(curr_player_index, next_player_index)
            # print(curr_player.hand)
            # print(next_player.hand)
            # print("\n")
            ## The player asks the next_player for a card in the player's hand
            ## Get random element from keys

            # curr_card_request = curr_player.get_random_card()
            curr_card_request, curr_card_count = curr_player.get_greatest_card()

            if curr_card_count == 4:
                curr_player.remove_card(curr_card_request)
                self.book_counter += 1

                print("Player {} has a Fish of {}".format(curr_player_index, curr_card_request))
                continue

            if not curr_card_request:
                curr_player_index = (curr_player_index + 1) % self.players
                next_player_index = (next_player_index + 1) % self.players
                continue

            if next_player.check(curr_card_request):
                next_player_card_count = next_player.get_card_num(curr_card_request)
                next_player.remove_card(curr_card_request)

                curr_player.take_card(curr_card_request, next_player_card_count)

                fish_cards = curr_player.get_card_by_val(4)

                for card in fish_cards:
                    curr_player.remove_card(card)
                    self.book_counter += 1

            else:
                if not self.deck.isEmpty():
                    curr_player.draw(self.deck)

                curr_player_index = (curr_player_index + 1) % self.players

            next_player_index = (next_player_index + 1) % self.players

            if next_player_index == curr_player_index:
                next_player_index = (next_player_index + 1) % self.players

        if self.num_turns >= 100:
            for p in self.player_hands:
                p.print_hand()

        print(self.num_turns)



currGame = GoFish()
currGame.game()
