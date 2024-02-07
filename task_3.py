"""Homework"""


class Square:
    def __init__(self, side_length):
        self.side_length = side_length

    def area(self):
        return self.side_length ** 2

    def perimeter(self):
        return 4 * self.side_length

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.1415 * self.radius ** 2

    def circumference(self):
        return 2 * 3.1415 * self.radius

class CircleInSquare(Square, Circle):
    def __init__(self, side_length):
        super().__init__(side_length)
        self.radius = side_length / 2

    def area_difference(self):
        square_area = super().area()
        circle_area = super().area()
        return square_area - circle_area

    def display_info(self):
        print(f"Square side length: {self.side_length}")
        print(f"Circle radius: {self.radius}")
        print(f"Area difference: {self.area_difference()}")
