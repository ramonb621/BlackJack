import random

suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 'Nine':9, 'Ten':10, 'Jack':10, 'Queen':10, 'King':10, 'Ace':11}

playing = True

class Card:

    '''
    OUTPUT: Card type by suit and rank
    '''

    def __init__(self, suit, rank):

        self.suit = suit
        self.rank = rank
        # self.value = values[rank]

    def __str__(self):
        return f'{self.rank} of {self.suit}'


class Deck:

    '''
    OUTPUT: Handles shuffling and dealing of cards in deck
    '''

    def __init__(self):
        self.deck = []
        for suit in suits:
            for rank in ranks:
                self.deck.append(Card(suit,rank))

    def shuffle(self):
        # shuffles cards in place
        random.shuffle(self.deck)

    def deal(self):
        # grabs a card from deck list
        return self.deck.pop()


class Hand:

    '''
    OUTPUT: Adds a card to players hand and adjusts value of aces to either 1 or 11 depending on if hand is over 21
    '''

    def __init__(self):
        self.cards = []
        self.value = 0
        self.aces = 0

    def add_card(self, card):
        self.cards.append(card)
        self.value += values[card.rank]
        if card.rank == 'Ace':
            self.aces += 1

    def adjust_aces(self):
        while self.value > 21 and self.aces:
            self.value -= 10
            self.aces-= 1


class Chips:

    '''
    OUTPUT: Keeps track of bets and wins
    '''

    def __init__(self):
        self.total = 100
        self.bet = 0

    def win_bet(self):
        self.total += self.bet

    def lose_bet(self):
        self.total -= self.bet 


def take_bet(chips):

    '''
    OUTPUT: Will take in a bet using chips class
    '''

    while True:

        try:
            chips.bet = int(input("How many chips do you wnat to bet? "))
        except:
            print("Please provide an integer.")
        else:
            if chips.bet > chips.total:
                print(f"You don't have enough chips to place this bet. Chips available: {chips.total}")
            else:
                break

def hit(deck, hand):

    '''
    OUTPUT: Will take card from the deck, add it to the players hand, and check for aces in the hand.
    '''

    hand.add_card(deck.deal())
    hand.adjust_aces()

def hit_stand(deck, hand):
    global playing

    '''
    OUTPUT: will take in players input to see if they want a hit or stand. If player wants a hit, the hit function is called.
    '''

    while True:

        option = input("What's your move, h for hit or s for stand? ").lower()

        if option[0] == 'h':
            # hand.add_card(deck.deal())
            # hand.adjust_aces()
            hit(deck,hand)
        elif option[0] == 's':
            print("Player stands... dealer's turn.")
            playing = False
        else:
            print("Please enter a valid selection.")
            continue
        break

def show_some(player,dealer):
    print("\nDealer's Hand:")
    print(" <card hidden>")
    print('',dealer.cards[1])  
    print("\nPlayer's Hand:", *player.cards, sep='\n ')
    
def show_all(player,dealer):
    print("\nDealer's Hand:", *dealer.cards, sep='\n ')
    print("Dealer's Hand =",dealer.value)
    print("\nPlayer's Hand:", *player.cards, sep='\n ')
    print("Player's Hand =",player.value)

def player_busts(player,dealer,chips):
    print("Player busts!")
    chips.lose_bet()

def player_wins(player,dealer,chips):
    print("Player wins!")
    chips.win_bet()

def dealer_busts(player,dealer,chips):
    print("Dealer busts!")
    chips.win_bet()
    
def dealer_wins(player,dealer,chips):
    print("Dealer wins!")
    chips.lose_bet()
    
def push(player,dealer):
    print("Dealer and Player tie! It's a push.")


while True:
    print("Let's play some blackjack y'all!")

    
    # Create & shuffle the deck, deal two cards to each player
    new_deck = Deck()
    new_deck.shuffle()

    player_hand = Hand()
    player_hand.add_card(new_deck.deal())
    player_hand.add_card(new_deck.deal())

    dealer_hand = Hand()
    dealer_hand.add_card(new_deck.deal())
    dealer_hand.add_card(new_deck.deal())


    
        
    # Set up the Player's chips
    player_chips = Chips()
    
    
    # Prompt the Player for their bet
    print(f"Players chips: {player_chips.total}")
    take_bet(player_chips)

    
    # Show cards (but keep one dealer card hidden)
    show_some(player_hand, dealer_hand)
    
    while playing:  # recall this variable from our hit_or_stand function
        
        # Prompt for Player to Hit or Stand
        hit_stand(new_deck, player_hand)
        
        
        # Show cards (but keep one dealer card hidden)
        show_some(player_hand, dealer_hand)
        
        # If player's hand exceeds 21, run player_busts() and break out of loop
        if player_hand.value > 21:
            player_busts(player_hand, dealer_hand, player_chips)

            break

    # If Player hasn't busted, play Dealer's hand until Dealer reaches 17
    if player_hand.value <= 21:
        while dealer_hand.value < 17:
        # Alternative to above is below, dealer can keep playing until they beat player or busts...
        # while dealer_hand.value < player_hand.value:
            hit(new_deck, dealer_hand)
    
        # Show all cards
        show_all(player_hand, dealer_hand)
    
        # Run different winning scenarios
        if dealer_hand.value > 21:
            dealer_busts(player_hand, dealer_hand, player_chips)
        elif dealer_hand.value > player_hand.value:
            dealer_busts(player_hand, dealer_hand, player_chips)
        elif dealer_hand.value < player_hand.value:
            player_wins(player_hand, dealer_hand, player_chips)
        else:
           push(player_hand, dealer_hand) 
    
    # Inform Player of their chips total 
        print(f"Players winnings are at: {player_chips.total}")
    # Ask to play again
        rematch = input("Want to play again? y/n: ").lower()

        if rematch[0] == "y":
            playing = True
            continue
        else:
            print("Thanks for playing.")
            break