import letters_to_numbers


def column_entry(board_size):
    if board_size == 20:
        end_letter = 'T'
    else:
        end_letter = 'J'
    # Enter Column
    valid_entry = False
    while not valid_entry:
        col_letter: str = input(f'Enter the desired column (A-{end_letter}): ')
        col_int = letters_to_numbers.l_t_n(col_letter)
        if col_letter == '' or (col_int < 1 or col_int > board_size):
            print('I did not understand your choice. Please try again.')
        else:
            valid_entry = True
    return col_int-1


def row_entry(board_size):
    # Enter Row
    valid_entry = False
    while not valid_entry:
        row = input(f'Enter the desired row (1-{board_size}): ')
        row_int = int(row) - 1
        if row == '' or (row_int < 0 or row_int >= board_size):
            print('I did not understand your choice. Please try again.')
        else:
            valid_entry = True
    return row_int-1
