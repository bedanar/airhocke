from vector_math import *

class Movement:
    def __init__(self, x=10 ** -9, y=10 ** -8):
        self.x, self.y = x, y
        self.koef = 1

    def change_koef(self, koef):
        self.koef = koef
        return self

    def change_x(self, addition):
        self.x += addition

    def change_y(self, addition):
        self.y += addition

    def get(self):
        return (self.x) * self.koef, (self.y) * self.koef

    def get_info(self):
        return self.x, self.y

    def set(self, x, y):
        self.x, self.y = x, y
        return self

    def connect(self, over, first_center, second_center):
        before = self
        self.set(*calculate_rez_vector(normal_vector(first_center, second_center, Movement()), self).get_info())
        if self == before:
            mult_vector(-1, self)
        self.set(*(self + over).get_info())
        mult_vector(1.06, self)
        self.x, self.y = min(30, self.x), min(30, self.y)
        return self

    def __str__(self):
        return str((self.x, self.y))


    def __add__(self, other):
        return Movement(self.x + other.x, self.y + other.y)
