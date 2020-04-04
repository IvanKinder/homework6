from TrafficLight import TrafficLight

light = TrafficLight()
set_0 = ["Красный", "Жёлтый", "Зелёный"]
if set_0 == ["Красный", "Жёлтый", "Зелёный"]:
    light.running(set_0)
else:
    print("Светофор не поддерживает данный режим!")
