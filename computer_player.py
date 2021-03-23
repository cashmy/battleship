from player import Player
# import random


class ComputerPlayer(Player):
    def __init__(self, name='', player_number=2, board_size=10):
        super().__init__(name, player_number, board_size)
        pass

    @staticmethod
    def validate_name(name, player_number):
        if not name or name == '':
            name = input(f'Player {player_number+1}/AI, what is your name?: ')
        return name

    # Redefinition of parent class method for this child class
    # A random method is available for all children which is defined in parent class
    def method_of_fleet_assignment(self):
        # inherit random assignment
        # FUTURE SPRINT: Add allowance for AI calculation for best next placement
        pass

    def determine_shot(self, board_size, method_type, opponent_fleet_board):
        if method_type == '1' or method_type == '2':  # Random - Override user interaction to random for AI
            # Call parent class base version actions
            super().determine_shot(board_size, method_type, opponent_fleet_board)
        else:
            # define action here
            pass
