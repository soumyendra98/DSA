# 2225, HashMap | O(N * log(N)) and O(N)
from typing import List
from collections import Counter


def findWinners(matches: List[List[int]]) -> List[List[int]]:
    win = set()
    lose = Counter()

    for w, l in matches:
        win.add(w)
        lose[l] += 1

    no_loss = [key for key in win if key not in lose]
    one_loss = [key for key, val in lose.items() if val == 1]

    no_loss.sort()
    one_loss.sort()
    return [no_loss, one_loss]
