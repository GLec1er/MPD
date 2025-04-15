def letters_inside(arr1, arr2):
    left = 0

    for right in range(len(arr2)):
        if left < len(arr1) and arr1[left] == arr2[right]:
            left += 1

    return left == len(arr1)


arr1 = 'abc'
arr2 = 'acccccbsc'
print(letters_inside(arr1, arr2))