# 1908, Backtracking and Game of Nim | O(N ^ 2) and O(1)
from typing import List
from functools import cache

def nimGame(piles: List[int]) -> bool:
    # piles.sort()

    # @cache
    # def dfs(state):
    #     if sum(state) == 0:
    #         return False

    #     for i in range(len(state)):
    #         if state[i] > 0:
    #             next_state = list(state)
    #             for j in range(1, state[i] + 1):
    #                 next_state[i] -= j
    #                 if not dfs(tuple(next_state)):
    #                     return True
    #                 next_state[i] += j
    #     return False
    # return dfs(tuple(piles))
    nim_sum = 0
    for p in piles:
        nim_sum ^= p
    return nim_sum
