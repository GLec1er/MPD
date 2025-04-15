def revert_list_two_pointers(arr):
    left = 0
    right = len(arr) - 1

    while left < right:
        arr[left], arr[right] = arr[right], arr[left]
        left += 1
        right -= 1

    return arr


a = [2, 7, 8, 9, 11, 12, 16, 21]
print(revert_list_two_pointers(arr=a))
