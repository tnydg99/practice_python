"""
This module setups and conducts the blackjack game
"""

from functools import reduce
from player import Human, Dealer
from deck import Deck


class Game():
    """
    This is the Game class
    """
    players = []

    def play_round(self):
        """
        This method plays a round of blackjack
        """
        deck = Deck()

        #show current players
        for player in self.players:
            print(
                f'Player name: {player.name}\nPlayer bankroll: ${player.bankroll}\n')

        # ask players for bets
        list(map(self.ask_for_bets, self.players))

        # shuffle the deck and pass out cards
        self.shuffle_and_pass(deck, self.players)

        # show round state
        print('\n')
        print(*self.players, sep='\n\n')

        # ask players to hit until they choose to stay
        print('\n')
        self.pass_or_play(deck, self.players)

        # let dealer play and determine winners
        self.determine_winners(self.players[-1], self.players, deck)

        # reset round
        self.conclude_round(self.players)

    def add_players(self):
        """
        This method adds players to the game
        """
        while True:
            try:
                number_of_players = int(
                    input('How many players are playing? Please enter a number: '))
                if number_of_players <= 0:
                    print('Please enter a valid number of players!')
                    continue
                break
            except ValueError:
                print('\nPlease enter a number!\n')
                continue

        for number in range(number_of_players):
            while True:
                try:
                    name = input(
                        f'\nPlayer {number + 1}, please enter in your name: ')
                    bankroll = float(
                        input('Please enter the amount you would like to play with: '))
                    self.players.append(Human(name, bankroll))
                except TypeError:
                    print('Please enter in a valid value for a bankroll!')
                    continue
                break
        self.players.append(Dealer())

    def shuffle_and_pass(self, deck, players):
        """
        This method shuffles the deck and passes cards to the players
        """
        try:
            deck.shuffle()
            for loop_count in range(2):
                for player_count in range(len(players)):
                    players[player_count].hand.append(deck.deck.pop(0))
                    if loop_count == 1 and player_count == len(players) - 1:
                        players[player_count].hide_card()
        except IndexError:
            print('There are no cards in the deck!')

    def ask_for_bets(self, player):
        """
        This method asks for player bets
        """
        player.bet()

    def pass_or_play(self, deck, players):
        """
        This method conducts a player hitting and standing
        """
        for player_count in range(len(players) - 1):
            standing = False
            while not standing and not players[player_count].out_of_round:
                hand, hand_total = self.present_hand(
                    players[player_count].hand)
                players[player_count].round_total = hand_total
                print(
                    f'{players[player_count].name} currently has {hand}')
                standing = players[player_count].stand()
                if standing:
                    print(
                        f'{players[player_count].name} is standing with a {hand_total}\n')
                    break
                else:
                    _ = self.player_hit(deck, players[player_count])

    def player_hit(self, deck, player):
        """
        This method lets the player take a hit
        """
        player.hit(deck.deck)
        _, hand_total = self.present_hand(player.hand)
        print(
            f'{player.name} has hit a {player.hand[-1].rank} of {player.hand[-1].suit}.\n')
        if hand_total > 21:
            player.out_of_round = True
            print(
                f"{player.name} has bust with a total of {hand_total}.")
        return hand_total

    def present_hand(self, hand):
        """
        This method presents the hand of a player
        """
        hand_string = ''
        hand_total = 0
        has_aces = False
        for card in hand:
            hand_total += card.value
            hand_string += f'{card.rank} of {card.suit} and '
            has_aces = has_aces or card.rank == 'Ace'
        if hand_total > 21 and has_aces:
            hand_total -= 10
        hand_string = hand_string[:-5]
        hand_string += ', totaling ' + str(hand_total) + '.'
        return hand_string, hand_total

    def determine_winners(self, dealer, players, deck):
        """
        This method conducts the dealer's turn and determines the winners of the round
        """
        dealer.reveal_card()
        print(
            f'{dealer.name} currently has {reduce(lambda x, y: x.rank + " of " + x.suit + " and " + y.rank + " of " + y.suit, dealer.hand)}\n')
        for card in dealer.hand:
            dealer.round_total += card.value
        while dealer.round_total < 17:
            dealer.round_total = self.player_hit(deck, dealer)
            hand, hand_total = self.present_hand(dealer.hand)
            dealer.round_total = hand_total
            print(
                f'{dealer.name} currently has {hand}')
        print(f'{dealer.name} is standing with a {dealer.round_total}.\n')
        for player_count in range(len(players) - 1):
            if not players[player_count].out_of_round and players[player_count].round_total == dealer.round_total and dealer.round_total == 21:
                players[player_count].bankroll += players[player_count].round_bet
                print(
                    f'{players[player_count].name}, you have pushed.\n')
            elif not players[player_count].out_of_round and (players[player_count].round_total >= dealer.round_total or dealer.out_of_round):
                players[player_count].bankroll += players[player_count].round_bet * 2
                print(
                    f'Congrats {players[player_count].name}, you have won ${players[player_count].round_bet * 2} with a {players[player_count].round_total}!\n')
            else:
                print(
                    f'{players[player_count].name}, you have lost this round with a {players[player_count].round_total}.\n')

    def conclude_round(self, players):
        """
        This method resets the round
        """
        delete_list = []
        self.reset_player(players[-1])
        for player_count in range(len(players) - 1):
            while True:
                choice = input(
                    f'{players[player_count].name}, would you like to continue playing? Enter Yes or No: ')
                if choice.lower() in ('yes', 'y', 'no', 'n'):
                    break
                else:
                    print('Please enter a valid value')
                    continue
            if choice.lower() in ('no', 'n'):
                print(
                    f'{players[player_count].name} has left the game with ${players[player_count].bankroll}.')
                delete_list.append(player_count)
            else:
                self.reset_player(players[player_count])
        for player_index in reversed(delete_list):
            del players[player_index]

    def reset_player(self, player):
        """
        This method resets a given player
        """
        player.hand.clear()
        player.round_bet = 0
        player.out_of_round = False
        player.round_total = 0
