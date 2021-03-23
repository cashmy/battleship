class Ship:
    def __init__(self):
        self.size = 2
        self.type = 'destroyer'
        # Additional size and type combinations
        #    3 - submarine
        #    4 - battleship
        #    5 - aircraft carrier
        self.strength = 2
        self.starting_coord = [0, 0]
        self.axis_direction = [0, 0]

    def update_status(self, hit):
        # this will track the remaining points before being sunk
        self.strength -= hit
        pass
