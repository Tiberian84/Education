import collections

# Инициализация словаря pets
pets = {
    1: {"Мухтар": {"Вид питомца": "Собака", "Возраст питомца": 9, "Имя владельца": "Павел"}},
    2: {"Каа": {"Вид питомца": "желторотый питон", "Возраст питомца": 19, "Имя владельца": "Саша"}},
}

# Функция для получения суффикса возраста
def get_suffix(age):
    if age % 10 == 1 and age % 100 != 11:
        return "год"
    elif 2 <= age % 10 <= 4 and (age % 100 < 10 or age % 100 >= 20):
        return "года"
    else:
        return "лет"

# Функция для получения информации о питомце по ID
def get_pet(ID):
    return pets[ID] if ID in pets.keys() else False

# Функция для отображения списка всех питомцев
def pets_list():
    for pet_id, pet_info in pets.items():
        for name, details in pet_info.items():
            print(f"ID: {pet_id}, Кличка: {name}, Вид: {details['Вид питомца']}, "
                  f"Возраст: {details['Возраст питомца']} {get_suffix(details['Возраст питомца'])}, "
                  f"Владелец: {details['Имя владельца']}")

# Функция для создания новой записи
def create():
    # Получаем последний ключ (ID) из словаря
    last = collections.deque(pets, maxlen=1)[0]
    new_id = last + 1

    # Запрашиваем данные о новом питомце
    name = input("Введите кличку питомца: ")
    pet_type = input("Введите вид питомца: ")
    age = int(input("Введите возраст питомца: "))
    owner_name = input("Введите имя владельца: ")

    # Добавляем новую запись в словарь
    pets[new_id] = {name: {"Вид питомца": pet_type, "Возраст питомца": age, "Имя владельца": owner_name}}
    print(f"Питомец {name} успешно добавлен с ID: {new_id}")

# Функция для чтения информации о питомце
def read():
    pet_id = int(input("Введите ID питомца: "))
    pet_info = get_pet(pet_id)

    if pet_info:
        for name, details in pet_info.items():
            print(f"Это {details['Вид питомца']} по кличке \"{name}\". "
                  f"Возраст питомца: {details['Возраст питомца']} {get_suffix(details['Возраст питомца'])}. "
                  f"Имя владельца: {details['Имя владельца']}")
    else:
        print("Питомец с таким ID не найден.")

# Функция для обновления информации о питомце
def update():
    pet_id = int(input("Введите ID питомца для обновления: "))
    pet_info = get_pet(pet_id)

    if pet_info:
        for name, details in pet_info.items():
            print(f"Текущая информация о питомце {name}:")
            print(f"Вид: {details['Вид питомца']}, Возраст: {details['Возраст питомца']}, Владелец: {details['Имя владельца']}")

            # Запрашиваем новые данные
            new_pet_type = input("Введите новый вид питомца (или оставьте пустым, чтобы не менять): ") or details['Вид питомца']
            new_age = int(input("Введите новый возраст питомца (или введите 0, чтобы не менять): ")) or details['Возраст питомца']
            new_owner_name = input("Введите новое имя владельца (или оставьте пустым, чтобы не менять): ") or details['Имя владельца']

            # Обновляем информацию
            pets[pet_id][name] = {"Вид питомца": new_pet_type, "Возраст питомца": new_age, "Имя владельца": new_owner_name}
            print(f"Информация о питомце {name} успешно обновлена.")
    else:
        print("Питомец с таким ID не найден.")

# Функция для удаления записи о питомце
def delete():
    pet_id = int(input("Введите ID питомца для удаления: "))
    pet_info = get_pet(pet_id)

    if pet_info:
        for name in pet_info.keys():
            del pets[pet_id]
            print(f"Питомец {name} успешно удалён.")
    else:
        print("Питомец с таким ID не найден.")

# Основной цикл программы
command = ""
while command != "stop":
    print("\nДоступные команды:")
    print("create - создать новую запись")
    print("read - прочитать информацию о питомце")
    print("update - обновить информацию о питомце")
    print("delete - удалить запись о питомце")
    print("list - вывести список всех питомцев")
    print("stop - завершить программу")

    command = input("Введите команду: ").strip().lower()

    if command == "create":
        create()
    elif command == "read":
        read()
    elif command == "update":
        update()
    elif command == "delete":
        delete()
    elif command == "list":
        pets_list()
    elif command != "stop":
        print("Неизвестная команда. Попробуйте снова.")