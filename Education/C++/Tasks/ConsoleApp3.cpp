#include <iostream>
#include <vector>
#include <algorithm>
#include <windows.h>

using namespace std;

int minCoins(vector<int>& coins, int amount) {
    int count = 0;
    int remaining = amount;

    vector<int> sortedCoins = coins;
    sort(sortedCoins.begin(), sortedCoins.end(), greater<int>());

    for (int coin : sortedCoins) {
        while (remaining >= coin) {
            remaining -= coin;
            count++;
        }
    }

    if (remaining > 0) {
        return -1;
    }

    return count;
}

int main() {

    vector<int> coins = {10, 5, 2, 1}; // Номиналы монет в рублях
    int amount;

    cout << "Enter the amount to make (in rubles): ";
    if (cin >> amount && amount >= 0) {
        int result = minCoins(coins, amount);
        if (result != -1) {
            cout << "Minimum number of coins: " << result << endl;
        } else {
            cout << "Unable to make the amount with given denominations." << endl;
        }
    } else {
        cout << "Error: Please enter a valid positive amount." << endl;
    }

    cin.get(); // Пропускаем символ новой строки
    cin.get(); // Ожидание ввода
    return 0;
}