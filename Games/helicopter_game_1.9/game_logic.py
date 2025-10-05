import random
import time
from field_generator import create_field, generate_rivers, generate_trees, generate_fire, generate_objects
from utils import draw_field
from settings import FIELD_WIDTH, FIELD_HEIGHT

class Helicopter:
    def __init__(self, start_position=(0, 0)):
        """
        Инициализация вертолёта.
        :param start_position: начальная позиция вертолёта (x, y)
        """
        self.position = start_position
        self.water_tank = 0
        self.lives = 3
        self.score = 0

    def move(self, field, direction):
        """
        Перемещает вертолёт по карте.
        :param field: игровое поле
        :param direction: направление движения ("up", "down", "left", "right")
        """
        x, y = self.position
        rows, cols = len(field), len(field[0])

        if direction == "up" and x > 0:
            x -= 1
        elif direction == "down" and x < rows - 1:
            x += 1
        elif direction == "left" and y > 0:
            y -= 1
        elif direction == "right" and y < cols - 1:
            y += 1

        self.position = (x, y)

    def extinguish(self, field):
        """
        Тушит пожар, если вертолёт находится над горящим деревом.
        :param field: игровое поле
        """
        x, y = self.position
        if field[x][y] == "🔥" and self.water_tank > 0:
            field[x][y] = "🌳"  # Пожар потушен, снова дерево
            self.water_tank -= 1
            self.score += 10  # Награда за тушение пожара
            print("Пожар потушен!")
        elif field[x][y] != "🔥":
            print("Здесь нет пожара!")
        else:
            print("Недостаточно воды!")

    def collect_water(self, field):
        """
        Собирает воду, если вертолёт находится над рекой.
        :param field: игровое поле
        """
        x, y = self.position
        if field[x][y] == "💧":
            self.water_tank += 1
            print("Вода собрана!")
        else:
            print("Здесь нет реки!")

    def visit_hospital(self):
        """
        Вертолёт заходит в госпиталь и восстанавливает жизни за очки.
        """
        if self.score >= 50:
            self.score -= 50
            self.lives += 1
            print("Вы зашли в госпиталь. Жизнь восстановлена!")
        else:
            print("Недостаточно очков для восстановления жизни!")

    def upgrade_tank(self):
        """
        Увеличивает вместимость резервуара за очки.
        """
        if self.score >= 30:
            self.score -= 30
            self.water_tank += 2
            print("Резервуар увеличен!")
        else:
            print("Недостаточно очков для улучшения резервуара!")

def game_loop(helicopter=None, field=None):
    from save_load import save_game

    if not helicopter or not field:
        field = create_field(FIELD_WIDTH, FIELD_HEIGHT)
        generate_rivers(field)
        generate_trees(field)
        generate_objects(field)
        helicopter = Helicopter()

    while helicopter.lives > 0:
        draw_field(field, helicopter.position)
        print(f"Очки: {helicopter.score}, Вода: {helicopter.water_tank}, Жизни: {helicopter.lives}")
        
        command = input("Введите команду (w/a/s/d - движение, e - тушить, r - собрать воду, h - госпиталь, u - улучшение, s - сохранить, q - выход): ").lower()
        if command in ["w", "a", "s", "d"]:
            direction = {"w": "up", "a": "left", "s": "down", "d": "right"}[command]
            helicopter.move(field, direction)
        elif command == "e":
            helicopter.extinguish(field)
        elif command == "r":
            helicopter.collect_water(field)
        elif command == "h":
            helicopter.visit_hospital()
        elif command == "u":
            helicopter.upgrade_tank()
        elif command == "s":
            save_game(field, helicopter)
            print("Игра сохранена!")
        elif command == "q":
            break
        
        generate_fire(field)
        time.sleep(1)  # Задержка между тиками