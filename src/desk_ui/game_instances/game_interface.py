"""Declare main class for interaction with game."""
import pygame

from game_instances.playable import Player, Puck
from game_instances.utils import collide

from typing import Iterable


class GameState():
    """Class for managing game state."""

    FIRST_PLAYER_COLOR = pygame.color.Color(255, 0, 0)
    FIRST_PLAYER_RADIUS = 50
    PUCK_COLOR = pygame.color.Color(0, 0, 0)
    PUCK_RADIUS = 30

    def __init__(
            self,
            field_borders: tuple[int | float, int | float, int | float, int | float],
    ):
        """Init game state."""
        self.first_player: Player = Player(
            100 - self.FIRST_PLAYER_RADIUS,
            field_borders[3] / 2 - self.FIRST_PLAYER_RADIUS, 0, 0,
            self.FIRST_PLAYER_COLOR,
            self.FIRST_PLAYER_RADIUS,
            field_borders,
            weight=10,
        )
        self._first_boost: pygame.math.Vector2 = pygame.math.Vector2(0, 0)
        self._first_player_extra_boost: int = 0
        self.puck: Puck = Puck(
            field_borders[2] / 2 - self.PUCK_RADIUS,
            field_borders[3] / 2 - self.PUCK_RADIUS, 0, 0,
            color=self.PUCK_COLOR,
            radius=self.PUCK_RADIUS,
            field_borders=field_borders,
        )

    @property
    def instances2draw(self) -> Iterable[Puck | Player]:
        """Return iterable object of all instances to draw."""
        return self.first_player, self.puck

    def add_first_boost(self, x: int | float = 0, y: int | float = 0) -> None:
        """Change first player boost."""
        self._first_boost += pygame.math.Vector2(x, y)

    def change_first_extra_boost(self) -> None:
        """Change first player extra boost."""
        self._first_player_extra_boost ^= 1

    def update(self) -> None:
        """Update game state."""
        self.first_player.change(self._first_boost.x, self._first_boost.y)

        # If player under bost increase his speed three times
        if self._first_player_extra_boost:
            for _ in range(2):
                self.first_player.change(
                    self._first_boost.x, self._first_boost.y)

        for find, fvalue in enumerate(self.instances2draw):
            for sind, svalue in enumerate(self.instances2draw):
                if find >= sind:
                    continue
                collide(fvalue, svalue)
        for mov_obj in self.instances2draw:
            mov_obj.update()


class Game():
    """Main game class."""

    SIZE = (1400, 768)
    BASE_SPEED = 0.00035
    MOVEMENT_CHANGE = {
        pygame.K_RIGHT: (BASE_SPEED, 0),
        pygame.K_LEFT: (-BASE_SPEED, 0),
        pygame.K_UP: (0, -BASE_SPEED),
        pygame.K_DOWN: (0, BASE_SPEED),
    }

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

    def __process_input(self):
        """Process user actions."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.__running = False
                break
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_f:
                    # straing full scrine resizing
                    # TODO: make this shit working
                    if self.__window.get_flags() & pygame.FULLSCREEN:
                        self.__window = pygame.display.set_mode(self.SIZE)
                    else:
                        self.__window = pygame.display.set_mode(
                            self.SIZE, pygame.FULLSCREEN)
                if event.key == pygame.K_ESCAPE:
                    self.__running = False
                    pygame.quit()
                    break
                elif event.key == pygame.K_LSHIFT:
                    # changing extra boost
                    self.__game_state.change_first_extra_boost()

                elif event.key in self.MOVEMENT_CHANGE:
                    # changing boost
                    self.__game_state.add_first_boost(
                        *self.MOVEMENT_CHANGE[event.key])
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_LSHIFT:
                    # changing extra boost
                    self.__game_state.change_first_extra_boost()

                elif event.key in self.MOVEMENT_CHANGE:
                    # changing boost
                    self.__game_state.add_first_boost(*map(
                        lambda x: -x, self.MOVEMENT_CHANGE[event.key]))

    def __update(self):
        """Update game instances."""
        # to make game interaction quicker we wouldn't draw every update iteration
        for _ in range(50):
            self.__game_state.update()

    def __render(self):
        """Render game instances."""
        self.__window.fill((0, 0, 255))
        for inst in self.__game_state.instances2draw:
            pygame.draw.circle(self.__window, *inst.draw_tuple())
        pygame.display.update()

    def run(self):
        """Game loop."""
        while self.__running:
            self.__process_input()
            self.__update()
            self.__render()
            self.__clock.tick(60)
