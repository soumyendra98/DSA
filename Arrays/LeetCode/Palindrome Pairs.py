# 336 HashMap | O(N * W ^ 2) where W is the length of the longest word
from typing import List


def maximumScore(nums: List[int], multipliers: List[int]) -> int:
    store = [0] * (len(multipliers) + 1)
    n = len(nums)
    max_score = [0] * len(multipliers)
    for i in reversed(range(len(multipliers))):
        for j in range(i + 1):
            left = store[j + 1] + nums[j] * multipliers[i]
            right = store[j] + nums[n - i + j - 1] * multipliers[i]
            max_score[j] = max(left, right)
        store = max_score

    return store[0]
