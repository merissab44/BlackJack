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
        # print(self.deal())
        # self.dealer_hand.append(self.deal())
        # # print(self.player_hand)
        # print(f"Your total is now: {self.get_value()}")
        # return self.dealer_hand
    
    #Display the dealers cards
    def display(self):
        print("hidden")
    # This will reveals the dealers hand
    def reveal(self):
        for card in self.hand:
            print(card)
# if __name__ == "__main__":
#     dealer = Dealer()
#     dealer.add_card(dealer.hit())
#     dealer.add_card(dealer.hit())
#     dealer.add_card(dealer.hit())
#     dealer.add_card(dealer.hit())
#     dealer.reveal()
    
