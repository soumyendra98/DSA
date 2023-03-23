# O(N * log(log(N))) and O(N)
from typing import List


def primeSieve(n: int) -> List[int]:
    if n < 2:
        return []

    val = set([i for i in range(2, n + 1)])
    p = 2
    while p ** 2 <= n:
        if p in val:
            for i in range(p ** 2, n + 1, p):
                if i in val:
                    val.remove(i)
        p += 1
    return list(val)


def isPrime(n):
    if n < 2:
        return False

    for x in range(2, int(n ** 0.5) + 1):
        if n % x == 0:
            return False
    return True
