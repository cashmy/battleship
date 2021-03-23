class Player:

    def __init__(self):
        self.name = ''  # Player's name
        self.player_type = ''  # Human or AI
        self.fleet = ''  # Stores ships and each ships status
        self.shot_board = ''  # Record of players hits against opponent
        self.fleet_board = ''  # stores fleet location and opponent's hits
