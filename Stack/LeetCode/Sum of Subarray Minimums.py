# 907, Monotonic Stack + DP | O(N) and O(N)
from typing import List


def sumSubarrayMins(self, arr: List[int]) -> int:
    mod = 10 ** 9 + 7
    n = len(arr)
    total_sum = 0
    stack = []
    running_sum = [0] * n
    for i in range(n):
        while stack and arr[stack[-1]] > arr[i]:
            stack.pop()

        top = stack[-1] if stack else -1

        running_sum[i] = running_sum[top] + (i - top) * arr[i]
        total_sum += running_sum[i]

        stack.append(i)

    return total_sum % mod
