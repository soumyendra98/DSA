# 263, Factorization | O(1) and O(1)
def isUgly(n: int) -> bool:
    allowed = [2, 3, 5]
    if n < 1:
        return False
    for factor in allowed:
        while n % factor == 0:
            n = n // factor

    if n != 1:
        return False

    return True
