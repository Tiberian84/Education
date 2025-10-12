import random

# Функция для генерации матрицы
def generate_matrix(rows, cols):
    """
    Генерирует матрицу заданной размерности.
    :param rows: количество строк
    :param cols: количество столбцов
    :return: двумерный список (матрица)
    """
    return [[random.randint(-100, 100) for _ in range(cols)] for _ in range(rows)]

# Функция для сложения двух матриц
def add_matrices(matrix_1, matrix_2):
    """
    Складывает две матрицы одинаковой размерности.
    :param matrix_1: первая матрица
    :param matrix_2: вторая матрица
    :return: результирующая матрица
    """
    # Проверяем, что размерности матриц совпадают
    if len(matrix_1) != len(matrix_2) or len(matrix_1[0]) != len(matrix_2[0]):
        raise ValueError("Матрицы имеют разные размерности!")
    
    # Складываем матрицы
    result = [
        [matrix_1[i][j] + matrix_2[i][j] for j in range(len(matrix_1[0]))]
        for i in range(len(matrix_1))
    ]
    return result

# Функция для красивого вывода матрицы
def print_matrix(matrix):
    """
    Выводит матрицу в удобочитаемом формате.
    :param matrix: матрица для вывода
    """
    for row in matrix:
        print(row)

# Основная программа
if __name__ == "__main__":
    # Ввод размерности матриц
    rows = int(input("Введите количество строк: "))
    cols = int(input("Введите количество столбцов: "))

    # Генерация двух матриц
    matrix_1 = generate_matrix(rows, cols)
    matrix_2 = generate_matrix(rows, cols)

    # Вывод сгенерированных матриц
    print("\nМатрица 1:")
    print_matrix(matrix_1)

    print("\nМатрица 2:")
    print_matrix(matrix_2)

    # Сложение матриц
    try:
        matrix_3 = add_matrices(matrix_1, matrix_2)
        print("\nРезультат сложения матриц:")
        print_matrix(matrix_3)
    except ValueError as e:
        print(f"Ошибка: {e}")