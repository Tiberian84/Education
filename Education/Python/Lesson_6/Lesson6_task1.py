# Ввод числа N
N = int(input("Введите количество чисел: "))

# Инициализация счетчика нулевых чисел
zero_count = 0

# Ввод N чисел и подсчет нулей
for _ in range(N):
    number = int(input("Введите число: "))
    if number == 0:
        zero_count += 1

# Вывод результата
print(f"Количество нулевых чисел: {zero_count}")