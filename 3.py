from Position import Position

pos = Position("Александр", "Сергеев", "Разработчик", 150000, 35000)

print(f"Атрибуты класса Position: {pos.name}, {pos.surname}, {pos.position}, {pos._income}")
pos.get_full_name()
pos.get_total_income()
