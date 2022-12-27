# 2478, 0/1 Knapsack } O(N * K) and O(N)

def beautifulPartitions(s: str, k: int, minLength: int) -> int:
    prime = {'2', '3', '5', '7'}
    n = len(s)

    if s[-1] in prime or s[0] not in prime or k * minLength > n:
        return 0

    prev = [1 for _ in range(n - minLength)]

    for i in range(1, k):

        curr = [0 for _ in range(n - minLength)]
        for j in range(i * minLength - 1, n - minLength):
            curr[j] = curr[j - 1]
            if s[j] not in prime and s[j + 1] in prime:
                curr[j] += prev[j - minLength]
            curr[j] %= (10 ** 9 + 7)
        prev = curr
    return prev[-1]
