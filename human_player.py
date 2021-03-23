from player import Player


class HumanPlayer(Player):
    def __init__(self, name='', player_number=1, board_size=10):
        super().__init__(name, player_number, board_size)

    # Redefinition of parent class method for this child class
    # A random method is available for all children which is defined in parent class
    def method_of_fleet_assignment(self):
        # inherit random assignment
        # add allowance for interactive assignment
        pass

    def determine_shot(self, board_size, method_type, opponent_fleet_board):
        if method_type == '1':  # Random
            super().determine_shot(board_size, method_type, opponent_fleet_board)
        elif method_type == '2':
            # define & use player interaction here:
            pass
        elif method_type == 3:
            # define auto AI Calc here for optimum layout - FUTURE SPRINT
            pass
        else:
            pass
