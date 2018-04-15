from random import randint

def set_active_player():
    rand_int = randint(1, 100)
    active_player = 'Player 1' if rand_int <= 50 else 'Player 2'
    
    print(f'{active_player} goes first!')
    return active_player

def set_active_marker():
    marker = None
    while marker == None:
         user_input = input('Select your piece: X or O\n')
         if user_input.lower() == 'x':
             marker = 'X'
         elif user_input.lower() == 'o':
             marker = 'O'
    return marker

def display_board(board):
    board_row_top = f'     |     |     |\n  {board[6]}  |  {board[7]}  |  {board[8]}  |     \n     |     |     |     \n-----------------------\n'
    board_row_mid = f'     |     |     |\n  {board[3]}  |  {board[4]}  |  {board[5]}  |     \n     |     |     |     \n-----------------------\n'
    board_row_bot = f'     |     |     |\n  {board[0]}  |  {board[1]}  |  {board[2]}  |     \n     |     |     |     \n'
    print(f'{board_row_top}{board_row_mid}{board_row_bot}')
    

def place_marker(board, marker, position):
    board[position] = marker

def win_check(board, mark):
    winning_positions = [ [0, 1, 2], [0, 3, 6], [0, 4, 8], [3, 4, 5], [1, 4, 7], [6, 7, 8], [2, 5, 8], [6, 4, 2] ]
    for position in winning_positions:
        marker_set = [board[index] for index in position]
        if marker_set == [mark, mark, mark]:
            return True
    return False

def space_available(board, position):
    return board[position] == ' '

def select_space(board, player):
    position = int(input(f'{player} - Select a space on the board (keys 0 - 8)\n'))
    valid_selection = space_available(board, position)
    if valid_selection:
        return position
    else:
        print('Selected space is unavailable\n')
        return select_space(board, player)

def replay():
    play_again = input('Would you like to play again? Y / N\n')
    if play_again.lower() == 'y':
        return True
    elif play_again.lower() == 'n':
        return False
    else:
        print('Invalid input. Please try again.\n')
        replay()

def clear_screen():
    print('\n' * 100)

print('Welcome to Tic Tac Toe!')

game_on = True
# Set up the board, decide which player is going first and which piece they want to be
board = [' '] * 9
active_player = set_active_player()
active_marker = set_active_marker()

# Inverse dictionaries used to swap markers and players
markers = { 'X': 'O', 'O': 'X' }
players = { 'Player 1': 'Player 2', 'Player 2': 'Player 1' }

while game_on:
    display_board(board)
    selected_position = select_space(board, active_player)
    place_marker(board, active_marker, selected_position)
    clear_screen()
    game_over = win_check(board, active_marker)
    if game_over:
        display_board(board)
        print(f'{active_player} wins!')
        game_on = False
    else:
        active_player = players[active_player]
        active_marker = markers[active_marker]
