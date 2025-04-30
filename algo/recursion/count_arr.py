def count_arr(arr):
    if not arr:
        return 0

    return 1 + count_arr(arr[1:])


print(count_arr(arr=[1, 2, 3, 4]))
