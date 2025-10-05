#https://www.emojiall.com/ru/sub-categories/I11
from colorama import init, Fore, Back, Style

init(autoreset=True)

def draw_field(field, helicopter_pos):
    """
    Отрисовывает игровое поле в консоли.
    :param field: игровое поле
    :param helicopter_pos: текущая позиция вертолёта (x, y)
    """
    for i, row in enumerate(field):
        for j, cell in enumerate(row):
            if (i, j) == helicopter_pos:
                print(Fore.YELLOW + "🚁", end=" ")  # Вертолёт
            elif cell == "💧":  # Река
                print(Fore.BLUE + "💧", end=" ")
            elif cell == "🌳":  # Дерево
                print(Fore.GREEN + "🌳", end=" ")
            elif cell == "🔥":  # Пожар
                print(Fore.RED + "🔥", end=" ")
            elif cell == "🏥":  # Госпиталь
                print(Fore.CYAN + "🏥", end=" ")
            elif cell == "🛒":  # Магазин улучшений
                print(Fore.MAGENTA + "🛒", end=" ")
            elif cell == "🌩️":  # Грозовое облако
                print(Fore.YELLOW + "🌩️", end=" ")
            elif cell == "🔺":  # Сгоревшее дерево
                print(Fore.YELLOW + "🔺", end=" ")
            else:  # Пустая клетка
                print(Fore.WHITE + ".", end=" ")
        print()