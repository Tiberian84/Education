import time
import settings
import random
from field_generator import FieldGenerator
from save_load import SaveLoad
from utils import draw_field


class Helicopter:
    def __init__(self, start_position=(0, 0)):
        """
        Инициализация вертолёта.
        :param start_position: начальная позиция вертолёта (x, y)
        """
        self.position = start_position
        self.water_tank = settings.INITIAL_WATER_TANK
        self.max_water_tank = settings.INITIAL_WATER_TANK_CAP  # Максимальный объём резервуара
        self.bucket_capacity = 1  # Количество воды, собираемое за раз
        self.lives = settings.INITIAL_LIVES
        self.max_lives = settings.INITIAL_WATER_LIVES_CAP  # Максимальное количество жизней
        self.score = 0
        self.extinguished_trees = 0  # Количество потушенных деревьев

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

    def extinguish(self, field, burning_trees):
        """
        Тушит пожар, если вертолёт находится над горящим деревом.
        :param field: игровое поле
        """
        x, y = self.position
        if field[x][y] == "🔥" and self.water_tank > 0:
            field[x][y] = "🌳"  # Пожар потушен, снова дерево
            self.water_tank -= 1
            self.score += 10  # Награда за тушение пожара
            del burning_trees[(x, y)]  # Удаляем дерево из списка горящих
            self.extinguished_trees += 1
            print("✅ Пожар потушен!")
        elif field[x][y] != "🔥":
            print("❌ Здесь нет пожара!")
        else:
            print("❌ Недостаточно воды!")

    def collect_water(self, field):
        """
        Собирает воду, если вертолёт находится над рекой.
        :param field: игровое поле
        """
        x, y = self.position
        if field[x][y] == "💧":
            available_space = self.max_water_tank - self.water_tank
            water_to_collect = min(self.bucket_capacity, available_space)
            if water_to_collect > 0:
                self.water_tank += water_to_collect
                print(f"✅ Вода собрана! (+{water_to_collect})")
            else:
                print("❌ Резервуар уже заполнен!")
        else:
            print("❌ Здесь нет реки!")

    def visit_hospital(self):
        """
        Вертолёт заходит в госпиталь и восстанавливает жизни за очки.
        """
        if self.score >= 50 and self.lives < self.max_lives:
            self.score -= 50
            self.lives += 1
            print("✅ Вы зашли в госпиталь. Жизнь восстановлена!")
        else:
            print("❌ Недостаточно очков или жизни уже максимум!")
    
    def buy_upgrade(self, choice):
        """
        Покупка улучшения в магазине.
        :param choice: выбранный товар (1 - ведро, 2 - резервуар, 3 - жизни, 0 - выход)
        """
        if choice == 0:
            print("🚪 Выход из магазина.")
            return

        # Максимальные значения для улучшений
        MAX_BUCKET_CAPACITY = 5
        MAX_WATER_TANK = 30
        MAX_LIVES = 10

        if choice == 1:
            if self.score >= 20 and self.bucket_capacity < MAX_BUCKET_CAPACITY:
                self.score -= 20
                self.bucket_capacity += 1
                print(f"✅ Куплено ведро! Теперь вы можете собирать {self.bucket_capacity} воды за раз (максимум: {MAX_BUCKET_CAPACITY}).")
            else:
                print("❌ Недостаточно очков или достигнут предел улучшений ведра!")
        elif choice == 2:
            if self.score >= 30 and self.max_water_tank < MAX_WATER_TANK:
                self.score -= 30
                self.max_water_tank += 1
                print(f"✅ Куплен резервуар! Новый объём: {self.max_water_tank} из {MAX_WATER_TANK} возможных.")
            else:
                print("❌ Недостаточно очков или достигнут предел улучшений резервуара!")
        elif choice == 3:
            if self.score >= 50 and self.max_lives < MAX_LIVES:
                self.score -= 50
                self.max_lives += 1
                print(f"✅ Куплена жизнь! Текущие жизни: {self.lives}/{self.max_lives} (максимум: {MAX_LIVES}).")
            else:
                print("❌ Недостаточно очков или достигнут предел улучшений жизней!")
        else:
            print("❌ Неверный выбор!")

