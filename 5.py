import Stationery

my_list = [Stationery.Stationery("Ластик"), Stationery.Pen("Ручка"), Stationery.Pencil(
    "Карандаш"), Stationery.Handle("Маркер")]

for object in my_list:
    print(object.title)
    object.draw()