from player import Player
# import random


class ComputerPlayer(Player):
    def __init__(self, name='', player_number=2, board_size=10):
        super().__init__(name, player_number, board_size)
        pass

    @staticmethod
    def validate_name(name, player_number):
        if not name or name == '':
            name = input(f'Player {player_number+1}/AI, what is your name?: ')
        return name

    def method_of_play(self, gestures):
        pass
