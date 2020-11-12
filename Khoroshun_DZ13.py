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
