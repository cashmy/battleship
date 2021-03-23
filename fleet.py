from ship import Ship


class Fleet:

    def __init__(self):
        self.fleet_name = ''
        self.number_of_ships = 4
        self.ship_list = []
        self.ships_left = 4

    def add_ship(self):
        self.ship_list[0] = Ship()
