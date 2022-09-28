# 72, DP Tabulation with Space Optimization | O(N * M) and O(min(N, M))
# 
def minDistance(word1: str, word2: str) -> int:
    big = word1 if len(word1) > len(word2) else word2
    small = word2 if big == word1 else word1

    dpPrev = [k for k in range(len(small) + 1)]
    dpCurr = [None for _ in range(len(small) + 1)]
    for i in range(1, len(big) + 1):
        if i % 2 == 1:
            curr = dpCurr
            prev = dpPrev
        else:
            curr = dpPrev
            prev = dpCurr
        curr[0] = i
        for j in range(1, len(small) + 1):
            if small[j - 1] == big[i - 1]:
                curr[j] = prev[j - 1]
            else:
                curr[j] = 1 + min(curr[j - 1], prev[j], prev[j - 1])
    return dpPrev[-1] if len(big) % 2 == 0 else dpCurr[-1]
