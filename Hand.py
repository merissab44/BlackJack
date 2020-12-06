from Card import Card
from Deck import Deck
from Dealer import Dealer
class Hand(Deck):
    def __init__(self, dealer = False):
        self.dealer = dealer
        self.player_hand = []
        self.value = 0

    #Add a card to our hand
    def add_card(self, card):
        self.player_hand.append(card)
    #This will hold the current sum of the cards in the players hand
    def calculate_hand(self):
        has_ace = False
        for card in self.player_hand:
            #The .isnumeric returns a bool if the input is numeric or not
            if card.value.isnumeric():
                self.value += int(card.value)
            elif card.value == "A":
                has_ace = True
                choice = input("Does this ace count as 1 or 11? ")
                if choice == "1":
                    self.value += 1
                else:
                    self.value += 11
            else:
                self.value += 10
    #Returns the value of the cards in the players hand
    def get_value(self):
        self.calculate_hand()
        return self.value

    def hit(self):
        print(f"Your total is now: {self.calculate_hand}")
        return self.player_hand.append(self.add_card(card))

    def show_hand(self):
        for card in self.player_hand:
            print(card)
            print(self.get_value())

if __name__ == "__main__":
    hand = Hand()
    hand.hit()