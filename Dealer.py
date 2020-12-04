from hand import Hand
from deck import Deck
from Card import Card
class Dealer(Deck):
    def __init__(self, dealer= False):
        self.dealer = dealer
    #This is accessing deal method in Deck class
    def deal(self):
        self.deal()

    def display(self):
        if self.dealer:
            print("hidden")
            print(self.cards[1])

    def add_card(self, card):
        self.cards.append(card)