class Game:
    def __init__(self):
        self.field_generator = FieldGenerator(settings.FIELD_WIDTH, settings.FIELD_HEIGHT)
        self.field = None
        self.helicopter = None
        self.save_load = SaveLoad()
        self.is_loaded = False
        self.burning_trees = {}  # Словарь для учета горящих деревьев
        self.burned_trees = 0  # Счётчик сгоревших деревьев
        self.thunderclouds = {}  # Словарь для учета грозовых облаков

    def start_new_game(self):
        """Начинает новую игру."""
        self.field = self.field_generator.generate_field()
        self.helicopter = Helicopter()
        self.is_loaded = False
        self.burning_trees = {}
        self.burned_trees = 0
        self.thunderclouds = {}
        self.field_generator.generate_thunderclouds(self.field, self.thunderclouds)

    def update_thunderclouds(self):
        """
        Обновляет состояние грозовых облаков.
        """
        for (row, col), data in list(self.thunderclouds.items()):
            data["time_left"] -= 1
            if data["time_left"] <= 0:
                self.field[row][col] = data["original_symbol"]  # Восстанавливаем исходный символ
                del self.thunderclouds[(row, col)]
            else:
                # Действие грозового облака: поджигает дерево или наносит урон вертолёту
                if random.random() < 0.5:  # 50% шанс активности
                    for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                        nr, nc = row + dr, col + dc
                        if 0 <= nr < len(self.field) and 0 <= nc < len(self.field[0]):
                            if self.field[nr][nc] == "🌳":
                                self.field[nr][nc] = "🔥"
                                self.burning_trees[(nr, nc)] = 20
                                print("⚡ Грозовое облако подожгло дерево!")
                                break
                    if self.helicopter.position == (row, col):
                        self.helicopter.lives -= 1
                        print("⚡ Грозовое облако нанесло урон вертолёту!")

    def load_game(self):
        """Загружает сохранённую игру."""
        saved_data = self.save_load.load_game()
        if saved_data:
            self.field, helicopter_data = saved_data
            self.helicopter = Helicopter(helicopter_data["position"])
            self.helicopter.water_tank = helicopter_data["water_tank"]
            self.helicopter.max_water_tank = helicopter_data["max_water_tank"]
            self.helicopter.bucket_capacity = helicopter_data["bucket_capacity"]
            self.helicopter.lives = helicopter_data["lives"]
            self.helicopter.max_lives = helicopter_data["max_lives"]
            self.helicopter.score = helicopter_data["score"]
            self.burning_trees = helicopter_data["burning_trees"]
            self.burned_trees = helicopter_data.get("burned_trees", 0)
            self.thunderclouds = helicopter_data.get("thunderclouds", {})
            self.is_loaded = True
        else:
            print("❌ Загрузка не удалась. Начинаем новую игру.")
            self.start_new_game()

    def save_game(self):
        """Сохраняет текущее состояние игры."""
        helicopter_data = {
            "position": self.helicopter.position,
            "water_tank": self.helicopter.water_tank,
            "max_water_tank": self.helicopter.max_water_tank,
            "bucket_capacity": self.helicopter.bucket_capacity,
            "lives": self.helicopter.lives,
            "max_lives": self.helicopter.max_lives,
            "score": self.helicopter.score,
            "burning_trees": self.burning_trees,
            "burned_trees": self.burned_trees,
            "thunderclouds": self.thunderclouds,
        }
        self.save_load.save_game(self.field, helicopter_data)

    def run(self):
        """Основной игровой цикл."""
        while self.helicopter.lives > 0:
            # Выводим параметры состояния вертолёта
            print("\n=== 🚁 ВАШ ВЕРТОЛЁТ ===")
            print(
                f"🪙 : {self.helicopter.score} | "
                f"💧 : {self.helicopter.water_tank}/{self.helicopter.max_water_tank} | "
                f"🪣 : {self.helicopter.bucket_capacity} | "
                f"💖 : {self.helicopter.lives}/{self.helicopter.max_lives}"
            )

            # Выводим игровое поле
            print("\n=== 🌳 ИГРОВОЕ ПОЛЕ ===")
            draw_field(self.field, self.helicopter.position)

            # Выводим статистику очков и деревьев
            print("\n=== 📊 СТАТИСТИКА ===")
            print(
                f"💀 Сгорело деревьев: {self.burned_trees} | "
                f"✅ Потушено деревьев: {self.helicopter.extinguished_trees}"
            )

            # Ввод команды
            command = input("\nВведите команду (w/a/s/d - движение, e - тушить, r - собрать воду, h - госпиталь, u - улучшение, save - сохранить, q - выход): ").lower()
            if command in ["w", "a", "s", "d"]:
                direction = {"w": "up", "a": "left", "s": "down", "d": "right"}[command]
                self.helicopter.move(self.field, direction)
            elif command == "e":
                self.helicopter.extinguish(self.field, self.burning_trees)
            elif command == "r":
                self.helicopter.collect_water(self.field)
            elif command == "h":
                x, y = self.helicopter.position
                if self.field[x][y] == "🏥":
                    self.helicopter.visit_hospital()
                else:
                    print("❌ Вы не находитесь рядом с госпиталем!")
            elif command == "u":
                x, y = self.helicopter.position
                if self.field[x][y] == "🛒":
                    print("\n=== 🛒 МАГАЗИН УЛУЧШЕНИЙ ===")
                    while True:
                        print("💰 Ваши текущие параметры: "
                            f"🪙: {self.helicopter.score}, "
                            f"💧: {self.helicopter.water_tank}/{self.helicopter.max_water_tank}, "
                            f"🪣: {self.helicopter.bucket_capacity}, "
                            f"💖: {self.helicopter.lives}/{self.helicopter.max_lives}")
                        print("1. 🪣 (+1 к сбору воды) - 20 очков")
                        print("2. 🛢️ (+1 к вместимости) - 30 очков")
                        print("3. 💖 (+1 жизнь) - 50 очков")
                        print("0. 🚪 Выход из магазина")
                        choice = input("Выберите товар (1/2/3) или выберите (0) для выхода: ")
                        if choice.isdigit() and int(choice) in [0, 1, 2, 3]:
                            if int(choice) == 0:
                                print("🚪 Выход из магазина.")
                                break
                            self.helicopter.buy_upgrade(int(choice))
                        else:
                            print("❌ Неверный выбор!")
                else:
                    print("❌ Вы не находитесь рядом с магазином улучшений!")
            elif command == "save":
                self.save_game()
                print("💾 Игра сохранена!")
            elif command == "q":
                break

            # Обновление состояния поля и учёт сгоревших деревьев
            old_burned = self.burned_trees
            self.burned_trees = self.field_generator.generate_fire(self.field, self.burning_trees, self.burned_trees)
            newly_burned = self.burned_trees - old_burned

            # Штраф за сгоревшие деревья
            if newly_burned > 0:
                self.helicopter.score -= newly_burned * 5
                print(f"❌ Сгорело {newly_burned} деревьев! Штраф: {newly_burned * 5} очков.")
                if self.helicopter.score <= 0:
                    self.helicopter.score = 0
                    print("💀 У вас закончились очки! Игра окончена.")
                    break

            # Обновление грозовых облаков
            self.update_thunderclouds()

            time.sleep(1)  # Задержка между тиками
            