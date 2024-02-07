"""Homework"""


class Ship:
    """
    Класс для представления корабля.
    """

    def __init__(self, name, length, displacement):
        """
        Инициализирует объект корабля с атрибутами названия, длины и водоизмещения.
        """
        self.name = name
        self.length = length
        self.displacement = displacement

    def move(self):
        """
        Перемещает корабль.
        """
        print(f"{self.name} перемещается по воде.")


class Frigate(Ship):
    """
    Класс для представления фрегата, унаследованный от Ship.
    """

    def __init__(self, name, length, displacement, missile_count):
        """
        Инициализирует объект фрегата с атрибутами названия, длины, водоизмещения и количества ракет.
        """
        super().__init__(name, length, displacement)
        self.missile_count = missile_count

    def fire_missile(self):
        """
        Открывает огонь ракетами.
        """
        print(f"{self.name} выпускает ракеты.")


class Destroyer(Ship):
    """
    Класс для представления эсминца, унаследованный от Ship.
    """

    def __init__(self, name, length, displacement, gun_caliber):
        """
        Инициализирует объект эсминца с атрибутами названия, длины, водоизмещения и калибра пушек.
        """
        super().__init__(name, length, displacement)
        self.gun_caliber = gun_caliber

    def fire_gun(self):
        """
        Открывает огонь из пушек.
        """
        print(f"{self.name} открывает огонь из пушек.")


class Cruiser(Ship):
    """
    Класс для представления крейсера, унаследованный от Ship.
    """

    def __init__(self, name, length, displacement, missile_count, gun_caliber):
        """
        Инициализирует объект крейсера с атрибутами названия, длины, водоизмещения, количества ракет
        и калибра пушек.
        """
        super().__init__(name, length, displacement)
        self.missile_count = missile_count
        self.gun_caliber = gun_caliber

    def fire_missile(self):
        """
        Открывает огонь ракетами.
        """
        print(f"{self.name} выпускает ракеты.")

    def fire_gun(self):
        """
        Открывает огонь из пушек.
        """
        print(f"{self.name} открывает огонь из пушек.")


if __name__ == "__main__":
    frigate = Frigate("British Frigate", 150, 5000, 30)
    destroyer = Destroyer("Planet Destroyer", 200, 8000, 127)
    cruiser = Cruiser("Titanicruiser", 250, 10000, 50, 152)

    frigate.move()
    frigate.fire_missile()

    destroyer.move()
    destroyer.fire_gun()

    cruiser.move()
    cruiser.fire_missile()
    cruiser.fire_gun()
