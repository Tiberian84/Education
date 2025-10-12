from game_logic import game_loop
from save_load import load_game

def main():
    print("Добро пожаловать в игру 'Спасательный вертолёт'!")
    choice = input("Начать новую игру (n) или загрузить сохранение (l)? ").lower()
    
    if choice == "l":
        saved_data = load_game()
        if saved_data:
            print("Игра успешно загружена!")
            game_loop(*saved_data)
        else:
            print("Загрузка не удалась. Начинаем новую игру.")
            game_loop()
    else:
        game_loop()

if __name__ == "__main__":
    main()