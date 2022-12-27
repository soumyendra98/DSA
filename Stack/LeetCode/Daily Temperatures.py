# 739, Monotonic Stack | O(N) and O(N)
from typing import List


def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
    n = len(temperatures)
    stack = []
    output = [0] * n
    for idx, val in enumerate(temperatures):
        while stack and stack[-1][0] < val:
            _, prev_idx = stack.pop()
            output[prev_idx] = idx - prev_idx
        stack.append((val, idx))
    return output
