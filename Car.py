class Car:
    def __init__(self, speed, color, name, is_police=False):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print(f"{self.color} {self.name} is GO!")

    def stop(self):
        print(f"{self.color} {self.name} is STOP!")

    def turn(self):
        turn = input("Выберете направление движения: ")
        if turn.lower() == "вперед" or turn.lower() == "назад" or turn.lower() == "влево" or turn.lower() == "вправо" or turn.lower() == "прямо":
            print(f"Едем {turn}")
        else:
            print("Введите корректное направление!!! (Вперед (прямо), назад, влево, вправо)")

    def show_speed(self):
        print(f"Скорость {self.color} {self.name} = {self.speed}")
