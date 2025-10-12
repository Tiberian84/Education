#include <iostream>

class BinarySearchTree {
public:
    // Конструктор для создания пустого дерева
    BinarySearchTree() : root(nullptr) {}

    // Публичный метод для вставки нового значения в дерево
    void insert(int value) {
        root = insert(root, value);
    }

    // Публичный метод для удаления значения из дерева
    void remove(int value) {
        root = remove(root, value);
    }

    // Публичный метод для поиска значения в дереве
    bool search(int value) {
        return search(root, value) != nullptr;
    }

    // Публичный метод для печати дерева в консоль
    void print() {
        inorder();
        std::cout << std::endl;
    }

private:
    // Определение структуры узла дерева
    struct Node {
        int value; // Значение узла
        Node* left; // Указатель на левого потомка
        Node* right; // Указатель на правого потомка

        // Конструктор для создания нового узла с заданным значением
        Node(int value) : value(value), left(nullptr), right(nullptr) {}
    };

    Node* root; // Корень дерева

    // Приватный метод для вставки нового значения в дерево
    Node* insert(Node* root, int value) {
        // Если дерево пустое, создаем новый корень
        if (root == nullptr) {
            return new Node(value);
        }

        // Если значение меньше значения корня, вставляем его в левое поддерево
        if (value < root->value) {
            root->left = insert(root->left, value);
        }
        // Иначе вставляем его в правое поддерево
        else {
            root->right = insert(root->right, value);
        }

        // Возвращаем новый корень дерева
        return root;
    }

    // Приватный метод для удаления значения из дерева
    Node* remove(Node* root, int value) {
        // Если дерево пустое, возвращаем nullptr
        if (root == nullptr) {
            return nullptr;
        }

        // Если значение меньше значения корня, удаляем его из левого поддерева
        if (value < root->value) {
            root->left = remove(root->left, value);
        }
        // Если значение больше значения корня, удаляем его из правого поддерева
        else if (value > root->value) {
            root->right = remove(root->right, value);
        }
        // Иначе удаляем корень
        else {
            // Если у корня нет потомков или только один потомок
            if (root->left == nullptr) {
                Node* temp = root->right;
                delete root;
                return temp;
            }
            else if (root->right == nullptr) {
                Node* temp = root->left;
                delete root;
                return temp;
            }
            // Если у корня есть оба потомка
            else {
                // Находим узел с минимальным значением в правом поддереве
                Node* temp = findMin(root->right);
                // Копируем значение этого узла в корень
                root->value = temp->value;
                // Удаляем этот узел из правого поддерева
                root->right = remove(root->right, temp->value);
            }
        }

        // Возвращаем новый корень дерева
        return root;
    }

    // Приватный метод для поиска значения в дереве
    Node* search(Node* root, int value) {
        // Если дерево пустое или значение найдено, возвращаем корень
        if (root == nullptr || root->value == value) {
            return root;
        }

        // Если значение меньше значения корня, ищем его в левом поддереве
        if (value < root->value) {
            return search(root->left, value);
        }
        // Иначе ищем его в правом поддереве
        else {
            return search(root->right, value);
        }
    }

    // Приватный метод для нахождения узла с минимальным значением в дереве
    Node* findMin(Node* root) {
        while (root->left != nullptr) {
            root = root->left;
        }
        return root;
    }

    // Приватный метод для печати узлов дерева в порядке возрастания
    void inorder() {
        inorderHelper(root);
    }

    // Приватный рекурсивный метод-помощник для печати
    void inorderHelper(Node* root) {
        // Если дерево не пустое
        if (root != nullptr) {
            // Обходим левое поддерево
            inorderHelper(root->left);
            // Печатаем значение корня
            std::cout << root->value << ' ';
            // Обходим правое поддерево
            inorderHelper(root->right);
        }
    }
};

int main() {
    BinarySearchTree tree;
    tree.insert(8);
    tree.insert(3);
    tree.insert(10);
    tree.insert(1);
    tree.insert(6);
    tree.insert(14);
    tree.insert(4);
    tree.insert(7);
    tree.insert(13);
    tree.print(); // 1 3 4 6 7 8 10 13 14

    std::cout << "Search 3: " << (tree.search(3) ? "Found" : "Not found") << std::endl;
    tree.remove(3);
    std::cout << "Search 3: " << (tree.search(3) ? "Found" : "Not found") << std::endl;
    tree.print(); // 1 4 6 7 8 10 13 14

    // Чтобы консоль не закрывалась сразу
    std::cin.get();
    return 0;
}