# 926, Flip 0's before one or 1's before 0 | O(N) and O(1)
def minFlipsMonoIncr(s: str) -> int:
    ones = ans = 0
    for char in s:
        if char == '0':
            ans = min(ans + 1, ones)
        else:
            ones += 1
    return ans
