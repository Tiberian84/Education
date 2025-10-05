import random
import settings


class FieldGenerator:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def create_field(self):
        """
        Создаёт игровое поле заданного размера, заполняя его деревьями.
        :return: двумерный список
        """
        return [["🌳" for _ in range(self.width)] for _ in range(self.height)]

    
    def generate_lake(self, field):
        """
        Генерирует озеро в виде квадрата 2x2 из капель воды.
        :param field: игровое поле
        :return: координаты верхнего левого угла озера (start_row, start_col)
        """
        rows, cols = len(field), len(field[0])
        while True:
            start_row = random.randint(0, rows - 2)
            start_col = random.randint(0, cols - 2)
            if all(field[start_row + i][start_col + j] == "🌳" for i in range(2) for j in range(2)):
                for i in range(2):
                    for j in range(2):
                        field[start_row + i][start_col + j] = "💧"
                return start_row, start_col

    def generate_river(self, field, start_row, start_col):
        """
        Генерирует реку, которая начинается из озера и занимает 30% игрового поля.
        :param field: игровое поле
        :param start_row: начальная строка (из озера)
        :param start_col: начальный столбец (из озера)
        """
        rows, cols = len(field), len(field[0])
        total_cells = rows * cols
        river_length_target = int(0.3 * total_cells)  # 30% от общего количества клеток
        x, y = start_row, start_col
        direction = random.choice(["up", "down", "left", "right"])
        river_length = 0

        while river_length < river_length_target and 0 <= x < rows and 0 <= y < cols:
            if field[x][y] == "🌳":
                field[x][y] = "💧"
                river_length += 1

            if random.random() < 0.2:  # 20% шанс изменить направление
                direction = random.choice(["up", "down", "left", "right"])

            if direction == "up" and x > 0:
                x -= 1
            elif direction == "down" and x < rows - 1:
                x += 1
            elif direction == "left" and y > 0:
                y -= 1
            elif direction == "right" and y < cols - 1:
                y += 1
            else:
                direction = random.choice(["up", "down", "left", "right"])

        if river_length < river_length_target:
            print("❌ Ошибка: река не достигла целевой длины. Попробуйте увеличить размер поля.")

    def generate_fire(self, field, burning_trees, burned_trees):
        """
        Генерирует новые пожары и обновляет состояние горящих деревьев.
        :param field: игровое поле
        :param burning_trees: словарь с координатами горящих деревьев и их временем горения
        :param burned_trees: счётчик сгоревших деревьев
        :return: обновлённый счётчик сгоревших деревьев
        """
        rows, cols = len(field), len(field[0])

        # Обновляем состояние горящих деревьев
        for (row, col), time_left in list(burning_trees.items()):
            if time_left > 1:
                burning_trees[(row, col)] -= 1  # Уменьшаем время горения
            else:
                del burning_trees[(row, col)]  # Удаляем дерево из списка горящих
                burned_trees += 1  # Увеличиваем счётчик сгоревших деревьев
                field[row][col] = "🔺"  # Превращаем в кучку пепла

        # Поджигаем новые деревья
        for row in range(rows):
            for col in range(cols):
                if field[row][col] == "🌳" and random.random() < 0.01:  # 1% шанс поджечь дерево
                    field[row][col] = "🔥"
                    burning_trees[(row, col)] = settings.SET_BUR_TREE  # Начальное время горения — n ходов

        return burned_trees

    def generate_thunderclouds(self, field, thunderclouds_dict):
            """
            Генерирует 1–2 грозовых облака на поле.
            :param field: игровое поле
            :param thunderclouds_dict: словарь для хранения данных об облаках
            """
            rows, cols = len(field), len(field[0])
            num_clouds = random.randint(1, 2)
            for _ in range(num_clouds):
                while True:
                    row, col = random.randint(0, rows - 1), random.randint(0, cols - 1)
                    if field[row][col] in ["🌳", "💧"]:  # Можно ставить только на дерево или воду
                        original = field[row][col]
                        field[row][col] = "🌩️"
                        thunderclouds_dict[(row, col)] = {
                            "original_symbol": original,
                            "time_left": random.randint(10, 20)  # Облако исчезнет через 10–20 тиков
                        }
                        break

    def spawn_thundercloud(self, field, thunderclouds_dict):
        rows, cols = len(field), len(field[0])
        suitable_cells = [
            (r, c) for r in range(rows) for c in range(cols)
            if field[r][c] in ["🌳", "💧"] and (r, c) not in thunderclouds_dict
        ]
        if suitable_cells:
            row, col = random.choice(suitable_cells)
            original = field[row][col]
            field[row][col] = "🌩️"
            thunderclouds_dict[(row, col)] = {
                "original_symbol": original,
                "time_left": random.randint(10, 20)
            }

    def generate_field(self):
        """
        Генерирует полное игровое поле с реками, озером, деревьями, госпиталем и магазином.
        :return: готовое игровое поле
        """
        field = self.create_field()
        lake_start_row, lake_start_col = self.generate_lake(field)
        self.generate_river(field, lake_start_row, lake_start_col)
        self.place_objects(field, ["🏥", "🛒"])  # Госпиталь и магазин
        return field

    @staticmethod
    def place_objects(field, objects):
        """
        Размещает объекты (например, госпиталь или магазин) в случайных пустых клетках.
        :param field: игровое поле
        :param objects: список символов объектов для размещения (например, ["🏥", "🛒"])
        """
        rows, cols = len(field), len(field[0])
        for obj_symbol in objects:
            while True:
                row, col = random.randint(0, rows - 1), random.randint(0, cols - 1)
                if field[row][col] == "🌳":
                    field[row][col] = obj_symbol
                    break