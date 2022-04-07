"""Declare main class for interaction with game."""
import pygame
from game_instances.instances import Player


class GameState():
    """Class for managing game state."""

    def __init__(self, field_borders: tuple[int]):
        """Init game state."""
        self.player = Player(
            0, 0, 0, 0,
            pygame.color.Color(255, 0, 0),
            50,
            field_borders,
        )

    def update(self, movement_x: int, movement_y: int, is_under_boost: bool):
        """Update game state."""
        self.player.change(movement_x, movement_y)

        # If player under boost increase his speed three times
        if is_under_boost:
            for _ in range(2):
                self.player.change(movement_x, movement_y)
        self.player.update()


class Game():
    """Main game class."""

    SIZE = (1400, 768)
    BASE_SPEED = 0.0001

    def __init__(self):
        """Init game instance."""
        pygame.init()
        self.__window = pygame.display.set_mode(self.SIZE)
        pygame.display.set_caption("Airhockey")
        pygame.display.set_icon(pygame.image.load(
            'static/icons/ice-hockey.png'))
        self.__clock = pygame.time.Clock()
        self.__game_state = GameState((0, 0) + self.SIZE)
        self.__running = True
        self.__player_speed_x_inc = 0
        self.__player_y_speed_inc = 0
        self.__speed_booster = False

    def process_input(self):
        """Process user actions."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.__running = False
                break
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_f:
                    if self.__window.get_flags() & pygame.FULLSCREEN:
                        self.__window = pygame.display.set_mode(self.SIZE)
                    else:
                        self.__window = pygame.display.set_mode(
                            self.SIZE, pygame.FULLSCREEN)
                if event.key == pygame.K_ESCAPE:
                    self.__running = False
                    pygame.quit()
                    break
                elif event.key == pygame.K_RIGHT:
                    self.__player_speed_x_inc += self.BASE_SPEED
                elif event.key == pygame.K_LEFT:
                    self.__player_speed_x_inc -= self.BASE_SPEED
                elif event.key == pygame.K_DOWN:
                    self.__player_y_speed_inc += self.BASE_SPEED
                elif event.key == pygame.K_UP:
                    self.__player_y_speed_inc -= self.BASE_SPEED
                elif event.key == pygame.K_LSHIFT:
                    self.__speed_booster = True
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_RIGHT:
                    self.__player_speed_x_inc -= self.BASE_SPEED
                elif event.key == pygame.K_LEFT:
                    self.__player_speed_x_inc += self.BASE_SPEED
                elif event.key == pygame.K_DOWN:
                    self.__player_y_speed_inc -= self.BASE_SPEED
                elif event.key == pygame.K_UP:
                    self.__player_y_speed_inc += self.BASE_SPEED
                elif event.key == pygame.K_LSHIFT:
                    self.__speed_booster = False

    def __update(self):
        """Update game instances."""
        # to make game interaction quicker we wouldn't draw every update iteration
        for _ in range(100):
            self.__game_state.update(
                self.__player_speed_x_inc,
                self.__player_y_speed_inc,
                self.__speed_booster,
            )

    def render(self):
        """Render game instances."""
        self.__window.fill((0, 0, 255))
        pygame.draw.circle(
            self.__window, self.__game_state.player.color,
            self.__game_state.player.pos, self.__game_state.player.radius
        )
        pygame.display.update()

    def run(self):
        """Game loop."""
        while self.__running:
            self.process_input()
            self.__update()
            self.render()
            self.__clock.tick(60)
