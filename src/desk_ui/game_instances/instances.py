"""Declare main game instacnes."""
import pygame

from abc import ABCMeta, abstractmethod


class MovableObject(metaclass=ABCMeta):
    """Metaclass for declaring basic functionality of movable object."""

    def __init__(
            self,
            x: float,
            y: float,
            mov_x: float,
            mov_y: float,
            color: pygame.color.Color,
            radius: int,
            field_borders: tuple[int],
            friction: float = 0.02,
    ):
        """Init player values."""
        self.pos = pygame.math.Vector2(x, y)
        self.movement = pygame.math.Vector2(mov_x, mov_y)
        self.color = color
        self.radius = radius
        self.field_borders = field_borders
        self.friction = friction

    def update(self):
        """Update positioin."""
        self.pos += self.movement
        self.movement *= (1 - self.friction)
        self.normalize()

    @abstractmethod
    def change(self, mov_x: int, mov_y: int):
        """Change movement."""

    @abstractmethod
    def normalize(self):
        """Normalize pos with borders."""


class Player(MovableObject):
    """Declare player class."""

    def change(self, mov_x: int, mov_y: int):
        """Increase movement by given arguments."""
        self.movement.x += mov_x
        self.movement.y += mov_y

    def normalize(self):
        """Normalize values with borders."""
        if self.pos.x < self.field_borders[0] + self.radius:
            self.pos.x = self.field_borders[0] + self.radius
            self.movement.x = 0

        if self.pos.x > self.field_borders[2] - self.radius:
            self.pos.x = self.field_borders[2] - self.radius
            self.movement.x = 0

        if self.pos.y < self.field_borders[0] + self.radius:
            self.pos.y = self.field_borders[1] + self.radius
            self.movement.y = 0

        if self.pos.y > self.field_borders[3] - self.radius:
            self.pos.y = self.field_borders[3] - self.radius
            self.movement.y = 0


class Puck(MovableObject):
    """Declare all puck related methods."""

    def normalize(self):
        """Normalize values with borders."""
        if self.pos.x < self.field_borders[0] + self.radius or \
                self.pos.x > self.field_borders[2] - self.radius:
            self.pos.x = -self.pos.x
        if self.pos.y < self.field_borders[1] + self.radius or \
                self.pos.y > self.field_borders[3] - self.radius:
            self.pos.y = -self.pos.y

    def change(self, mov_x: float, mov_y: float):
        """Change values by given arguments."""
        self.movement = pygame.math.Vector2(mov_x, mov_y)
