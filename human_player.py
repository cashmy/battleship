from player import Player
import coordinates


class HumanPlayer(Player):
    def __init__(self, name='', player_number=1, board_size=10):
        super().__init__(name, player_number, board_size)
        self.method_of_shot_determination()
        self.method_of_ship_placement()
        self.fleet_board.ship_placement(self.ship_placement_method)

    def method_of_shot_determination(self):
        valid_entry = False
        while not valid_entry:
            method = input('How would like to determine your shots (1=Random 2=Manual Entry)? : ')
            if method == '1' or method == '2':
                self.target_method = method
                valid_entry = True
            else:
                print('I did not understand your choice. Please try again.')
        return self

    def method_of_ship_placement(self):
        valid_entry = False
        while not valid_entry:
            method = input('How would like to place your ships (1=Random 2=Manual Entry)? : ')
            if method == '1' or method == '2':
                self.ship_placement_method = method
                valid_entry = True
            else:
                print('I did not understand your choice. Please try again.')
        return self

    def determine_shot(self, opponent_fleet_board):
        if self.target_method == '1':  # Random coordinates inherited from parent class
            super().determine_shot(opponent_fleet_board)
        elif self.target_method == '2':
            # define & use player interaction here:
            self.ui_take_a_shot()
            pass
        elif self.target_method == 3:
            # define auto AI Calc here for optimum fire
            pass
        else:
            # Some error occurred. Revert chosen method to default
            self.target_method = '1'

        hit = self.fleet_board.check_board(self.chosen_row, self.chosen_col)
        self.shot_board.update_board(self.chosen_row, self.chosen_col, hit)
        self.shot_board.print_board('shot board')

    def ui_take_a_shot(self):
        # Enter Column
        self.chosen_col = coordinates.column_entry(self.shot_board.board_size)
        # Enter Row
        self.chosen_row = coordinates.row_entry(self.shot_board.board_size)
        return self
