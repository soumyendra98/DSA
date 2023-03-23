# 787, Bellman Ford with K + 1 edges | O(E * (K + 1)) and O(V)
from typing import List


def findCheapestPrice(n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
    prices = [float('inf')] * n
    prices[src] = 0

    for i in range(k + 1):
        curr_prices = prices[:]
        for f, t, w in flights:
            if prices[f] + w < curr_prices[t]:
                curr_prices[t] = prices[f] + w
        if curr_prices == prices:
            break

        prices = curr_prices

    return prices[dst] if prices[dst] != float('inf') else -1
