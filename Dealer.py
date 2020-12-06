from Hand import Hand
from Deck import Deck
from Card import Card
class Dealer(Deck, Hand):
    def __init__(self, dealer= False):
        self.dealer = dealer

    #Display the dealers cards
    def display(self):
        if self.dealer:
            print("hidden")
            print(self.cards[1])
    #This will add a card to the player
    def add_card(self, card):
        self.player_hand.append(card)
    
