import random 

class Card:
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value

    # Override the str class This changes how we print out the card string
    def __str__(self):
        return (f"{self.value} of {self.suit}")
    '''
    When we have a hand, we are holding card objects. Instead of the program printing 
    the actual object location, we want it to print what the card is. So we override the 
    repr class to make the objects print like the string method does. When we print the
    card objects it will look like (Ace of Hearts)
    '''
    def __repr__(self):
        return (self.__str__())