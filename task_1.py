"""Homework"""


class Device:
    """
    Класс для представления общего устройства.
    """

    def __init__(self, brand, model, power):
        """
        Инициализирует объект устройства с атрибутами бренда, модели и мощности.
        """
        self.brand = brand
        self.model = model
        self.power = power

    def turn_on(self):
        """
        Включает устройство.
        """
        print(f"{self.brand} {self.model} теперь включено.")

    def turn_off(self):
        """
        Выключает устройство.
        """
        print(f"{self.brand} {self.model} теперь выключено.")


class CoffeeMachine(Device):
    """
    Класс для представления кофемашины, унаследованный от Device.
    """

    def __init__(self, brand, model, power, capacity):
        """
        Инициализирует объект CoffeeMachine с атрибутами бренда, модели, мощности и вместимости.
        """
        super().__init__(brand, model, power)
        self.capacity = capacity

    def make_coffee(self):
        """
        Готовит кофе с использованием кофемашины.
        """
        print(f"{self.brand} {self.model} готовит кофе.")


class Blender(Device):
    """
    Класс для представления блендера, унаследованный от Device.
    """

    def __init__(self, brand, model, power, speed_levels):
        """
        Инициализирует объект блендера с атрибутами бренда, модели, мощности и уровней скорости.
        """
        super().__init__(brand, model, power)
        self.speed_levels = speed_levels

    def blend(self):
        """
        Начинает мешать с помощью блендера.
        """
        print(f"{self.brand} {self.model} мешает.")


class MeatGrinder(Device):
    """
    Класс для представления мясорубки, унаследованный от Device.
    """

    def __init__(self, brand, model, power, blade_type):
        """
        Инициализирует объект MeatGrinder с атрибутами бренда, модели, мощности и типа лезвия.
        """
        super().__init__(brand, model, power)
        self.blade_type = blade_type

    def grind_meat(self):
        """
        Начинает измельчать мясо с помощью мясорубки.
        """
        print(f"{self.brand} {self.model} измельчает мясо.")


if __name__ == "__main__":
    coffee_machine = CoffeeMachine("Phillips", "CoffeGear-9000", 1000, 10)
    blender = Blender("LG", "Mixer-blander ultra 2.0", 750, 3)
    meat_grinder = MeatGrinder("Xiaomeat", "Mi Meatmaker plus", 1200, "Нержавеющая сталь")

    coffee_machine.turn_on()
    coffee_machine.make_coffee()
    coffee_machine.turn_off()

    blender.turn_on()
    blender.blend()
    blender.turn_off()

    meat_grinder.turn_on()
    meat_grinder.grind_meat()
    meat_grinder.turn_off()
