# Даны координаты центров двух окружностей (x1; y1) (x2; y2) и и их радиусы  R1 и R2.
# Находится ли одна окружность целиком внутри другой

# TODO: your code here
def distance(x1, y1, x2, y2):
    return ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5


def circle_inside(point_a, point_b, r_1, r_2):
    return distance(*point_a, *point_b) + r_2 <= r_1


print(circle_inside((10, 12),(14, 18),10,2))
print(circle_inside((10, 12),(14, 18),10,20))
print(circle_inside((10, 10),(12, 18),10,2))
