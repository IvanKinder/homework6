from time import sleep


class TrafficLight:
    __color = ""

    def show(self):
        print(self._TrafficLight__color)

    def change_color(self, color):
        self._TrafficLight__color = color

    def running(self):
        while True:
            self.change_color("Красный")
            self.show()
            sleep(7)
            self.change_color("Жёлтый")
            self.show()
            sleep(2)
            self.change_color("Зелёный")
            self.show()
            sleep(10)
