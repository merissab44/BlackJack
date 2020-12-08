class Player:
    def __init__(self, dealer = False):
        #hand will hold our cards
        self.hand = []
        self.score = 0
        self.dealer = dealer

    #This will hold the current sum of the cards in the players hand
    def calculate_hand(self):
        self.score = 0
        for card in self.hand:
            #The .isnumeric returns a bool if the input is numeric or not
            if card.value.isnumeric():
                self.score += int(card.value)
            #checks the score to determine whether ace is a 1 or 11
            elif card.value == "Ace":
                if self.score <= 10:
                    self.score += 11
                elif self.score > 10:
                    self.score += 1
            else:
                self.score += 10
        return self.score
    #returns the current hand
    def get_hand(self):
        return self.score
    #adds the dealt card to players hand
    def add_card(self, card):
        self.hand.append(card)
    #if it's the dealers card, we want to hide it until end of game
        if self.dealer:
            print(f"Dealer's cards are hidden")
        return self.hand
    # Shows the total score
    def show_hand(self):
        print("Your total: ", self.calculate_hand())
        return self.hand
