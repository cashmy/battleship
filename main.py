import game_actions


def print_hi(name):
    print(f'Hi, {name}! Welcome to BattleShip!')  # Press Ctrl+F8 to toggle the breakpoint.


if __name__ == '__main__':
    print_hi('Gamer')
    game_actions.game_setup()
    game_actions.game_turn()
