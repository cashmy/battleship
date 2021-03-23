from gameboard import GameBoard


class ShotBoard(GameBoard):

    def __init__(self, board_size):
        super().__init__('shot', board_size)
        self.initialize_board()

