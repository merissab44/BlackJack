import random
from Card import Card
class Deck:
    def __init__(self):
        #This will hold our deck of cards
        self.cards = []
        #This will loop through both list and we will get a deck of every pair
    def __build_deck(self):
        for suit in ["Spades", "Clubs", "Hearts", "Diamonds"]:
            for value in ["Ace", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King"]:
                self.cards.append(Card(suit,value))
    #This randomizes the suits and values in the card 
    def shuffle(self):
        # we want to have at least 2 cards otherwise there's nothing to shuffle
            random.shuffle(self.cards)
            return self.cards
    
    #show the deck
    def show(self):
        for card in self.cards:
            card.show()

    def deal(self):
        if len(self.cards) > 1:
            return self.cards.pop(0)
if __name__ == "__main__":
    deck = Deck()
    deck._Deck__build_deck()
    # print (deck.show())
