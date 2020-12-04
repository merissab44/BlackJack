from Card import Card
from dealer import Dealer
class Hand(Dealer):
    def __init__(self):
        self.cards = []
        self.value = 0

    def calculate_value(self):
        has_ace = False
        for card in self.cards:
            if card.value.isnumeric():
                self.value += int(card.value)
            else:
                if card.value == "A":
                    has_ace = True
                    self.value += 11

        if has_ace and self.value > 21:
            self.value -= 10

    def get_value(self):
        self.calculate_value()
        return self.value

    def display(self):
        if self.dealer:
            print(self.dealer.display())
        else:
            for card in self.cards:
                print(card)
                print("Value: ", self.get_value())