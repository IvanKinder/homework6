from random import randint
from Car import Car
from Cars import TownCar, SportCar, WorkCar, PoliceCar

car = Car(randint(0, 120), "Белый", "Nissan")
print(f"Сейчас будет всё для класса Car с атрибутами: {car.speed}, {car.color}, {car.name}, {car.is_police}:")
car.go()
car.stop()
car.turn()
car.show_speed()

town_car = TownCar(randint(0, 120), "Жёлтый", "Ford")
print(
    f"Сейчас будет всё для класса TownCar с атрибутами: {town_car.speed}, {town_car.color}, {town_car.name}, {town_car.is_police}:")
town_car.go()
town_car.stop()
town_car.turn()
town_car.show_speed()

sport_car = SportCar(randint(0, 120), "Красный", "Ferrari")
print(
    f"Сейчас будет всё для класса SportCar с атрибутами: {sport_car.speed}, {sport_car.color}, {sport_car.name}, {sport_car.is_police}:")
sport_car.go()
sport_car.stop()
sport_car.turn()
sport_car.show_speed()

work_car = WorkCar(randint(0, 120), "Чёрный", "Opel")
print(
    f"Сейчас будет всё для класса WorkCar с атрибутами: {work_car.speed}, {work_car.color}, {work_car.name}, {work_car.is_police}:")
work_car.go()
work_car.stop()
work_car.turn()
work_car.show_speed()

police_car = PoliceCar(randint(0, 120), "Белый", "УАЗ")
print(
    f"Сейчас будет всё для класса PoliceCar с атрибутами: {police_car.speed}, {police_car.color}, {police_car.name}, {police_car.is_police}:")
police_car.go()
police_car.stop()
police_car.turn()
police_car.show_speed()
