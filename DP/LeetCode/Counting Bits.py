# 338, Find (i / 2)th element | O(N) and O(N)
from typing import List


def countBits(n: int) -> List[int]:
    output = [0]
    for i in range(1, n + 1):
        output.append(i % 2 + output[i // 2])
    return output
