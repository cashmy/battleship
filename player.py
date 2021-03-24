from shot_board import ShotBoard
from fleet_board import FleetBoard
import random


class Player:

    def __init__(self, name, player_number, board_size):
        self.name = self.validate_name(name, player_number)
        self.player_number = player_number  # Player number in the game (1-4)
        self.fleet = ''  # Stores ships and each ships status
        self.shot_board = ShotBoard(board_size)  # Record of players hits against opponent
        self.fleet_board = FleetBoard(board_size)  # stores fleet location and opponent's hits
        self.chosen_method = '1'  # Default to "random" for this games chosen method
        self.chosen_row = 0
        self.chosen_col = 0
        # ADDED FOR TEST - REMOVE for Production
        self.fleet_board.default_placement()

    @staticmethod
    def validate_name(name, player_number):
        if not name or name == '':
            name = input(f'Player {player_number+1}, what is your name?: ')
        return name

    def method_of_fleet_assignment(self):
        # An method that will require extension definition in child classes
        # A random method is available for all children
        pass

    def determine_shot(self, board_size, method_type, opponent_fleet_board):
        #  method_type:   "1" = random, "2" = User entry, "3" = AI calculation
        #  Method type is 1 is the only type defined in the parent class.
        #  This method will be overridden in the child classes to include the other options
        #  and the condition check, based upon the method_type will be used there.
        # Random method (to be inherited in child classes
        self.chosen_row = random.randint(0, board_size-1)
        self.chosen_col = random.randint(0, board_size-1)
        # hit = opponent_fleet_board.check_board(self.chosen_row, self.chosen_col)
        # self.shot_board.update_board(self.chosen_row, self.chosen_col, hit)
        pass
