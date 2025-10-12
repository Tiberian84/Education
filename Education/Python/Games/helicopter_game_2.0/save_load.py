import pickle

class SaveLoad:
    def save_game(self, field, helicopter_data):
        with open("savegame.pkl", "wb") as f:
            pickle.dump((field, helicopter_data), f)
        print("Игра успешно сохранена!")

    def load_game(self):
        try:
            with open("savegame.pkl", "rb") as f:
                data = pickle.load(f)
                field, helicopter_data = data
                return field, helicopter_data
        except FileNotFoundError:
            print("Файл сохранения не найден.")
            return None