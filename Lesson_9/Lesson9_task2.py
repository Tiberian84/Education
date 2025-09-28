def read_and_check_set():
    numbers = input("Введите числа через пробел: ").split()
    if len(numbers) > 100000:
        raise ValueError("Количество чисел в списке превышает 100000.")
    return set(map(int, numbers))

try:
    # Чтение первого множества
    set1 = read_and_check_set()

    # Чтение второго множества
    set2 = read_and_check_set()

    # Находим пересечение множеств
    common_elements = set1 & set2

    # Выводим количество общих элементов
    print(len(common_elements))

except ValueError as e:
    print(f"Ошибка: {e}")

    