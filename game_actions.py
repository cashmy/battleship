# Game activity - may not need to be a class
from human_player import HumanPlayer
from computer_player import ComputerPlayer

game_player = []


# Set up number and type of players
def game_setup():
    board_size = get_board_size()
    number_of_players = input('How many players (2 or 4)?: ')
    counter = 0
    while counter < int(number_of_players):
        valid_entry = False
        while not valid_entry:
            player_type = input(f'Player {counter + 1}, what type of player shall you be (H=Human, A=AI)?: ')
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
    for player in game_player:
        print(f'*** {player.name} *** your shot board looks like this: ')
        player.shot_board.print_board()
        print('And your fleet board looks like this:')
        player.fleet_board.print_board()
        input('When ready press the enter key for the next player')
        print('\n')
        # clear()
    print(f'{game_player[0].name}, we will take a turn at F-7 (6,5)')
    hit = game_player[0].fleet_board.check_board(6, 5)
    game_player[0].shot_board.update_board(6, 5, hit)
    print(f'{game_player[0].name}, we will take a turn at F-6 (6,4)')
    hit = game_player[0].fleet_board.check_board(6, 4)
    game_player[0].shot_board.update_board(6, 4, hit)
    game_player[0].shot_board.print_board()


# Helper function to convert a letter to its numerical equivalent (1-26)
def letters_to_numbers(letter):
    number = ord(letter) - 96
    return number


# Pycharm console clear screen simulation
def clear():
    counter = 0
    while counter <= 69:
        print('\n')
        counter += 1
