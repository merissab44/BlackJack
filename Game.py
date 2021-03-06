import random
from Card import Card
from Player import Player
from Deck import Deck
from Dealer import Dealer

class Game:
    def __init__(self):
        # self.players_cards = []
        # self.dealers_cards = []

        self.player = Player()
        self.dealer = Dealer()
        self.deck = Deck()
        self.deck.build_deck()
        self.deck.shuffle()

    #This runs the game
    def game_running(self):
        in_play = True
        while in_play:
            deck = Deck()
            # If either hand has 0 cards, deal a random card from the card list
            while len(self.player.hand) < 1 and len(self.player.hand) < 1:
                player_first_card = deck.deal()
                self.player.add_card(player_first_card) 
                dealer_first_card = deck.deal()
                self.dealer.add_card(dealer_first_card) 
            # Show the hand and ask player to hit or stay
            print(f" Your hand is: {self.player.show_hand()}")
            # print(f"Dealer's hand is: {self.dealer.display()}")
            choice = input("Please choose [Hit / Stay] ").lower()
            while choice not in ["h", "s", "hit", "stay"]:
                choice = input("Please enter 'hit' or 'stay' (or H/S) ").lower()
            # If they hit, add card to their hand and update the score
            if choice == "hit" or choice == "h":
                #Deal a card to both player and dealer
                self.player.add_card(deck.deal())
                self.dealer.add_card(deck.deal())
                #This checks if dealer or player has blackjack
                player_blackjack, dealer_blackjack = self.check_blackjack()
                #If blackjack is True, this ends the game
                if player_blackjack or dealer_blackjack:
                    return player_blackjack, dealer_blackjack
            elif choice == "stay" or choice == "s":
                #If player has higher score, player wins
                if self.player.get_hand() > self.dealer.get_hand():
                    print("Your hand was higher, you win!")
                    print("Final Results")
                    print("Dealer's hand:", self.dealer.reveal())
                else:
                     #If dealer has higher score, dealer wins, and reveals their cards
                    print("You busted. The dealer wins")
                    print("Final Results")
                    print("Dealer's hand:", self.dealer.reveal())

    # Checks if player or dealer has reached 21 or if the player has higher hand
    def check_blackjack(self):
        player_blackjack = False
        dealer_blackjack = False
        players_hand = self.player.calculate_hand()
        dealers_hand = self.dealer.calculate_hand()
        if players_hand == 21 or dealers_hand > 21:
            player_blackjack = True
        if dealers_hand == 21 or players_hand > 21:
            dealer_blackjack = True
        return player_blackjack, dealer_blackjack

    # When game is over ask to play 
    # This method returns true or false if the player wants to play again
    def is_game_over(self, player_has_blackjack, dealer_has_blackjack):
        game_over = False
        # If this returns True then the game is over
        if player_has_blackjack and dealer_has_blackjack:
            game_over = True
            print("Draw!")
        if player_has_blackjack:
            game_over = True
            print("dealer busted. you win!")
            print(self.dealer.reveal())
            print(self.player.show_hand())
        if dealer_has_blackjack:
            game_over = True
            print(self.dealer.reveal())
            print(self.player.show_hand())
            print("You busted. The dealer wins")
        if game_over == True:
            play_again = input("Would you like to play again? Y/N ").lower()
            if play_again == "n":
                print("Thanks for playing BlackJack!")
                return True
            else:
                return False
#This will create a new game if the player wants to play again
if __name__ == "__main__":
    game_over = False
    while game_over == False:
        game = Game()
        player_blackjack, dealer_blackjack = game.game_running()
        game_over = game.is_game_over(player_blackjack, dealer_blackjack)