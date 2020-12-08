class Player:
    def __init__(self, dealer = False):
        self.hand = []
        self.score = 0
        self.dealer = dealer

    #This will hold the current sum of the cards in the players hand
    def calculate_hand(self):
        self.score = 0
        for card in self.hand:
            #The .isnumeric returns a bool if the input is numeric or not
            # print(card)
            if card.value.isnumeric():
                self.score += int(card.value)
            elif card.value == "Ace":
                if self.score <= 10:
                    self.score += 11
                elif self.score > 10:
                    self.score += 1
            else:
                self.score += 10
        return self.score

    def get_hand(self):
        return self.score
    def add_card(self, card):
        # print(self.deal())
        self.hand.append(card)
        if self.dealer:
            print(f"Dealer's cards are hidden")
        return self.hand

    def show_hand(self):
        print("Your total: ", self.calculate_hand())
        return self.hand

# if __name__ == "__main__":
#     player = Player()
    # player.build_deck()
    # player.shuffle()
    # player.hit()