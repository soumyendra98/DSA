# 2125, Single pass | O(N * K) and O(1)
from typing import List


def numberOfBeams(bank: List[str]) -> int:
    n = len(bank)

    total = 0
    curr = 0
    for val in bank:
        count = val.count('1')
        if count != 0:
            total += curr * count
            curr = count

    return total
