# 2517, Binary Search | O(N * log(Max(arr)) | O(1)
from typing import List


def maximumTastiness(price: List[int], k: int) -> int:
    price.sort()
    n = len(price)

    def check(val):
        prev, total = price[0], 1

        for i in range(1, n):
            if price[i] - prev >= val:
                total += 1
                prev = price[i]
            if total == k:
                return True

        return False

    left, right = 0, price[-1]

    while left < right:
        mid = (left + right) // 2
        if check(mid):
            left = mid + 1
        else:
            right = mid

    return left - 1
