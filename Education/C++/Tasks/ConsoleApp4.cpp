#include <iostream>
#include <vector>
#include <algorithm>
#include <windows.h>
using namespace std;

// Структура для хранения информации о занятии
struct Activity {
    int start;
    int finish;
};

// Функция сравнения для сортировки занятий по времени окончания
bool compareByFinish(const Activity& a, const Activity& b) {
    return a.finish < b.finish;
}

// Жадный алгоритм для выбора максимального числа не пересекающихся занятий
void selectMaxActivities(vector<Activity>& activities) {
    // Сортируем занятия по времени окончания
    sort(activities.begin(), activities.end(), compareByFinish);

    cout << "Выбранные занятия (начало, конец):" << endl;
    int count = 0;
    int lastFinish = -1;

    for (const Activity& activity : activities) {
        if (activity.start >= lastFinish) {
            cout << "(" << activity.start << ", " << activity.finish << ")" << endl;
            lastFinish = activity.finish;
            count++;
        }
    }

    cout << "Максимальное количество занятий: " << count << endl;
}

int main() {
    SetConsoleOutputCP(CP_UTF8); // Установка UTF-8 для корректного вывода в Windows

    // Пример данных из задания (можно настроить по необходимости)
    vector<Activity> activities = {
        {1, 4}, {3, 5}, {0, 6}, {5, 7}, {3, 8}, {5, 9}, {6, 10}, {8, 11}, {8, 12}, {2, 13}, {12, 14}
    };

    selectMaxActivities(activities);

    cin.get(); // Пропускаем символ новой строки
    cin.get(); // Ожидание ввода для предотвращения закрытия консоли
    return 0;
}