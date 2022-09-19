# 1770, Using Memoization | O(M^2) and O(M+1)
# The last multiplier has M-1 choices, whereas the first multiplier has 2
# choices, so in order to reach the optimal solution we need to traverse from the last element to the first element
# in our nums and find out all the possible values and store them in our MEMO or store.
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
