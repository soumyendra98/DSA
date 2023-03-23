# 134, Single Pass | O(N) and O(1)
from typing import List


def canCompleteCircuit(gas: List[int], cost: List[int]) -> int:
    output = 0
    extra = 0
    tc = tg = 0
    for idx, c in enumerate(cost):
        tc += c
        tg += gas[idx]
        extra += gas[idx] - c
        if extra < 0:
            output = idx + 1
            extra = 0

    return output if tc <= tg else -1
