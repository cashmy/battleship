from shot_board import ShotBoard
from fleet_board import FleetBoard
import random
import letters_to_numbers


class Player:

    def __init__(self, name, player_number, board_size):
        self.name = self.validate_name(name, player_number)
        self.player_number = player_number  # Player number in the game (1-4)
        self.fleet = ''  # Stores ships and each ships status
        self.shot_board = ShotBoard(board_size)  # Record of players hits against opponent
        self.fleet_board = FleetBoard(board_size)  # stores fleet location and opponent's hits

        self.target_method = '1'  # Default to "random" for this games chosen method
        #  chosen.method:   "1" = random, "2" = User entry, "3" = AI calculation
        #  Method type is 1 is the only type defined in the parent class.
        #  This method will be overridden in the child classes to include the other options
        self.ship_placement_method = '1'

        self.chosen_row = 0
        self.chosen_col = 0
        # ADDED FOR TEST - REMOVE for Production
        # self.fleet_board.default_placement()

    @staticmethod
    def validate_name(name, player_number):
        if not name or name == '':
            name = input(f'Player {player_number+1}, what is your name?: ')
        return name

    def method_of_fleet_assignment(self):
        # An method that will require extension definition in child classes
        # A random method is available for all children
        pass

    def determine_shot(self, opponent_fleet_board):
        # Random method (to be inherited in child classes
        self.chosen_row = random.randint(0, self.shot_board.board_size-1)
        self.chosen_col = random.randint(0, self.shot_board.board_size-1)
        letter = letters_to_numbers.n_t_l(self.chosen_col+1)
        print(f'A random shot was fired to location {letter}-{self.chosen_row+1}')
        pass
