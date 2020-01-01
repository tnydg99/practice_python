def main():
    tic_tac_toe()
    
def tic_tac_toe():
    print("Welcome to Tic Tac Toe!")
    play_again = True
    players = {
        '1': {
            'symbol': '',
            'wins': 0,
            'losses': 0,
            'ties': 0,
            'turn_player': True
        },
        '2': {
            'symbol': '',
            'wins': 0,
            'losses': 0,
            'ties': 0,
            'turn_player': False
        }
    }
    while play_again:
        print(f'players = {players}')
        board = start_game(players)
        still_playing = input('Are you ready to play? Enter Yes or No: ').lower() in ('yes', 'y')
        turn_count = 1
        while still_playing:
            turn_player = '1' if players['1']['turn_player'] else '2'
            turn_player_symbol = players[turn_player]['symbol']
            print(display_board(board))
            if turn_count <= 9:
                ask_for_position(board, players, turn_player, turn_player_symbol)
                winner = has_won(board, turn_player, turn_player_symbol)
                if turn_player == winner:
                    still_playing = False
                    print(display_board(board))
                    play_again = end_game(players, turn_player, turn_count)
                else:
                    turn_count += 1
            else:
                still_playing = False
                play_again = end_game(players, turn_player, turn_count)
    
def start_game(players):
    valid_start = False
    while not valid_start:
        turn_player = '1' if players['1']['turn_player'] else '2'
        other_player = '2' if turn_player == '1' else '1'
        start_symbol = input(f'Player {turn_player} please select a symbol to play with (X or O): ')
        if start_symbol.lower() == 'x' or start_symbol.lower() == 'o':
            players[turn_player]['symbol'] = start_symbol.lower()
            players[other_player]['symbol'] = 'o' if players[turn_player]['symbol'] == 'x' else 'x'
            valid_start = True
        else:
            print('\nPlease enter a valid symbol!')
    return [[i + j + 1 for i in range(3)] for j in range(0, 7, 3)]

def display_board(symbol_positions):
    board = ''
    for row in range(3):
        board += '\n   |   |\n'
        for column in range(3):
            board += f' {symbol_positions[row][column]} |' if (column + 1) % 3 != 0 else f' {symbol_positions[row][column]} \n'
        board += '   |   |\n-----------' if (row + 1) % 3 != 0 else '   |   |\n'
    return board        

def ask_for_position(board, players, player, symbol):
    valid_move = False
    while not valid_move:
        try:
            position = int(input(f'Player {player}, please select an available position: '))
        except ValueError:
            print('Please enter a value between 1 and 9')
            continue
        if check_for_valid_move(position, board, symbol):
            valid_move = True
        else:
            print(f'Player {player}, that is not a valid move!\n')
    other_player = '2' if player == '1' else '1'
    players[player]['turn_player'] = False
    players[other_player]['turn_player'] = True

def has_won(board, player, symbol):
    #horizontal & vertical & diagonal
    diagonal_count = 0
    for row in range(3):
        row_count = 0
        column_count = 0
        for column in range(3):
            if board[row][column] == symbol:
                row_count += 1
            if board[column][row] == symbol:
                column_count += 1
            if (row + column) % 2 == 0 and board[row][column] == symbol:
                diagonal_count += 1
        if row_count == 3 or column_count == 3 or diagonal_count >= 3:
             break
    else:
        player = '2' if player == '1' else '1'
    return player

def end_game(players, winner, turn_count):
    loser = '2' if winner == '1' else '1'
    if turn_count >= 9:
        print(f'\nNobody won the game. Both players will receive a tie.')
        players[winner]['ties'] += 1
        players[loser]['ties'] += 1
    else:
        print(f'\nCongratulations Player {winner}, you have won the game! Player {loser}, better luck next time.')
        players[winner]['wins'] += 1
        players[loser]['losses'] += 1
        players[winner]['turn_player'] = False
        players[loser]['turn_player'] = True
    return input('\nWould you like to play again? Enter Yes or No: ').lower() in ('yes', 'y')

def check_for_valid_move(position, board, symbol):
    for row in range(3):
        for column in range(3):
            if board[row][column] == position:
                board[row][column] = symbol
                return True
        else:
            continue
        break
    else:
        return False

if __name__ == '__main__':
    main()