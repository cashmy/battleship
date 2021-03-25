from gameboard import GameBoard
from fleet import Fleet
import random
import coordinates
import clear_screen


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

    def ship_placement(self, method_of_placement='1'):
        direction = 0

        for ship in self.fleet.ship_list:
            collision = True
            placement_effort = 0
            row = 0
            col = 0
            while collision and placement_effort <= 5:
                self.print_board('Fleet Board')
                if method_of_placement == '1' or method_of_placement == '3':
                    if placement_effort == 0:
                        print(f'Placing the {ship.ship_type}')
                    else:
                        print(f'Placing the {ship.ship_type} attempt number: {placement_effort+1}')
                    row = random.randint(0, self.board_size-1)
                    col = random.randint(0, self.board_size-1)
                    direction_int = random.randint(0, 1)
                    if direction_int == 0:
                        direction = 'down'
                    else:
                        direction = 'across'
                elif method_of_placement == '2':
                    if placement_effort == 0:
                        print(f'Please give the starting coordinates for the {ship.ship_type}')
                    else:
                        print(f'Please give the starting coordinates for the {ship.ship_type} '
                              f'attempt number: {placement_effort + 1}')
                    col = coordinates.column_entry(self.board_size)
                    row = coordinates.row_entry(self.board_size)
                    direction = coordinates.get_direction()
                # Now check for collision
                collision = self.ship_placement_check(row, col, direction, ship.size)
                # If collision exists, optionally print error message and then cycle back for another effort
                if collision:
                    if method_of_placement == '2':
                        print('The ship cannot be placed here. Please select another starting location')
                    placement_effort += 1
                else:
                    self.place_ship(row, col, direction, ship)
                    pass
        self.print_board("Final Fleet Layout")
        input('When ready press the enter key for the next player')
        clear_screen.clear()
        return self

    def ship_placement_check(self, row, col, direction, size):
        # check the initial starting position for a collision - Sets initial value for collision
        collision = self.collision_check(row, col)
        if collision:
            return collision

        # Setup temp start and end locations so the loop will also "Increment
        if direction == 'down':
            start_point = row + 1
            end_point = col + size
        elif direction == 'across':
            end_point = row + size
            start_point = col + 1

        # check for boundaries based upon ship size
        if end_point > self.board_size:
            collision = True
            return collision

        # Iterate over board for clear place
        counter = start_point
        while not collision and counter <= end_point:
            if direction == 'down':
                collision = self.collision_check(counter, col)
            else:
                collision = self.collision_check(row, counter)
            counter += 1
        return collision

    def collision_check(self, row, col):
        collision = False
        char_check = self.board_layout[row][col]
        if not char_check == ' ':
            collision = True
        return collision

    def place_ship(self, row, col, direction, ship):
        # Update ship class with coordinates
        ship.starting_coord[0] = row
        ship.starting_coord[1] = col
        if direction == 'down':
            ship.ending_coord[0] = row
            ship.ending_coord[1] = col + ship.size
        else:
            ship.ending_coord[0] = row + ship.size
            ship.ending_coord[1] = col
        ship.ship_placed = True
        # Update Fleet board with ship location
        # self.board_layout[row][col] = ship.ship_designator
        counter = 0
        while counter < ship.size:
            if direction == 'down':
                self.board_layout[row + counter][col] = ship.ship_designator
            else:
                self.board_layout[row][col + counter] = ship.ship_designator
            counter += 1
        return self
