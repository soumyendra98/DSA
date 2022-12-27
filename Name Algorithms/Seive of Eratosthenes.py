from typing import List


def primeSieve(n: int) -> List[int]:
    if n < 2:
        return []

    val = set([i for i in range(2, n + 1)])

    while p ** 2 <= n:
        if p in val:
            for i in range(p ** 2, n + 1, p):
                val.remove(i)
        p += 1
    return val
