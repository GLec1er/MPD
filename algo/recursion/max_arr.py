def max_arr(arr):
    if len(arr) == 2:
        return arr[0] if arr[0] > arr[1] else arr[1]

    sub_max = max_arr(arr[1:])

    return arr[0] if arr[0] > sub_max else sub_max


print(max_arr(arr=[1, 2, 3, 4]))