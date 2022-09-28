# Using DP |O(N) and O(1)
def maxSubsetSumNoAdjacent(array):
    # Write your code here.
    if len(array) == 0:
        return 0
    if len(array) == 1:
        return array[0]

    max_2 = array[0]
    max_1 = max(array[1], array[0])

    for idx in range(2, len(array)):
        curr = max(max_2 + array[idx], max_1)
        max_2 = max_1
        max_1 = curr

    return max_2
