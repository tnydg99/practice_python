"""
This module defines the players of the game
"""

from functools import reduce
from deck import Card

class Player():
    """
    This is the Player base class
    """
    hand = []
    round_total = 0
    round_bet = 0
    out_of_round = False

    def __init__(self, name='Dealer', bankroll=0):
        self.name = name
        self.bankroll = bankroll
        self.hand = list()

    def __str__(self):
        return f'Player name: {self.name}\nPlayer bankroll: ${self.bankroll}\nPlayer current hand: {reduce(lambda x, y: x.rank + " of " + x.suit + " and " + y.rank + " of " + y.suit, self.hand)}\nPlayer current bet: ${self.round_bet}'

    def __del__(self):
        print('\nPlayer deleted.')

    def bet(self):
        return self.name, self.round_bet

    def hit(self, deck):
        """
        This method lets the player get a new card to their hand
        """
        try:
            self.hand.append(deck.pop(0))
        except IndexError:
            print('There are no more cards in the deck!')

    def stand(self):
        """
        This method lets the player stand on their card amount
        """
        while True:
            choice = input(
                f'\n{self.name}, would you like to stand? Enter Yes or No: ')
            if choice.lower() in ('yes', 'y', 'no', 'n'):
                break
            else:
                print('Please enter a valid value')
                continue
        return choice.lower() in ('yes', 'y')


class Human(Player):
    """
    This is the Human class to simulate a human
    """

    def bet(self):
        """
        This method lets the human player bet an amount of money
        """
        while True:
            try:
                self.round_bet = float(
                    input(f'{self.name}, please enter an amount to bet for this round: '))
                if self.round_bet > self.bankroll:
                    print('You have bet more than you have!')
                    continue
                if self.round_bet <= 0:
                    self.out_of_round = True
                else:
                    self.bankroll -= self.round_bet
                break
            except TypeError:
                print('Please enter in a valid bet!')
                continue
            except ValueError:
                print('Please enter in a valid bet!')
        return self.name, self.round_bet


class Dealer(Player):
    """
    This is the Dealer class to simulate the computer
    """
    hidden_card_value = Card()

    def __str__(self):
        return f'Player name: {self.name}\nPlayer current hand: {reduce(lambda x, y: x.rank + " of " + x.suit + " and " + y.rank + " of " + y.suit, self.hand)}'

    def hide_card(self):
        """
        This method hides the card value of one of the cards in the hand
        """
        try:
            self.hidden_card_value = self.hand[1]
            self.hand[1] = Card()
        except IndexError:
            print('The dealer does not have enough cards!')

    def reveal_card(self):
        """
        This method reveals the hidden card value of the dealer's hand
        """
        self.hand[1] = self.hidden_card_value
        self.hidden_card_value = Card()
