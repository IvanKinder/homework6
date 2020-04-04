from time import sleep


class TrafficLight:
    __color = ""

    def change_color(self, color, sleep_time):
        self._TrafficLight__color = color
        print(self._TrafficLight__color, end='\r')
        sleep(sleep_time)

    def running(self):
        while True:
            self.change_color("Красный", 7)
            self.change_color("Жёлтый", 2)
            self.change_color("Зелёный", 10)
            self.change_color("Жёлтый", 2)
