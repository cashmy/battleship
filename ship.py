class Ship:
    def __init__(self, size=2, ship_type='destroyer', ship_designator='D'):
        self.size = size
        self.ship_type = ship_type
        # Additional size and type combinations
        #    3 - submarine
        #    4 - battleship
        #    5 - aircraft carrier
        self.ship_designator = ship_designator      # Valid entries are: 'D', 'S', 'B', 'C'
        self.strength = size                        # Initial strength is the same as the size
        self.starting_coord = [0, 0]
        self.axis_direction = [0, 0]
        self.ship_placed = False

    def update_status(self, hit):
        # this will track the remaining points before being sunk
        self.strength -= hit
        pass
