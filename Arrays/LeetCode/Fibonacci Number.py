# 509, Single Pass | O(N) and O(1)

def fib(n: int) -> int:
    if n == 0:
        return 0
    if n == 1:
        return 1
    prev = 0
    curr = 1
    for i in range(2, n):
        next_val = curr + prev
        prev = curr
        curr = next_val
    return curr + prev

