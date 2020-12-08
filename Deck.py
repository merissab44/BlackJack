import random
from Card import Card
class Deck(Card):
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
        # print("Deck has been built")
    #This randomizes the suits and values in the card 
    def shuffle(self):
        # we want to have at least 2 cards otherwise there's nothing to shuffle
        while len(self.cards) == 52:
            return random.shuffle(self.cards)
    
    def deal(self):
        card = self.cards.pop()
            # self.hand.append(self.cards.pop(0))
        return card
    
        
    #show the deck
    def show(self):
        for card in self.cards:
            print(card)
# if __name__ == "__main__":
#     deck = Deck()
#     # deck.build_deck()
#     # deck.shuffle()
#     deck.deal()
#     # print(f"Your hand is: ")
#     # deck.show()
#     print("----------------")
#     deck.deal()
#     deck.show()
