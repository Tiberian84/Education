import random

def create_field(width, height):
    """
    Создаёт игровое поле заданного размера.
    :param width: ширина поля
    :param height: высота поля
    :return: двумерный список
    """
    return [[" " for _ in range(width)] for _ in range(height)]

def generate_rivers(field, num_rivers=2):
    rows, cols = len(field), len(field[0])
    for _ in range(num_rivers):
        start_row = random.randint(0, rows - 1)
        start_col = random.randint(0, cols - 1)
        length = random.randint(3, 6)
        direction = random.choice(["horizontal", "vertical"])
        
        if direction == "horizontal":
            for i in range(length):
                if start_col + i < cols:
                    field[start_row][start_col + i] = "💧"
        else:
            for i in range(length):
                if start_row + i < rows:
                    field[start_row + i][start_col] = "💧"

def generate_trees(field, num_trees=10):
    rows, cols = len(field), len(field[0])
    for _ in range(num_trees):
        row, col = random.randint(0, rows - 1), random.randint(0, cols - 1)
        if field[row][col] == " ":
            field[row][col] = "🌳"

def generate_fire(field):
    rows, cols = len(field), len(field[0])
    for row in range(rows):
        for col in range(cols):
            if field[row][col] == "🌳" and random.random() < 0.1:
                field[row][col] = "🔥"

def generate_objects(field):
    rows, cols = len(field), len(field[0])
    hospital_pos = (random.randint(0, rows - 1), random.randint(0, cols - 1))
    shop_pos = (random.randint(0, rows - 1), random.randint(0, cols - 1))

    if field[hospital_pos[0]][hospital_pos[1]] == " ":
        field[hospital_pos[0]][hospital_pos[1]] = "🏥"
    if field[shop_pos[0]][shop_pos[1]] == " ":
        field[shop_pos[0]][shop_pos[1]] = "🛒"