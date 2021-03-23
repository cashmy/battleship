class GameBoard:

    def __init__(self, board_type, board_size=10):
        self.board_type = board_type  # hit board or shot board
        self.board_size = board_size  # 10x10 or 20x20 grid
        self.board_layout = [self.board_size, self.board_size]

    def initialize_board(self):
        # Using a 2 dimensional array, create the board
        # (Basically a list of lists)
        rows, cols = (self.board_size, self.board_size)
        # self.board_layout = [[' '] * cols] * rows
        self.board_layout = [[" " for i in range(cols)] for j in range(rows)]

    def print_board(self):
        # This will display my hits and misses
        letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T']
        counter = 0
        header = ''
        while counter <= self.board_size-1:
            header += letters[counter] + '.'
            counter += 1
        print(f'    {header}')

        counter = 1
        for row in self.board_layout:
            new_row = ".".join(row)
            if counter < 10:
                print(f' {counter}) {new_row}')
            else:
                print(f'{counter}) {new_row}')
            counter += 1
        print('==========')

    def update_board(self, row, col, hit):
        # Update with hits and misses
        # Update coordinate with miss '~' , or hit '*'
        if hit:
            action = '*'
        else:
            action = '~'
        self.board_layout[row-1][col-1] = action
