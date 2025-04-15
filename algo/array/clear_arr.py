def clear_arr(n, arr, dl):
    for val in arr[:]:
        if val == dl:
            arr.remove(val)
    return arr


n = int(input())
arr = list(map(int, input().split()))
dl = int(input())

cl = clear_arr(n, arr, dl)
print(*cl)