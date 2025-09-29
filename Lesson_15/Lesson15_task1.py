# Родительский класс Transport
class Transport:
    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage

# Дочерний класс Autobus
class Autobus(Transport):
    pass  # Наследуем всё от родительского класса

# Создание объекта класса Autobus
autobus = Autobus("Renaul Logan", 180, 12)

# Вывод данных объекта
print(f"Название автомобиля: {autobus.name} Скорость: {autobus.max_speed} Пробег: {autobus.mileage}")