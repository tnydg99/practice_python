"""
This module is for defining the deck of cards
"""

import random


class Card():
    def __init__(self, suit='X', rank='X', value=0):
        self.suit = suit
        self.rank = rank
        self.value = value

    def __str__(self):
        return f'{self.rank} of {self.suit}'


class Deck():
    values = {'Ace': 11, 'King': 10, 'Queen': 10,
              'Jack': 10, 'Ten': 10, 'Nine': 9, 'Eight': 8,
              'Seven': 7, 'Six': 6, 'Five': 5, 'Four': 4,
              'Three': 3, 'Two': 2}
    ranks = ['Ace', 'King', 'Queen', 'Jack', 'Ten', 'Nine', 'Eight',
             'Seven', 'Six', 'Five', 'Four', 'Three', 'Two']
    suits = ['Clubs', 'Diamonds', 'Hearts', 'Spades']
    deck = []

    def __init__(self):
        for suit in self.suits:
            for rank in self.ranks:
                value = self.values[rank]
                self.deck.append(Card(suit, rank, value))

    def shuffle(self):
        """
        This method shuffles the deck
        """
        random.shuffle(self.deck)
