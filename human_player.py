from player import Player
import letters_to_numbers


class HumanPlayer(Player):
    def __init__(self, name='', player_number=1, board_size=10):
        super().__init__(name, player_number, board_size)
        self.chosen_method = self.method_of_shot_determination()

    def method_of_shot_determination(self):
        valid_entry = False
        while not valid_entry:
            method = input('How would like to determine your shots (1=Random 2=Manual Entry)? : ')
            if method == '1' or method == '2':
                self.chosen_method = method
                valid_entry = True
            else:
                print('I did not understand your choice. Please try again.')
        return self

    # Redefinition of parent class method for this child class
    # A random method is available for all children which is defined in parent class
    def method_of_fleet_assignment(self):
        # inherit random assignment
        # add allowance for interactive assignment
        pass

    def determine_shot(self, opponent_fleet_board):
        if self.chosen_method == '1':  # Random coordinates inherited from parent class
            super().determine_shot(opponent_fleet_board)
        elif self.chosen_method == '2':
            # define & use player interaction here:
            self.ui_take_a_shot()
            pass
        elif self.chosen_method == 3:
            # define auto AI Calc here for optimum fire
            pass
        else:
            # Some error occurred. Revert chosen method to default
            self.chosen_method = '1'

        hit = self.fleet_board.check_board(self.chosen_row, self.chosen_col)
        self.shot_board.update_board(self.chosen_row, self.chosen_col, hit)
        self.shot_board.print_board()

    def ui_take_a_shot(self):
        if self.shot_board.board_size == 20:
            end_letter = 'T'
        else:
            end_letter = 'J'
        col_letter: str = input(f'Enter the desired column (A-{end_letter})')
        self.chosen_col = letters_to_numbers(col_letter)
        self.chosen_row = input(f'Enter the desired row (1-{self.shot_board.board_size}): ')
        return self
