# Ввод пятизначного числа
number = int(input("Введите пятизначное целое число: "))

# Разбиваем число на составляющие
units = number % 10  # Единицы
tens = (number // 10) % 10  # Десятки
hundreds = (number // 100) % 10  # Сотни
thousands = (number // 1000) % 10  # Тысячи
ten_thousands = number // 10000  # Десятки тысяч

# Выполняем математические операции
result = (tens ** units) * hundreds / (ten_thousands - thousands)

# Выводим результат
print(f"Результат: {result}")