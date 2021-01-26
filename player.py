from movement import Movement
from constants import RED, BLUE, BORDERS


class Player:
    def __init__(self, coords, radius, type, window_height, window_length):
        self.coords = coords[0], coords[1]
        self.radius = radius
        self.type = type

        self.window_height = window_height
        self.window_length = window_length
        self.movement = Movement()

    def draw_info(self, sc):
        return [sc, RED if self.type else BLUE, self.coords, self.radius]

    def change_coords(self):
        self.coords = self.next_coords()
        return self

    def next_coords(self):
        if self.type:
            return (min(max(self.radius + BORDERS,
                                   self.coords[0] + self.movement.x),
                               self.window_length // 2 - self.radius - 50),
                           min(max(self.radius + BORDERS,
                                   self.coords[1] + self.movement.y),
                               self.window_height - self.radius - BORDERS))
        else:
            return (min(max(self.radius +
                                   self.window_length //
                                   2 + 50, self.coords[0] +
                                   self.movement.x), self.window_length - BORDERS -
                               self.radius), min(max(self.radius + BORDERS, self.coords[1] +
                                                     self.movement.y), self.window_height - BORDERS -
                                                 self.radius))

    def get_coords(self):
        return self.coords

    def change_movement(self):
        return self.movement
