from gameboard import GameBoard
from fleet import Fleet


class FleetBoard(GameBoard):

    def __init__(self, board_size):
        super().__init__('shot', board_size)
        self.initialize_board()
        self.fleet = Fleet()
