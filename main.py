from all_types_of_games import two_in_one, game_intro, online, ai
import pygame 

game_condition = 0

values = [game_intro, two_in_one, online, ai]


if __name__ == '__main__':
    running = True
    pygame.init()
    while running:
        try:
            game_condition = values[game_condition](pygame)
        except Exception as e:
            print(e)
            running = False
    pygame.quit()
