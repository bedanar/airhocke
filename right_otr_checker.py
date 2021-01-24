from movement import Movement
from vector_math import *

for _ in  range(int(input())):
    first_point, second_point = Point(), Point()
    
    first_point.x, first_point.y = list(map(int, input('First point: ').split()))
    second_point.x, second_point.y = list(map(int, input("Second point: ").split()))
    begin_vector = Movement(*list(map(int, input("Begin vector: ").split())))
    print(list(map(lambda x: -x, calculate_rez_vector(normal_vector(first_point, second_point, Movement()), begin_vector).get_info())))
