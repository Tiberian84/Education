#include <iostream>
#include <vector>
#include <algorithm>
#include <windows.h> // Для SetConsoleOutputCP
#include <cstdint>   // Для INT64_MIN
using namespace std;

long long maxProductSubsequence(vector<int>& nums, int k) {
    int n = nums.size();
    if (k > n || k <= 0) return -1; // Неверные входные данные

    // Используем динамическое программирование
    // dp[i][j] — максимальное произведение подпоследовательности длины j, заканчивающейся на i
    vector<vector<long long>> dp(n, vector<long long>(k + 1, INT64_MIN));
    
    // Инициализация для подпоследовательностей длины 1
    for (int i = 0; i < n; i++) {
        dp[i][1] = nums[i];
    }

    // Заполняем таблицу динамического программирования
    for (int len = 2; len <= k; len++) {
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < i; j++) {
                if (dp[j][len - 1] != INT64_MIN) {
                    dp[i][len] = max(dp[i][len], dp[j][len - 1] * nums[i]);
                }
            }
        }
    }

    // Находим максимальное значение для длины k
    long long maxProduct = INT64_MIN;
    for (int i = 0; i < n; i++) {
        maxProduct = max(maxProduct, dp[i][k]);
    }

    return maxProduct == INT64_MIN ? -1 : maxProduct;
}

int main() {
    SetConsoleOutputCP(CP_UTF8); // Установка UTF-8 для корректного вывода в Windows

    vector<int> nums = {2, 3, -4, 5, -1}; // Пример массива
    int k;

    cout << "Enter the length of subsequence (k): ";
    cin >> k;

    long long result = maxProductSubsequence(nums, k);
    if (result != -1) {
        cout << "Maximum product of subsequence of length " << k << ": " << result << endl;
    } else {
        cout << "Invalid input or no valid subsequence found." << endl;
    }

    cin.get(); // Пропускаем символ новой строки
    cin.get(); // Ожидание ввода для предотвращения закрытия консоли
    return 0;
}