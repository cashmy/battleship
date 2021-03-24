class IntelligentGuesses:
    def __init__(self, hit_row, hit_col):
        self.hit_row = hit_row
        self.hit_col = hit_col
        self.direction = 'N'  # Direction code can be 'N', 'S', 'E', or 'W'
        self.next_row = 0     # Not sure if we need this here, but adding it for tracking of ideas
        self.next_col = 0     # Not sure if we need this here, but adding it for tracking of ideas

    def __del__(self):
        pass
