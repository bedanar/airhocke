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
            field_borders: tuple[int | float, int | float, int | float, int | float],
            friction: float = 0.0001,
            weight: float = 1,
            max_magnitude: float = 1.5,
    ):
        """Init player values."""
        self.pos = pygame.math.Vector2(x, y)
        self.movement = pygame.math.Vector2(mov_x, mov_y)
        self.color = color
        self.radius = radius
        self.field_borders = field_borders
        self.friction = friction
        self.max_magnitude = max_magnitude
        self.weight = weight

    def update(self):
        """Update position."""
        self.pos += self.movement
        self.movement *= (1 - self.friction)
        self.normalize()

    def draw_tuple(self) -> tuple[pygame.color.Color, pygame.math.Vector2, int | float]:
        """Tuple for drawing circle."""
        return self.color, self.pos, self.radius

    def normalize(self) -> int:
        """Normalize values with borders."""
        rez = 0
        if self.pos.x < self.field_borders[0] + self.radius or \
                self.pos.x > self.field_borders[2] - self.radius:
            self.movement.x = -self.movement.x
            rez += 1
        if self.pos.y < self.field_borders[1] + self.radius or \
                self.pos.y > self.field_borders[3] - self.radius:
            self.movement.y = -self.movement.y
            rez += 1
        self.pos.x = max(self.pos.x, self.field_borders[0] + self.radius)
        self.pos.y = max(self.pos.y, self.field_borders[1] + self.radius)
        self.pos.x = min(self.pos.x, self.field_borders[2] - self.radius)
        self.pos.y = min(self.pos.y, self.field_borders[3] - self.radius)
        return rez

    @abstractmethod
    def change(self, mov_x: int, mov_y: int):
        """Change movement."""


class Player(MovableObject):
    """Declare player class."""
    
    def change(self, mov_x: int | float, mov_y: int | float):
        """Increase movement by given arguments."""
        self.movement.x += mov_x
        self.movement.y += mov_y
        magnitude = self.movement.magnitude()
        if magnitude > self.max_magnitude:
            self.movement.x *= self.max_magnitude / magnitude
            self.movement.y *= self.max_magnitude / magnitude

    def normalize(self):
        """Normalize values with borders."""
        collitions_numb = super().normalize()
        if collitions_numb:
            self.movement *= 0.8


class Puck(MovableObject):
    """Declare all puck related methods."""

    def change(self, mov_x: float, mov_y: float):
        """Change values by given arguments."""
        self.movement = pygame.math.Vector2(mov_x, mov_y)
