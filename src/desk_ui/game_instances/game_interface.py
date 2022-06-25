"""Declare main class for interaction with game."""
import pygame

from game_instances.playable import Player, Puck
from game_instances.utils import collide
from game_instances import interfaces

from typing import Iterable


class GameState():
    """Class for managing game state."""

    FIRST_PLAYER_COLOR = pygame.color.Color(255, 0, 0)
    SECOND_PLAYER_COLOR = pygame.color.Color(0, 255, 255)
    PLAYER_RADIUS = 50
    PLAYER_WEIGHT = 10
    PLAYER_MAGNITUDE = 0.75
    PLAYER_FRICTION = 0.001

    PUCK_COLOR = pygame.color.Color(255, 255, 255)
    PUCK_RADIUS = 30
    PUCK_WEIGHT = 0.01

    SPEED_BOOST: float = 2.5

    def __init__(
            self,
            field_borders: tuple[int | float, int | float, int | float, int | float],
    ):
        """Init game state."""
        # First player initialization
        self.first_player: Player = Player(
            100 - self.PLAYER_RADIUS,
            field_borders[3] / 2, 0, 0,
            self.FIRST_PLAYER_COLOR,
            self.PLAYER_RADIUS,
            field_borders,
            friction=self.PLAYER_FRICTION,
            weight=self.PLAYER_WEIGHT,
            max_magnitude=self.PLAYER_MAGNITUDE,
        )
        
        # Second player initialization
        self.second_player: Player = Player(
            field_borders[2] - (100 - self.PLAYER_RADIUS),
            field_borders[3] / 2, 0, 0,
            self.SECOND_PLAYER_COLOR,
            self.PLAYER_RADIUS,
            field_borders,
            friction=self.PLAYER_FRICTION,
            weight=self.PLAYER_WEIGHT,
            max_magnitude=self.PLAYER_MAGNITUDE,
        )
        
        # Additional stuff for player movement
        self._first_boost: pygame.math.Vector2 = pygame.math.Vector2(0, 0)
        self._first_extra_boost: int = 0
        
        self._second_boost: pygame.math.Vector2 = pygame.math.Vector2(0, 0)
        self._second_extra_boost: int = 0

        # Puck initialization
        self.puck: Puck = Puck(
            field_borders[2] / 2,
            field_borders[3] / 2, 0, 0,
            color=self.PUCK_COLOR,
            radius=self.PUCK_RADIUS,
            field_borders=field_borders,
            weight=self.PUCK_WEIGHT,
        )

    @property
    def instances2draw(self) -> Iterable[Puck | Player]:
        """Return iterable object of all instances to draw."""
        return self.first_player, self.second_player, self.puck

    def add_first_boost(self, x: int | float = 0, y: int | float = 0) -> None:
        """Change first player boost."""
        self._first_boost += pygame.math.Vector2(x, y)

    def change_first_extra_boost(self) -> None:
        """Change first player extra boost."""
        # Changing state for first extra boost
        self._first_extra_boost ^= 1
        
        # Koef for magnitude
        koef = self.SPEED_BOOST
        if not self._first_extra_boost:
            koef = 1 / koef
        
        # Changin magnitude according to koef
        self.first_player.max_magnitude *= koef

    def add_second_boost(self, x: int | float =0, y: int | float = 0) -> None:
        """Change second player boost."""
        self._second_boost += pygame.math.Vector2(x, y)

    def change_second_extra_boost(self) -> None:
        """Change second player extra boost."""
        # Change state for second extra boost
        self._second_extra_boost ^= 1
        
        # Koef for magnitude
        koef = self.SPEED_BOOST
        if not self._second_extra_boost:
            koef = 1 / koef

        # Changing magnitude acccording to koef
        self.second_player.max_magnitude *= koef

    def update(self) -> None:
        """Update game state."""

        # Normal speed + speed_boost coef
        self.first_player.change(
                self._first_boost.x + self._first_extra_boost *\
                        self._first_boost.x * (self.SPEED_BOOST - 1),
                self._first_boost.y + self._first_extra_boost *\
                        self._first_boost.y * (self.SPEED_BOOST - 1),
        )
        self.second_player.change(
                self._second_boost.x + self._second_extra_boost *\
                        self._second_boost.x * (self.SPEED_BOOST - 1),
                self._second_boost.y + self._second_extra_boost *\
                        self._second_boost.y * (self.SPEED_BOOST - 1),
        )
        
        # Collide everything with each other
        for find, fvalue in enumerate(self.instances2draw):
            for sind, svalue in enumerate(self.instances2draw):
                if find >= sind:
                    continue
                collide(fvalue, svalue)

        # Update positions
        for mov_obj in self.instances2draw:
            mov_obj.update()


class Game():
    """Main game class."""

    SIZE = (1400, 768)
    BASE_SPEED = 0.001
    UPDATES_PER_FRAME = 50
    ARROW_MOVEMENT_CHANGE = {
        pygame.K_RIGHT: (BASE_SPEED, 0),
        pygame.K_LEFT: (-BASE_SPEED, 0),
        pygame.K_UP: (0, -BASE_SPEED),
        pygame.K_DOWN: (0, BASE_SPEED),
    }
    WASD_MOVEMENT_CHANGE = {
        pygame.K_d: (BASE_SPEED, 0),
        pygame.K_a: (-BASE_SPEED, 0),
        pygame.K_w: (0, -BASE_SPEED),
        pygame.K_s: (0, BASE_SPEED),
    }
    FIELD_COLORING = interfaces.PlayingFieldColoring

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

                elif event.key in self.ARROW_MOVEMENT_CHANGE:
                    # changing boost
                    self.__game_state.add_first_boost(
                        *self.ARROW_MOVEMENT_CHANGE[event.key])
                elif event.key in self.WASD_MOVEMENT_CHANGE:
                    # changing boost
                    self.__game_state.add_second_boost(
                        *self.WASD_MOVEMENT_CHANGE[event.key])
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_LSHIFT:
                    # changing extra boost
                    self.__game_state.change_first_extra_boost()

                elif event.key in self.ARROW_MOVEMENT_CHANGE:
                    # changing boost
                    self.__game_state.add_first_boost(*map(
                        lambda x: -x, self.ARROW_MOVEMENT_CHANGE[event.key]))
                elif event.key in self.WASD_MOVEMENT_CHANGE:
                    # changin boost
                    self.__game_state.add_second_boost(*map(
                        lambda x: -x, self.WASD_MOVEMENT_CHANGE[event.key]))
    def __update(self):
        """Update game instances."""
        # to make game interaction quicker we wouldn't draw every update iteration
        for _ in range(self.UPDATES_PER_FRAME):
            self.__game_state.update()

    def __render(self):
        """Render game instances."""
        self.__window.fill((0, 0, 0))
        self.FIELD_COLORING.draw(self.__window, (0, 0) + self.SIZE)
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
