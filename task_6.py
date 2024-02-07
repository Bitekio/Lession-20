"""Homework"""


class Wheels:
    def __init__(self, number_of_wheels):
        self.number_of_wheels = number_of_wheels

    def rotate(self):
        print("Колеса вращаются.")


class Engine:
    def __init__(self, horsepower):
        self.horsepower = horsepower

    def start(self):
        print("Двигатель запущен.")

    def stop(self):
        print("Двигатель заглушен.")


class Doors:
    def __init__(self, number_of_doors):
        self.number_of_doors = number_of_doors

    def open(self):
        print("Двери открыты.")

    def close(self):
        print("Двери закрыты.")


class Car(Wheels, Engine, Doors):
    def __init__(self, number_of_wheels, horsepower, number_of_doors):
        Wheels.__init__(self, number_of_wheels)
        Engine.__init__(self, horsepower)
        Doors.__init__(self, number_of_doors)

    def drive(self):
        print("Автомобиль едет.")


if __name__ == "__main__":
    car = Car(number_of_wheels=4, horsepower=200, number_of_doors=4)
    car.start()
    car.drive()
    car.rotate()
    car.open()
    car.close()
    car.stop()
