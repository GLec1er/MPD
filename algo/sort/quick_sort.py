def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    else:
        first = arr[0]
        middle = arr[len(arr) // 2]
        last = arr[-1]
        pivot = sorted([first, middle, last])[1]

        less = [i for i in arr if i < pivot]
        greater = [i for i in arr if i > pivot]

        return quick_sort(less) + [pivot] + quick_sort(greater)


ln = int(input())
arr = list(map(int, (input().split())))
print(' '.join(map(str, quick_sort(arr))))
