import random

# list for card numbers
CARD_NUMBERS = ['Ace', '2', '3', '4', '5','6','7','8','9','10','Jack','Queen','King']
# create a list of tuples, where each tuple contains a single card number, using a list comprehension
SHUFFLED_DECK = [(card) for card in CARD_NUMBERS]

#shuffles cards
random.shuffle(SHUFFLED_DECK)

def card_value (card, selected_hand) ->int:
    """
    Gives a value to each card, giving 10 to each face card (Jack, Queen, King),
    1 or 11 to aces, depending on if the max hand value will exceed 21, and gives 
    number cards their normal displayed value

    :param card: one of the cards in hand
    :param selected_hand: the selected hand, either player_hand or dealer_hand
    """
    if card == 'Ace':
        if hand_value(selected_hand) + 11 <= 21:
            return 11
        else:
            return 1
    elif card in ['Jack', 'Queen', 'King']:
        return 10
    else:
        return int(card)
    

def hand_value(card_list):
    """
    Checks the total value of the cards in a hand and returns that total value
    
    :param selected_hand: The selected hand, either player or dealer
    """

    card_count = 0
    for card in card_list:
        card_count += card_value(card, card_list)
    return card_count


class BlackjackGame:
    """
    Plays a game of blackjack with the user. The dealer is played by the computer.
    """
    def __init__(self):
        """
        Initializes the player's hand and the dealer's hand as empty lists.
        """
        self.player_hand = []
        self.dealer_hand = []
    
    def play(self):
        """
        Starts game of blackjack
        """

        play_game = input("Do you want to play a game of blackjack? Type 'y' or 'n': ").lower()
    
        if play_game == 'y':
            
            # The two lines of code bellow are equivalent to:
            # card1 = SHUFFLED_DECK.pop()
            # card2 = SHUFFLED_DECK.pop()
            #Popped two cards from the deck *SHUFFLED_DECK*
            # self.player_hand.append(card1)
            # self.player_hand.append(card2)
            #Added the popped cards to the player hand
            # card3 = SHUFFLED_DECK.pop()
            # card4 = SHUFFLED_DECK.pop()
            #Popped two more cards from the deck *SHUFFLED_DECK*
            # self.dealer_hand.append(card3)
            # self.dealer_hand.append(card4)
            #Added cards to the dealer hand
            
        
        # Gives two cards to the player and two cards to the dealer
            self.player_hand.extend([SHUFFLED_DECK.pop(), SHUFFLED_DECK.pop()])
            self.dealer_hand.extend([SHUFFLED_DECK.pop(), SHUFFLED_DECK.pop()]) 
            
            while play_game == 'y':

                print(f"\nYour cards: {self.player_hand}")
                print(f"\nDealer's first card: {self.dealer_hand[0]}")

                while hand_value(self.player_hand) < 22:
                    hit_or_stand = input("Do you want to hit or stand? Type 'h' or 's': \n").lower()
                    if hit_or_stand == 'h':
                        #Adds one more card to the player hand
                        self.player_hand.append(SHUFFLED_DECK.pop())
                        print(f"\nYour cards: {self.player_hand}\n")
                    else:
                        break   
                
                #Checks if player hand value is above the limit (21)
                if hand_value(self.player_hand) > 21:
                    print(f"Your final hand: {self.player_hand}")
                    print(f"Dealer's final hand: {self.dealer_hand}")
                    print("\nYou busted! Dealer wins")
                    break
                
                #Checks who was the highest score bellow 21, between dealer and player    
                elif hand_value(self.dealer_hand) < hand_value(self.player_hand) <= 21:
                    print(f"Your final hand: {self.player_hand}")
                    print(f"Dealer's final hand: {self.dealer_hand}")
                    print("\nYou win!")
                    break
                
                elif hand_value(self.dealer_hand) == hand_value(self.player_hand):
                    print(f"Your final hand: {self.player_hand}")
                    print(f"Dealer's final hand: {self.dealer_hand}")
                    print("\nDraw!")
                    break
                    
                else:
                    print(f"Your final hand: {self.player_hand}")
                    print(f"Dealer's final hand: {self.dealer_hand}")
                    print("\nDealer wins.")
                    break
                
        print("Thanks for playing!")
            
    
if __name__ == "__main__":
    game = BlackjackGame()
    game.play()
    