# 1402, Positive Prefix Sum | O(N * (logN)) and O(1)
from typing import List

def maxSatisfaction(satisfaction: List[int]) -> int:
    satisfaction.sort(reverse=True)
    n = len(satisfaction)
    prefix = output = 0
    for i in range(n):
        prefix += satisfaction[i]
        if prefix < 0:
            break
        output += prefix

    return output
