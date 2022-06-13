"""All function for instances."""
from pygame.math import Vector2
from game_instances import playable


def sq_dist(first: Vector2, second: Vector2) -> float | int:
    """Get squared distance from one point to another."""
    return (first.x - second.x) ** 2 + (first.y - second.y) ** 2


def collide(first: playable.MovableObject, second: playable.MovableObject) -> None:
    """
    Collide two movable objects.

    Change directions of two movable objects if they have a collision.
    """
    # if they don't touch each other stop function
    if sq_dist(first.pos, second.pos) > (first.radius + second.radius) ** 2:
        return

    # calculationg vector between first and second objects
    main_axis_vector = Vector2(
        first.pos.x - second.pos.x, first.pos.y - second.pos.y)
    magnitude = main_axis_vector.magnitude()

    # speed projections on this vector
    first_projection = main_axis_vector.dot(
        first.movement) / magnitude
    second_projection = main_axis_vector.dot(
        second.movement) / magnitude

    # remove value of the projection from our speed
    # we will calculate new later
    first.movement -= first_projection * main_axis_vector / magnitude
    second.movement -= second_projection * main_axis_vector / magnitude

    total_weight = first.weight + second.weight

    # creating new speed projections according to phisics ot two objects
    first_new_speed = (first.weight - second.weight) / total_weight * \
        first_projection + 2 * second.weight / total_weight * second_projection
    second_new_speed = 2 * first.weight / total_weight * first_projection + \
        (second.weight - first.weight) / total_weight * second_projection

    # creating new movement on this axis
    first.movement += first_new_speed * main_axis_vector / magnitude
    second.movement += second_new_speed * main_axis_vector / magnitude
