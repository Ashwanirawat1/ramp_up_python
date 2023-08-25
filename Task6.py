import math


class Shape:
    def area(self):
        pass


class Square(Shape):
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side * self.side


class Triangle(Shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area(self):
        return 0.5 * self.base * self.height


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius * self.radius


def main():
    s = Square(5)
    t = Triangle(4, 6)
    c = Circle(3)

    shapes = [s, t, c]

    for shape in shapes:
        print(f"Area of {type(shape).__name__}: {shape.area()}")


main()
