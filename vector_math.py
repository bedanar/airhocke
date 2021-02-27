class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __str__(self):
        return f"Point({self.x}, {self.y})"


def normal_vector(first_point, second_point, template):
    template.change_x((first_point.x - second_point.x))
    template.change_y((first_point.y - second_point.y))
    return template


def scalar(first, second):
    return first.x * second.x + first.y * second.y


def mult_vector(koef, vector):
    vector.set(*list(map(lambda x: x * koef, vector.get())))
    return vector


def calculate_rez_vector(normal_vector, begin_vector):
    koef = scalar(normal_vector, begin_vector) / \
        scalar(normal_vector, normal_vector)
    mult_vector(-2 * koef, normal_vector)
    return mult_vector(-1, normal_vector + begin_vector)
