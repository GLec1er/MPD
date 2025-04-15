# https://cups.online/ru/workareas/education_2277/1221/2289/

# На складе хранятся контейнеры с товарами, каждому из которых присвоен номер. Чётный номер означает, что контейнер
# прошёл проверку качества. Ваша задача — найти номер последнего проверенного контейнера (последнего чётного числа в массиве).
# Если в массиве нет чётных чисел, вернуть -1


def containers(num, arr):
    for i in range(num - 1, -1, -1):
        if arr[i] % 2 == 0:
            return arr[i]

    return -1




num = int(input())
arr = list(map(int, input().split()))
print(containers(num, arr))
