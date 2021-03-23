# Game activity - may not need to be a class
from player import Player


# Set up number of players
def game_setup():
    game_player = []
    number_of_players = input('How many players (2 or 4)?: ')
    counter = 1
    while counter <= int(number_of_players):
        game_player[counter] = Player()
        counter += 1


# Set up size of game board
def get_board_size():
    board_size_str = input('Will the board be 10x10 or 20x20 squares (10/20?: ')
    board_size = int(board_size_str)
    return board_size


# Helper function to convert a letter to its numerical equivalent (1-26)
def letters_to_numbers(letter):
    number = ord(letter) - 96
    return number
