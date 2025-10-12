import math

class Turtle:
    def __init__(self, x=0, y=0, s=1):
        """
        Инициализация черепашки с начальными координатами и шагом.
        :param x: начальная координата x (по умолчанию 0)
        :param y: начальная координата y (по умолчанию 0)
        :param s: шаг перемещения (по умолчанию 1)
        """
        self.x = x
        self.y = y
        self.s = s

    def go_up(self):
        """Перемещение вверх."""
        self.y += self.s
        print(f"Черепашка переместилась вверх. Текущая позиция: ({self.x}, {self.y})")

    def go_down(self):
        """Перемещение вниз."""
        self.y -= self.s
        print(f"Черепашка переместилась вниз. Текущая позиция: ({self.x}, {self.y})")

    def go_left(self):
        """Перемещение влево."""
        self.x -= self.s
        print(f"Черепашка переместилась влево. Текущая позиция: ({self.x}, {self.y})")

    def go_right(self):
        """Перемещение вправо."""
        self.x += self.s
        print(f"Черепашка переместилась вправо. Текущая позиция: ({self.x}, {self.y})")

    def evolve(self):
        """Увеличение шага на 1."""
        self.s += 1
        print(f"Шаг увеличен. Текущий шаг: {self.s}")

    def degrade(self):
        """Уменьшение шага на 1. Выбрасывает ошибку, если шаг станет ≤ 0."""
        if self.s <= 1:
            raise ValueError("Шаг не может быть ≤ 0.")
        self.s -= 1
        print(f"Шаг уменьшен. Текущий шаг: {self.s}")

    def count_moves(self, x2, y2):
        """
        Подсчёт минимального количества действий для достижения точки (x2, y2).
        :param x2: целевая координата x
        :param y2: целевая координата y
        :return: минимальное количество действий
        """
        # Вычисляем разницу между текущими и целевыми координатами
        dx = abs(x2 - self.x)
        dy = abs(y2 - self.y)

        # Если разница не делится нацело на шаг, округляем вверх
        moves_x = math.ceil(dx / self.s)
        moves_y = math.ceil(dy / self.s)

        # Общее количество действий
        total_moves = moves_x + moves_y
        print(f"Минимальное количество действий до точки ({x2}, {y2}): {total_moves}")
        return total_moves

# Пример использования
if __name__ == "__main__":
    # Создаем объект класса Turtle
    turtle = Turtle(x=0, y=0, s=2)

    # Перемещаем черепашку
    turtle.go_right()
    turtle.go_up()

    # Увеличиваем шаг
    turtle.evolve()

    # Считаем минимальное количество действий до точки (5, 7)
    turtle.count_moves(5, 7)

    # Пытаемся уменьшить шаг до ≤ 0
    try:
        turtle.degrade()
        turtle.degrade()
        turtle.degrade()
    except ValueError as e:
        print(e)