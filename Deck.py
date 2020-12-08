import random
from Card import Card
class Deck:
    def __init__(self):
        #This will hold our deck of cards
        self.cards = []
        self.build_deck()
        self.shuffle()
        #This will loop through both list and we will get a deck of every pair
    def build_deck(self):
        for suit in ["Spades", "Clubs", "Hearts", "Diamonds"]:
            for value in ["Ace", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King"]:
                self.cards.append(Card(suit,value))

    #This randomizes the suits and values in the deck 
    def shuffle(self):
        # we only shuffle at teh beginning of 
        # each round so we want to have 52 cards when we shuffle
        while len(self.cards) == 52:
            return random.shuffle(self.cards)
    #This returns the top card of the deck and removes it from the deck list
    def deal(self):
        card = self.cards.pop(0)
        return card
    
