from constants import WHITE
from movement import Movement
from vector_math import *
import random
class Puck:
    def __init__(self, coords, players, radius, window_height, window_length):
        self.coords = coords[0], coords[1]
        self.movement = Movement()
        self.players = players
        self.radius = radius
        self.stoping = 0.997
        self.window_height = window_height
        self.window_length = window_length

    def remove_collision(self):
        if self.coords[0] <= self.radius or self.coords[0] >= self.window_length - self.radius:
            self.movement.x = -self.movement.x
        if self.coords[1] <= self.radius or self.coords[1] >= self.window_height - self.radius:
            self.movement.y = -self.movement.y
        for player in self.players:
            player_coords = player.get_coords()
            if ((player_coords[0] - self.coords[0]) ** 2 + (player_coords[1] -
                                                            self.coords[1]) ** 2) ** 0.5 - 1 <= player.radius + self.radius:
                # print("Collision3 with", player.type, player.movement, Point(*player.coords), Point(*self.coords), end=' ')

                self.movement.connect(player.movement, Point(*player.coords), Point(*self.coords))
                mult_vector(1.5, self.movement)
                for _ in range(3):
                    self.coords = self.next_coords()
                mult_vector(1 / 1.5, self.movement)
                break
        return self


    def next_coords(self):
        #
        # if self.coords[0] <= self.radius or self.coords[0] >= self.window_length - self.radius:
        #     self.movement.x = -self.movement.x
        # if self.coords[1] <= self.radius or self.coords[1] >= self.window_height - self.radius:
        #     self.movement.y = -self.movement.y
        return (min(max(self.radius, self.coords[0] + self.movement.x), self.window_length - self.radius),
                       min(max(self.radius, self.coords[1] + self.movement.y), self.window_height - self.radius))

    def draw_info(self, sc):
        return [sc, WHITE, self.coords, self.radius]

    def change_coords(self):
        self.movement.x = self.movement.x * self.stoping
        self.movement.y = self.movement.y * self.stoping
        self.coords = self.next_coords()
        return self
