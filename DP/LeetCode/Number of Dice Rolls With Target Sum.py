# 1155 Bottom Up Approach | O(N * T * K) and O(N * T)

def numRollsToTarget(n: int, k: int, target: int) -> int:
    dp1 = [0] * (target + 1)
    for i in range(1, min(k + 1, target + 1)):
        dp1[i] = 1

    if n == 1:
        return dp1[-1]

    for i in range(1, n):
        dp2 = [0] * (target + 1)
        for j in range(1, target + 1):
            for l in range(max(1, j - k), j):
                dp2[j] += dp1[l]
                dp2[j] = dp2[j] % (10 ** 9 + 7)
        dp1 = dp2

    return dp1[-1]