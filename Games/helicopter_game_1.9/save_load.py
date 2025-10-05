import pickle

def save_game(field, helicopter):
    with open("savegame.pkl", "wb") as f:
        pickle.dump((field, helicopter.position, helicopter.water_tank, helicopter.score, helicopter.lives), f)
    print("Игра успешно сохранена!")

def load_game():
    try:
        with open("savegame.pkl", "rb") as f:
            data = pickle.load(f)
            field, position, water_tank, score, lives = data
            from game_logic import Helicopter
            helicopter = Helicopter(position)
            helicopter.water_tank = water_tank
            helicopter.score = score
            helicopter.lives = lives
            return field, helicopter
    except FileNotFoundError:
        print("Файл сохранения не найден.")
        return None