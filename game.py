import random

money = 0
bet = 0
stand = False
hit = False

suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 'Nine':9, 'Ten':10, 'Jack':10, 'Queen':10, 'King':10, 'Ace':11}

class Card:

    '''
    Output: card type by suit and rank
    '''

    def __init__(self, suit, rank):

        self.suit = suits
        self.rank = rank
        self.value = values[rank]

    def __str__(self):
        return f'{self.rank} of {self.suit}'


class Deck:

    '''
    Output: handles shuffling and dealing of cards in deck
    '''

    def __init__(self):
        self.all_cards = []
        for suit in suits:
            for rank in ranks:
                self.all_cards.append(Card(suit,rank))

    def shuffle(self):
        # shuffles cards in place
        random.shuffle(self.all_cards)

    def deal(self):
        return self.all_cards.pop()