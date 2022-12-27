# 279, Perfect Square | O(1) and O(1)
import math


def isSquare(n: int) -> bool:
    sq = int(math.sqrt(n))
    return sq * sq == n


def numSquares(self, n: int) -> int:
    while (n & 3) == 0:
        n >>= 2
    if (n & 7) == 7:
        return 4

    if self.isSquare(n):
        return 1

    for i in range(1, int(math.sqrt(n)) + 1):
        if self.isSquare(n - i * i):
            return 2
    return 3
