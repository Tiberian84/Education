from game_logic import Game

def main():
    print("🌲🌳 ДОБРО ПОЖАЛОВАТЬ В ИГРУ 🚁 'СПАСАТЕЛЬНЫЙ ВЕРТОЛЁТ' 💧")
    print("⚡ Боритесь с огнём, собирайте воду и улучшайте свой вертолёт!")
    print("🏆 Станьте героем и спасите лес от разрушительных пожаров!")
    
    choice = input("\nНачать новую игру (n) или загрузить сохранение (l)? ").lower()
    
    game = Game()
    if choice == "l":
        game.load_game()
        if not game.is_loaded:
            print("❌ Загрузка не удалась. Начинаем новую игру.")
            game.start_new_game()
    else:
        game.start_new_game()

    game.run()

if __name__ == "__main__":
    main()