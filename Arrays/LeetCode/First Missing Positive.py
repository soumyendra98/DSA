# 41, 3 Pass | O(N) and O(1)
from typing import List


def firstMissingPositive(nums: List[int]) -> int:
    isOne = False
    for i in range(len(nums)):
        if nums[i] == 1:
            isOne = True
        if nums[i] > len(nums) or nums[i] < 1:
            nums[i] = 1
    if not isOne:
        return 1

    for i in range(len(nums)):
        index = abs(nums[i]) - 1
        nums[index] = -abs(nums[index])

    for i in range(len(nums)):
        if nums[i] >= 0:
            return i + 1

    return len(nums) + 1


arr = [3,4,-1,1]

print(firstMissingPositive(arr))
