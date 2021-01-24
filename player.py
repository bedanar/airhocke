from movement import Movement
from constants import RED, BLUE


class Player:
    def __init__(self, coords, radius, type, window_height, window_length):
        self.coords = coords[0], coords[1]
        self.radius = radius
        self.type = type

        self.window_height = window_height
        self.window_length = window_length
        self.movement = Movement()
        # self.movement.change_koef(1)

    def draw_info(self, sc):
        return [sc, RED if self.type else BLUE, self.coords, self.radius]

    def change_coords(self):
        if self.type:
            self.coords = (min(max(self.radius,
                                   self.coords[0]+ self.movement.x),
                               self.window_length // 2 - self.radius),
                           min(max(self.radius,
                                   self.coords[1] + self.movement.y),
                               self.window_height - self.radius))
        else:
            self.coords = (min(max(self.radius +
                                   self.window_length //
                                   2, self.coords[0] +
                                   self.movement.x * self.movement.koef), self.window_length -
                               self.radius), min(max(self.radius, self.coords[1] +
                                                     self.movement.y * self.movement.koef), self.window_height -
                                                 self.radius))
        return self

    def next_coords(self):
        if self.type:
            return (min(max(self.radius,
                                   self.coords[0]+ self.movement.x),
                               self.window_length // 2 - self.radius),
                           min(max(self.radius,
                                   self.coords[1] + self.movement.y),
                               self.window_height - self.radius))
        else:
            return (min(max(self.radius +
                                   self.window_length //
                                   2, self.coords[0] +
                                   self.movement.x), self.window_length -
                               self.radius), min(max(self.radius, self.coords[1] +
                                                     self.movement.y), self.window_height -
                                                 self.radius))

    def get_coords(self):
        return self.coords

    def change_movement(self):
        return self.movement
