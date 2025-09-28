# Считываем строку чисел и преобразуем её в список
numbers = list(map(int, input("Введите последовательность чисел через пробел: ").split()))

# Множество для хранения уже встреченных чисел
seen_numbers = set()

# Проходим по каждому числу в списке
for number in numbers:
    if number in seen_numbers:
        print("YES")  # Число уже встречалось
    else:
        print("NO")   # Число встречается впервые
        seen_numbers.add(number)  # Добавляем число в множество