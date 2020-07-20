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
        self.value = values[rank]

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
        try:
            option = input("What's your move, h for hit or s for stand? ").lower()
        except:
            print("Please enter a valid selection.")
        else:
            if option[0] == 'h':
                # hand.add_card(deck.deal())
                # hand.adjust_aces()
                hit(deck,hand)
            elif option[0] == 's':
                print("Player stands... dealer's turn.")
                playing = False
            else:
                print("Please enter a valid selection.")
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