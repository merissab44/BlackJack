from Card import Card
from Hand import Hand
from Deck import Deck
from Dealer import Dealer
class Game:
    def __init__(self):
        pass

    def game_running(self):
        in_play = True
        while self.in_play:
            deck = Deck()
            deck.shuffle()
            players_cards = Hand()
            dealers_cards = Hand()
            # If either hand has 0 cards, deal a random card from the card list
            while len(player_hand, dealer_hand) < 1:
                player_hand = random.choice(deck)
                players_cards.append(player_hand) 

                dealer_hand = random.choice(deck)
                dealers_cards.append(dealer_hand) 
            # Show the hand and ask player to hit or stay
            print(f" Your hand is: {player_hand.show_hand()}")
            print(f"Dealer's hand is: {dealer_hand.show_hand()}")
            choice = input("Please choose [Hit / Stay] ").lower()
            while choice not in ["h", "s", "hit", "stay"]:
                choice = input("Please enter 'hit' or 'stay' (or H/S) ").lower()
            # If they hit, add card to their hand and update the score
            if choice == "hit" or choice == "h":
                player_hand.hit()
                player_hand.show_hand()
            else:
                #If they stay get each score and compare them
                player_hand_value = self.player_hand.get_value()
                dealer_hand_value = self.dealer_hand.get_value()

                print("Final Results")
                print("Your hand:", player_hand_value)
                print("Dealer's hand:", dealer_hand_value)
                #If player score is greater than dealer, player wins
                if player_hand_value > dealer_hand_value:
                    print("You Win!")
                elif player_hand_value == dealer_hand_value:
                    print("Tie!")
                else:
                    print("Dealer Wins!")
                    game_over = True
    #While the game is not over, check for a blackjack
    game_over = False
    while not game_over:
        player_has_blackjack, dealer_has_blackjack = self.check_blackjack()

    # Checks if player or dealer has reached 21
    def check_blackjack(self):
        player_blackjack = False
        dealer_blackjack = False
        if player_hand.get_hand() == 21:
            player_blackjack = True
        if dealer_hand.get_hand() == 21 or player_hand.get_hand > 21:
            dealer_blackjack = True
        return player_blackjack, dealer_blackjack
    # When game is overm ask to play again
    def is_game_over(self, player_has_blackjack, dealer_has_blackjack):
        if player_has_blackjack and dealer_has_blackjack:
            game_over = True
            print("Draw!")
        if player_has_blackjack:
            print("Dealer busted, you win!")
        if dealer_has_blackjack:
            print("The dealer wins")
        if game_over == True:
            play_again = input("Would you like to play again? Y/N ").lower()
            if play_again == "n":
                print("Thanks for playing BlackJack!")
                in_play = False
            else:
                game_over = False

if __name__ == "__main__":
    game = Game()
    game.game_running()