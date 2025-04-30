# Дан отсортированный по возрастанию массив целых чисел и некоторое целое число.
# Ваша задача — найти минимальный диапазон индексов (подмассив), в котором может находиться заданное число.
# Используйте метод экспоненциального поиска.


def expo_search(ln, arr, fn):
    border = 1
    last_el = ln - 1

    while border < last_el and arr[border] < fn:
        if arr[border] == fn:
            return f'{border} {border*2}'

        border *= 2

        if border > last_el:
            return f'{border // 2} {last_el}'

    return f'{border // 2} {border}'


ln = 11
arr = [8, 11, 12, 16, 18, 21, 33, 36, 48, 54, 63]
fn = 16

print(expo_search(ln, arr, fn))
