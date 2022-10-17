# Simple Greedy Optimization | O(NlogN) and O(1)
def minimumWaitingTime(queries):
    # Write your code here.
    total = 0
    queries.sort()
    curr = 0
    for idx in range(len(queries) - 1):
        val = queries[idx]
        curr += val
        total += curr
    return total

