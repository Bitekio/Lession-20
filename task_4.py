"""Homework"""


class Square:
    """
    Класс для представления квадрата.
    """

    def __init__(self, side_length):
        """
        Инициализирует объект квадрата с заданной длиной стороны.
        """
        self.side_length = side_length

    def area(self):
        """
        Вычисляет площадь квадрата.
        """
        return self.side_length ** 2

    def perimeter(self):
        """
        Вычисляет периметр квадрата.
        """
        return 4 * self.side_length

class Circle:
    """
    Класс для представления окружности.
    """

    def __init__(self, radius):
        """
        Инициализирует объект окружности с заданным радиусом.
        """
        self.radius = radius

    def area(self):
        """
        Вычисляет площадь окружности.
        """
        return 3.1415 * self.radius ** 2

    def circumference(self):
        """
        Вычисляет длину окружности.
        """
        return 2 * 3.1415 * self.radius

class CircleInSquare(Square, Circle):
    """
    Класс для представления окружности, вписанной в квадрат.
    """

    def __init__(self, side_length):
        """
        Инициализирует объект окружности, вписанной в квадрат, с заданной длиной стороны квадрата.
        """
        super().__init__(side_length)
        self.radius = side_length / 2

    def area_difference(self):
        """
        Вычисляет разницу площадей квадрата и вписанной окружности.
        """
        square_area = super().area()
        circle_area = super().area()
        return square_area - circle_area

    def display_info(self):
        """
        Выводит информацию о длине стороны квадрата, радиусе окружности и разнице площадей на экран.
        """
        print(f"Длина стороны квадрата: {self.side_length}")
        print(f"Радиус окружности: {self.radius}")
        print(f"Разница площадей: {self.area_difference()}")


if __name__ == "__main__":
    circle_in_square = CircleInSquare(10)
    circle_in_square.display_info()
