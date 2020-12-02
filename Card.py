import random 

class Card:
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value

    # This changes how we print out the card
    def __repr__(self):
        return " of ".join((self.value, self.suit))
