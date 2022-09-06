# 70, Fibonacci Series | O(N) and O(1)
def climbStairs(n: int) -> int:
    if n == 1:
        return 1
    prev = 0
    curr = 1
    for i in range(1, n):
        next_val = curr + prev
        prev = curr
        curr = next_val
    return curr + prev