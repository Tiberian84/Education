# Функция для создания списка факториалов
def generate_factorials(n):
    # Создаём список для хранения факториалов
    factorials = []
    current_factorial = 1  # Начинаем с 1! = 1

    # Вычисляем факториалы от 1 до n
    for i in range(1, n + 1):
        current_factorial *= i  # Умножаем на текущее число
        factorials.append(current_factorial)

    # Возвращаем список факториалов в обратном порядке
    return factorials[::-1]

# Основная программа
number = int(input("Введите натуральное целое число от 1 до 100: "))

# Проверка, что число находится в допустимом диапазоне
if number <= 0 or number > 100:
    print("Ошибка: число должно быть натуральным целым (от 1 до 100).")
else:
    # Генерируем список факториалов
    result = generate_factorials(number)
    print(f"Факториал числа {number}: {result[0]}")
    print(f"Список факториалов чисел от {number}! до 1!: {result}")