from Car import Car
from random import randint


class TownCar(Car):
    def show_speed(self):
        if self.speed > 60:
            print("Превышение скорости!!!")
        else:
            print(self.speed)


class SportCar(Car):
    def __init__(self, speed, color, name, is_police=False):
        super().__init__(color, name, is_police)
        self.speed = randint(120, 270)
        self.name = "Sportcar " + name


class WorkCar(Car):
    def show_speed(self):
        if self.speed > 40:
            print("Превышение скорости!!!")
        else:
            print(self.speed)


class PoliceCar(Car):
    def __init__(self, speed, color, name, is_police=True):
        super().__init__(speed, color, name, is_police)
        self.name = "Police car " + name
