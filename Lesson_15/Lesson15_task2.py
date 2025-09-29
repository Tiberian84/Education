# Родительский класс Transport
class Transport:
    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage

    def seating_capacity(self, capacity):
        return f"Вместимость одного автобуса {self.name}: {capacity} пассажиров"

# Дочерний класс Autobus
class Autobus(Transport):
    def seating_capacity(self, capacity=50):  # Переопределение метода с значением по умолчанию
        return super().seating_capacity(capacity)  # Используем метод родительского класса

# Создание объекта класса Autobus
autobus = Autobus("Renaul Logan", 180, 12)

# Вызов переопределенного метода
print(autobus.seating_capacity())  # Используем значение по умолчанию