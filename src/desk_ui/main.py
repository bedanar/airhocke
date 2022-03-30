"""Specify main event in global scope."""
from game_instances import game_interface


def main():
    """Declair main game instances and run game."""
    main_game = game_interface.Game()
    main_game.run()


if __name__ == '__main__':
    main()
