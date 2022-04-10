# Даны координаты трех точек (xa; ya) (xb; yb) (xc; yc),
# точки соединены отрезками AB, BC и AC. Найдите отрезок с минимальной длинной.
# Если отрезков с минимальной длиной несколько - вывести любой

# При решении задачи необходимо использовать функцию расстояния между двумя точками.

def distance(x1, y1, x2, y2):
    return ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5


# TODO: your code here

p_a = (10, 12)
p_b = (14, 18)
p_c = (12, 16)


def find_min_value(point_a, point_b, point_c):
    len_segments = {}
    len_segments["AB"] = distance(*point_a, *point_b)
    len_segments["BC"] = distance(*point_b, *point_c)
    len_segments["AC"] = distance(*point_a, *point_c)
    min_segment = distance(*point_a, *point_b)
    # return min(len_segments, key=len_segments.get) вариант #2
    for segment in len_segments:
        if len_segments[segment] < min_segment:
            min_segment = len_segments[segment]
            min_len_segment = segment
    return min_len_segment  # Вариант №1


print("Самый короткий отрезок:", find_min_value(p_a, p_b, p_c))  # Выводим название отрезка, например “АС”
