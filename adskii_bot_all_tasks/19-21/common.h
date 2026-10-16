#include <stdbool.h>
#include <stdio.h>


// Аналог any(): возвращает true, если хотя бы один элемент массива истинен (не равен 0)
bool any(const int *arr, size_t size) {
    for (size_t i = 0; i < size; i++) {
        if (arr[i]) { // если элемент true / не ноль
            return true; // ранний выход (short-circuit)
        }
    }
    return false;
}

// Аналог all(): возвращает true, если абсолютно все элементы истинны
bool all(const int *arr, size_t size) {
    for (size_t i = 0; i < size; i++) {
        if (!arr[i]) { // если нашли хотя бы один false / ноль
            return false; // ранний выход
        }
    }
    return true;
}
