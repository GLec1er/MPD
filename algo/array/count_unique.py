from typing import List


def main(n: int, arr: List[int]) -> int:
    hash_map = {}

    for i in arr:
        if i not in hash_map:
            hash_map[i] = 1
        else:
            hash_map[i] += 1

    unique_count = 0
    for count in hash_map.values():
        if count == 1:
            unique_count += 1

    return unique_count


if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    print(main(n, arr))

from typing import List
from collections import Counter


def main(arr: List[int]) -> int:
    counter = Counter(arr)
    return sum(1 for count in counter.values() if count == 1)


if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    print(main(arr))