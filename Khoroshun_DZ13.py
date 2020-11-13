import random


def create_random_triangle():
    x1 = random.uniform(-100, 100)
    x2 = random.uniform(-100, 100)
    x3 = random.uniform(-100, 100)
    y1 = random.uniform(-100, 100)
    y2 = random.uniform(-100, 100)
    y3 = random.uniform(-100, 100)
    coordinat = [(x1, y1), (x2, y2), (x3, y3)]
    print(tuple(coordinat))
    if abs((x3 - x1) / (x2 - x1) - (y3 - y1) / (y2 - y1)) <= 0.01:
        print("Точки лежат на одной прямой")
    else:
        print("Точки не лежат на одной прямой")
    return tuple(coordinat)


create_random_triangle()


def create_right_triangle(vert: tuple, square=100):
    x1 = vert[0]
    y1 = vert[1]
    x2 = x1
    y2 = y1 + ((2 * square) ** 0.5)
    x3 = y2
    y3 = y1
    coordinat_triangle = [(x1, y1), (x2, y2), (x3, y3)]
    print(coordinat_triangle)
    return tuple(coordinat_triangle)


my_coordinat = create_right_triangle((3, 5))


def triangle_square():
    print("Введите координаты вершин треугольника:")
    x1 = float(input("x1 = "))
    y1 = float(input("y1 = "))
    x2 = float(input("x2 = "))
    y2 = float(input("y2 = "))
    x3 = float(input("y3 = "))
    y3 = float(input("y3 = "))
    square = ((x1 - x3) * (y2 - y3) - (y1 - y3) * (x2 - x3)) / 2
    print("Площадь треугольника равна:")
    print(square)
    return square


triangle_square()

