from gameboard import GameBoard
from fleet import Fleet


class FleetBoard(GameBoard):

    def __init__(self, board_size):
        super().__init__('shot', board_size)
        self.initialize_board()
        self.fleet = Fleet()  # Initialize the fleet

    # This method is used for TDD testing.
    def default_placement(self):
        # Destroyer
        self.board_layout[1][2] = 'D'
        self.board_layout[2][2] = 'D'

        # Submarine
        self.board_layout[4][7] = 'S'
        self.board_layout[4][8] = 'S'
        self.board_layout[4][9] = 'S'

        # Battleship
        self.board_layout[6][5] = 'B'
        self.board_layout[6][6] = 'B'
        self.board_layout[6][7] = 'B'
        self.board_layout[6][8] = 'B'

        # Carrier
        self.board_layout[5][3] = 'C'
        self.board_layout[6][3] = 'C'
        self.board_layout[7][3] = 'C'
        self.board_layout[8][3] = 'C'
        self.board_layout[9][3] = 'C'
        return self

    def check_board(self, row, col):
        ship_char_list = ['D', 'S', 'B', 'C']
        # rtv the current value in the board
        char_check = self.board_layout[row][col]
        hit = False
        for char in ship_char_list:
            if char_check == char:
                hit = True  # Always assume hit for testing purposes
        # ADD Ship Update here
        return hit

    def ship_placement(self, ):
        # get starting coordinates
        # determine direction to place  (N, S, E, W)
        # check for boundaries based upon ship size
        # Iterate over board for clear place
        # Raise error if collision occurs

        # If random place - cycle clockwise one space until fit is found
        # if not fit is found either add two spaces or chose another random point
        pass
