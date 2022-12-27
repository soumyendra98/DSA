# 7, Reverse a number | O(1) and O(1)
def reverse(x: int) -> int:
    isNegative = x * -1 > 0
    if isNegative:
        x *= -1

    rev = 0

    while x != 0:
        rev *= 10
        rev += x % 10
        x = x // 10
    if rev > 2 ** 31:
        return 0
    return -rev if isNegative else rev
