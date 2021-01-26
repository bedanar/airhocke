from constants import WHITE, GATES_SIZE
from movement import Movement
from vector_math import *
import pygame
import random


class Puck(pygame.sprite.Sprite):
    def __init__(self, coords, players, radius, window_height, window_length):
        self.coords = [coords[0], coords[1]]
        self.movement = Movement()
        self.players = players
        self.radius = radius
        self.stoping = 0.998
        self.window_height = window_height
        self.window_length = window_length

    def remove_collision(self):
        up_y = self.window_height / 2 - GATES_SIZE / 2
        up_y += self.radius - 5
        down_y = up_y + GATES_SIZE
        down_y -= self.radius + 5
        if not up_y <= self.coords[1] <= down_y:
            if self.coords[0] <= self.radius or self.coords[0] >= self.window_length - self.radius:
                self.movement.x = -self.movement.x
            if self.coords[1] <= self.radius or self.coords[1] >= self.window_height - self.radius:
                self.movement.y = -self.movement.y
        for player in self.players:
            player_coords = player.get_coords()
            if ((player_coords[0] - self.coords[0]) ** 2 + (player_coords[1] -
                                                            self.coords[1]) ** 2) ** 0.5 - 1 <= player.radius + self.radius:
                self.movement.connect(player.movement, Point(*player.coords), Point(*self.coords))
                for item in range(4):
                    self.coords = self.next_coords()
        return self


    def next_coords(self):
        up_y = self.window_height / 2 - GATES_SIZE / 2
        up_y += self.radius - 5
        down_y = up_y + GATES_SIZE
        down_y -= self.radius + 5
        if up_y <= self.coords[1] <= down_y:
            return self.coords[0] + self.movement.x, self.coords[1] + self.movement.y
        return (min(max(self.radius, self.coords[0] + self.movement.x), self.window_length - self.radius),
                       min(max(self.radius, self.coords[1] + self.movement.y), self.window_height - self.radius))

    def draw_info(self, sc, color=-1, radius=-1):
        # print(color)
        if color == -1:
            color = WHITE
        if radius == -1:
            radius = self.radius
        return [sc, color, self.coords, radius]

    def change_coords(self):
        self.movement.x = min(15, self.movement.x)
        self.movement.y = min(15, self.movement.y)
        self.movement.x = self.movement.x * self.stoping
        self.movement.y = self.movement.y * self.stoping
        self.coords = self.next_coords()
        return self

    def check_goal(self):
        up_y = self.window_height / 2 - GATES_SIZE / 2
        up_y += self.radius - 5
        down_y = up_y + GATES_SIZE
        down_y -= self.radius + 5
        if self.coords[0] + self.radius - 18 <= 0:
            if  up_y <= self.coords[1] <= down_y:
                return 2

        if self.coords[0] - self.radius + 18 >= self.window_length - 4:
            if up_y <= self.coords[1] <= down_y:

                return 1
        return 0
