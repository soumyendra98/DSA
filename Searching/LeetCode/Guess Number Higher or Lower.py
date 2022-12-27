# 374, Binary search | O(log(N)) and O(1)
def guess(n): return 0


def guessNumber(self, n: int) -> int:
    l = 1
    r = n

    while l < r:
        mid = (l + r) // 2
        if guess(mid) == 1:
            l = mid + 1
        elif guess(mid) == -1:
            r = mid - 1
        else:
            return mid
    return (l + r) // 2
