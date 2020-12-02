import random
from Card import Card
class Deck:
    def __init__(self):
        #This assigns the suits to variable s and the values to variable v
        self.cards = [Card(s,v) for s in ["Spades", "Clubs", "Hearts", "Diamonds"]
                                 for v in ["Ace", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King"]]

    def shuffle(self):
        # we want to have at least 2 cards otherwise there's nothing to shuffle
        if len(self.cards) > 1:
            random.shuffle(self.cards)

    def deal(self):
        if len(self.cards) > 1:
            # when we deal a card, we want to remove
            # it from the list so that we don't deal the same card twice
            return self.cards.pop(0)
    
deck1 = Deck()

deck1.shuffle()
print (deck1.deal())