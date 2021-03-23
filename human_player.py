from player import Player


class HumanPlayer(Player):
    def __init__(self, name='', player_number=1, board_size=10):
        super().__init__(name, player_number, board_size)
        pass

    def method_of_play(self, gestures):
        pass
