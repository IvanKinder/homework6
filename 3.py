from Class_3_1 import Position

income = {"Оклад": int(input("Введите оклад сотрудника: ")), "Премия": int(input("Введите премию сотрудника: "))}
pos = Position("Александр", "Сергеев", "Разработчик", income)

print(f"Атрибуты класса Position: {pos.name}, {pos.surname}, {pos.position}, {pos._income}")
pos.get_full_name()
pos.get_total_income()
