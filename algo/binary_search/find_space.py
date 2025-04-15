def findSpace(ln, arr, fn):
    left = 0
    right = ln - 1

    while left <= right:
        mid = (left + right) // 2

        if arr[mid] == fn:
            return mid  # Число найдено, возвращаем его индекс

        if arr[mid] > fn:
            right = mid - 1  # Сужаем правую границу
        else:
            left = mid + 1  # Сужаем левую границу

    # Если число не найдено, возвращаем позицию для вставки
    return left


# Ввод данных
ln = int(input())
arr = list(map(int, input().split()))
fn = int(input())

# Вызов функции и вывод результата
print(findSpace(ln, arr, fn))
