# 1578 Greedy approach | O(N) and O(1)
from typing import List

## Two Pointer Approach
# def minCost(colors: str, neededTime: List[int]) -> int:
#     left = 0
#     right = 0
#     n = len(colors)
#     max_val = 0
#     curr_sum = 0
#     total = 0
#     while right < n:
#         print(curr_sum, max_val)
#         if colors[left] != colors[right]:
#             if flag:
#                 total +=  curr_sum - max_val
#             left = right
#             curr_sum = neededTime[right]
#             max_val = neededTime[right]
#             flag = False
#         else:
#             curr_sum += neededTime[right]
#             max_val = max(max_val, neededTime[right])
#             flag = True
#         right += 1
#     if flag:
#         total += curr_sum - max_val
#     return total


## Greedy Approach
def minCost(colors: str, neededTime: List[int]) -> int:
    curr = 0
    total = 0
    for i in range(len(colors)):
        if i > 0 and colors[i] != colors[i - 1]:
            curr = 0

        total += min(curr, neededTime[i])
        curr = max(curr, neededTime[i])

    return total
