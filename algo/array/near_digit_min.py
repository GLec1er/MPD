# Дан отсортированный массив положительных целых чисел. Необходимо найти такую пару соседних элементов, у которых абсолютная разница минимальна.
from itertools import combinations

def near_digit_min(n, arr):
    if len(arr) < 2:
        return None

    min_diff = float('inf')
    good_pair = None

    for i in range(len(arr) - 1):
        diff = arr[i + 1] - arr[i]

        if diff < min_diff:
            min_diff = diff
            good_pair = [arr[i], arr[i + 1]]

    return f'{good_pair[0]} {good_pair[1]}'


n = int(input())
arr = list(map(int, input().split()))
print(near_digit_min(n, arr))
