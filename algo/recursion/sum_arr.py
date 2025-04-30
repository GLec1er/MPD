def sum_arr(arr):
    if not arr:
        return 0

    return arr[0] + sum(arr[1:])


print(sum_arr(arr=[1, 2, 3, 4]))
