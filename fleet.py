from ship import Ship


class Fleet:

    def __init__(self):
        self.fleet_name = ''
        self.number_of_ships = 4
        self.ship_list = []
        self.ships_left = 4
        self.add_ship()

    def add_ship(self):
        self.ship_list.append(Ship())
        self.ship_list.append(Ship(3, 'submarine', 'S'))
        self.ship_list.append(Ship(4, 'battleship', 'B'))
        self.ship_list.append(Ship(5, 'carrier', 'C'))

