# Game activity - may not need to be a class
from human_player import HumanPlayer
from computer_player import ComputerPlayer


# Set up number and type of players
def game_setup():
    game_player = []
    number_of_players = input('How many players (2 or 4)?: ')
    counter = 0
    while counter < int(number_of_players):
        valid_entry = False
        while not valid_entry:
            player_type = input(f'Player {counter + 1}, what type of player shall you be (H=Human, A=AI)?:')
            if player_type == 'H':
                game_player.append( HumanPlayer('', counter))
                valid_entry = True
            elif player_type == 'A':
                game_player.append(ComputerPlayer('', counter))
                valid_entry = True
            else:
                print('I did not understand your choice. Please try again.')
        counter += 1


# Set up size of game board
def get_board_size():
    board_size_str = input('Will the board be 10x10 or 20x20 squares (10/20)?: ')
    board_size = int(board_size_str)
    return board_size


# Helper function to convert a letter to its numerical equivalent (1-26)
def letters_to_numbers(letter):
    number = ord(letter) - 96
    return number
