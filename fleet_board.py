from gameboard import GameBoard
from fleet import Fleet


class FleetBoard(GameBoard):

    def __init__(self, board_size):
        super().__init__('shot', board_size)
        self.initialize_board()
        self.fleet = Fleet()  # Initialize the fleet

    # This method is used for testing.
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

    @staticmethod
    def check_board(row, col):
        # add logic for check here
        hit = True  # Always assume hit for testing purposes
        return hit
