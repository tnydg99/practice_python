"""
This program simulates the game Blackjack
"""

from game import Game


def main():
    """
    This is the main function
    """
    print('\nWelcome to Blackjack!\n')
    game = Game()
    game.add_players()
    while len(game.players) > 1:
        game.play_round()


if __name__ == "__main__":
    main()
