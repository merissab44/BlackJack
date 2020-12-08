import random 

class Card:
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value

    # This changes how we print out the card string
    def __str__(self):
        val = self.value
        if val == "1" or val == "11":
            val = "Ace"
        return (f"{self.value} of {self.suit}")

    def __repr__(self):
        return (self.__str__())