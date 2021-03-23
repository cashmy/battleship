from shot_board import ShotBoard
from fleet_board import FleetBoard


class Player:

    def __init__(self, name, player_number, board_size):
        self.name = self.validate_name(name, player_number)
        self.player_number = player_number  # Player number in the game (1-4)
        self.fleet = ''  # Stores ships and each ships status
        self.shot_board = ShotBoard(board_size)  # Record of players hits against opponent
        self.fleet_board = FleetBoard(board_size)  # stores fleet location and opponent's hits

    @staticmethod
    def validate_name(name, player_number):
        if not name or name == '':
            name = input(f'Player {player_number+1}, what is your name?: ')
        return name
