from player import Player
# import random


class ComputerPlayer(Player):
    def __init__(self, name='', player_number=2, board_size=10):
        super().__init__(name, player_number, board_size)
        self.chosen_method = self.method_of_shot_determination()

    def method_of_shot_determination(self):
        valid_entry = False
        while not valid_entry:
            method = input('How would like the AI to determine its shots (1=Random 3=Intelligent Calculation)? : ')
            if method == '1' or method == '3':
                self.chosen_method = method
                valid_entry = True
            else:
                print('I did not understand your choice. Please try again.')
        return self

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

    def determine_shot(self, opponent_fleet_board):
        # Random - Override "2=user interaction" if passed, to "1=random" for AI
        if self.chosen_method == '1' or self.chosen_method == '2':
            # Call parent class base version actions
            super().determine_shot(opponent_fleet_board)
        elif self.chosen_method == 3:
            # define auto AI Calc here for optimum fire
            pass
        else:
            # Some error occurred. Revert chosen method to default
            self.chosen_method = '1'

