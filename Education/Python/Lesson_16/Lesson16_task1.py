class CashRegister:
    def __init__(self, initial_money=0):
        """
        Инициализация кассы с начальным количеством денег.
        :param initial_money: начальное количество денег в кассе (по умолчанию 0)
        """
        self.money = initial_money

    def top_up(self, amount):
        """
        Пополнение кассы на указанную сумму.
        :param amount: сумма для пополнения
        """
        if amount < 0:
            raise ValueError("Сумма пополнения не может быть отрицательной.")
        self.money += amount
        print(f"Касса пополнена на {amount}. Текущий баланс: {self.money}")

    def count_1000(self):
        """
        Подсчёт целых тысяч в кассе.
        :return: количество целых тысяч
        """
        thousands = self.money // 1000
        print(f"В кассе {thousands} целых тысяч.")
        return thousands

    def take_away(self, amount):
        """
        Забрать деньги из кассы.
        :param amount: сумма для изъятия
        """
        if amount < 0:
            raise ValueError("Сумма изъятия не может быть отрицательной.")
        if self.money >= amount:
            self.money -= amount
            print(f"Из кассы изъято {amount}. Текущий баланс: {self.money}")
        else:
            raise ValueError("Недостаточно денег в кассе.")

# Пример использования
if __name__ == "__main__":
    # Создаем объект класса CashRegister
    cash_register = CashRegister(initial_money=5000)

    # Пополняем кассу
    cash_register.top_up(3000)

    # Считаем целые тысячи
    cash_register.count_1000()

    # Забираем деньги из кассы
    try:
        cash_register.take_away(4000)
    except ValueError as e:
        print(e)

    # Пытаемся забрать больше денег, чем есть в кассе
    try:
        cash_register.take_away(10000)
    except ValueError as e:
        print(e)