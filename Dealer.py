from Player import Player
from Deck import Deck
class Dealer(Player):
    def __init__(self):
        Player.__init__(self, dealer = True)
        self.deck = Deck()
        # We're automating the build deck and shuffle method from the deck class
        self.deck.build_deck()
        self.deck.shuffle()

    def hit(self):
        return self.deck.deal()

    # This will reveals the dealers hand
    def reveal(self):
        print("Dealer's total: ", self.calculate_hand())
        return self.hand
