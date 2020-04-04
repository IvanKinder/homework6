from time import sleep


class TrafficLight:
    __color = ""

    def change_color(self, color, sleep_time):
        self._TrafficLight__color = color
        print(self._TrafficLight__color, end='\r')
        sleep(sleep_time)

    def running(self, colors):
        while True:
            self.change_color(colors[0], 7)
            self.change_color(colors[1], 2)
            self.change_color(colors[2], 10)
            self.change_color(colors[1], 2)
