# 948, Simple Greedy approach |O(N) and O(1)
from typing import List


def bagOfTokensScore(tokens: List[int], power: int) -> int:
    curr_power = power
    tokens.sort()
    left = 0
    right = len(tokens) - 1
    points = 0
    max_points = 0

    while left <= right:
        if curr_power >= tokens[left]:
            print(curr_power, left)
            curr_power -= tokens[left]
            points += 1
            max_points = max(points, max_points)
            left += 1
        elif points > 0:
            curr_power += tokens[right]
            points -= 1
            right -= 1
        else:
            break

    return max_points

