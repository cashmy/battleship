
from shot_board import ShotBoard

my_shot_board = ShotBoard(10)

my_shot_board.print_board()
my_shot_board.update_board(1, 1, False)
my_shot_board.update_board(3, 4, True)
my_shot_board.update_board(9, 9, False)
my_shot_board.update_board(10, 10, False)
my_shot_board.print_board()
