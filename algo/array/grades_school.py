def move_zeros_to_end(n, grades):
    result = []
    zero_count = 0

    for i in range(n):
        if grades[i] == 0:
            zero_count += 1
        else:
            result.append(grades[i])

    result.extend([0] * zero_count)
    return result


# two pointers
def move_zeros_to_end_pointers(n, grades):
    non_zero_idx = 0

    for i in range(n):
        if grades[i] != 0:
            grades[non_zero_idx] = grades[i]
            non_zero_idx += 1

    for i in range(non_zero_idx, n):
        grades[i] = 0

    return grades


n = int(input())
grades = list(map(int, input().split()))
g = move_zeros_to_end_pointers(n, grades)
print(*g)

# nums = 6
# grades = [0, 0, 6, 0, 9, 8]
# print(move_zeros_to_end_pointers(n=nums, grades=grades))
