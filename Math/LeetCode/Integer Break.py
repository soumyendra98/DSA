# 343, Maximize (x ^ ( n/ x)) | O(1) and O(1)

def integerBreak(n: int) -> int:
    if n < 4:
        return n - 1

    rem = n % 3
    div = n // 3
    prod = 3 ** div
    if rem == 1:
        return prod // 3 * 4
    elif rem == 2:
        return prod * 2

    return prod
