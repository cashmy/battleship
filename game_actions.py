# Game activity - may not need to be a class
from human_player import HumanPlayer
from computer_player import ComputerPlayer
# import letters_to_numbers

game_player = []


# Set up number and type of players
def game_setup():
    global number_of_players

    board_size = get_board_size()
    number_of_players = input('How many players (2 or 4)?: ')
    counter = 0
    while counter < int(number_of_players):
        valid_entry = False
        while not valid_entry:
            player_type = input(f'\nPlayer {counter + 1}, what type of player shall you be (H=Human, A=AI)?: ')
            if player_type == 'H':
                game_player.append(HumanPlayer('', counter, board_size))
                valid_entry = True
            elif player_type == 'A':
                game_player.append(ComputerPlayer('', counter, board_size))
                valid_entry = True
            else:
                print('I did not understand your choice. Please try again.')
        counter += 1


# Set up size of game board
def get_board_size():
    board_size = 10
    valid_entry = False
    while not valid_entry:
        board_size_str = input('Will the board be 10x10 or 20x20 squares (10/20)?: ')
        if board_size_str == '10' or board_size_str == '20':
            board_size = int(board_size_str)
            valid_entry = True
        else:
            print('I did not understand your choice. Please try again.')
    return board_size


# run the game turn
def game_turn():
    turn_counter = 1
    game_over = False
    while not game_over:
        print(f'==================== TURN {turn_counter} ====================')
        index = 0
        for player in game_player:
            print(f'*** {player.name} *** your shot board looks like this: ')
            player.shot_board.print_board()
            print('And your fleet board looks like this:')
            player.fleet_board.print_board()
            print('\n')
            opponent_index = determine_opponent(index)
            player.determine_shot(game_player[opponent_index])
            index += 1
            input('When ready press the enter key for the next player')
            clear()
        turn_counter += 1
        game_over = True


# Pycharm console clear screen simulation
def clear():
    counter = 0
    while counter <= 69:
        print('\n')
        counter += 1


def determine_opponent(index):
    # For a two opponent game 0 vs 1 and 1 vs 0
    if number_of_players == '2':
        if index == 0:
            return 1
        else:
            return 0
    else:  # number of players = 4
        if index == 0:
            return 2
        elif index == 1:
            return 3
        elif index == 2:
            return 0
        elif index == 3:
            return 1
