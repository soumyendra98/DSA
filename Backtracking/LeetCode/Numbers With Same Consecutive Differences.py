# 967 DFS | O(2^N) and O(2^N)
from typing import List


def numsSameConsecDiff(n: int, k: int) -> List[int]:
    output = []

    def dfs(num, n):
        if n == 0:
            return output.append(num)

        last_digit = num % 10
        next_digits = set([last_digit + k, last_digit - k])

        for digit in next_digits:
            if 0 <= digit < 10:
                dfs(num * 10 + digit, n - 1)

    for i in range(1, 10):
        dfs(i, n - 1)

    return list(output)


print(numsSameConsecDiff(3, 7))
