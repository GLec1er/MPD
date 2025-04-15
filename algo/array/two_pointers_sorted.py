# отсортированный по возрастанию
def two_pointers(arr, target):
    left = 0
    right = len(arr) - 1

    while left < right:
        lr = arr[left] + arr[right]

        if lr == target:
            return arr[left], arr[right]

        elif lr < target:
            left += 1

        elif lr > target:
            right -= 1

    return None


a = [2, 7, 8, 9, 11, 12, 16, 21]
sm = 19
print(two_pointers(arr=a, target=sm))
