import random 

class Card:
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value

    # This changes how we print out the card string
    def show(self):
        print (f"{self.value} of {self.suit}")
