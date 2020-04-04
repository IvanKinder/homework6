from Class_3 import Worker


class Position(Worker):
    def get_full_name(self):
        print(f"{self.name} {self.surname}")

    def get_total_income(self):
        print(sum(self._income.values()))
