# Ввод целого числа
number = int(input("Введите целое число: "))

# Определяем знак числа
if number > 0:
    sign = "положительное"
elif number < 0:
    sign = "отрицательное"
else:
    sign = "нулевое"

# Проверяем четность числа
if number == 0:
    description = "нулевое число"
else:
    if number % 2 == 0:
        parity = "четное число"
    else:
        parity = "и не является четным числом"
    
    # Формируем описание
    description = f"{sign} {parity}"

# Выводим результат
print(description)
