class Road:
    def __init__(self, length, width):
        self._length = length
        self._width = width

    def how_mass(self):
        print(self._length * self._width * 0.025 * 5, " тонн")
