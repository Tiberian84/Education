#include <iostream>
#include <vector>
using namespace std;

int main() {
    int n, m; // количество вершин и ребер
    cout << "Enter the number of vertices and edges: ";
    cin >> n >> m;

    vector<vector<pair<int, int>>> adj_list(n + 1); // список смежности
    vector<vector<int>> adj_matrix(n + 1, vector<int>(n + 1)); // матрица смежности

    cout << "Enter the edges (vertex1 vertex2 weight):" << endl;
    for (int i = 0; i < m; i++) {
        int v1, v2, w;
        cin >> v1 >> v2 >> w;
        // добавляем ребро в список смежности
        adj_list[v1].push_back({v2, w});
        adj_list[v2].push_back({v1, w});
        // добавляем ребро в матрицу смежности
        adj_matrix[v1][v2] = w;
        adj_matrix[v2][v1] = w;
    }

    cout << "Adjacency list:" << endl;
    for (int i = 1; i <= n; i++) {
        cout << i << ": ";
        for (auto j : adj_list[i]) {
            cout << "(" << j.first << ", " << j.second << ") ";
        }
        cout << endl;
    }

    cout << "Adjacency matrix:" << endl;
    for (int i = 1; i <= n; i++) {
        for (int j = 1; j <= n; j++) {
            cout << adj_matrix[i][j] << " ";
        }
        cout << endl;
    }

    return 0;
}