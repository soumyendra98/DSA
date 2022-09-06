# 278 Binary Search | O(logN) and O(1)
def isBadVersion(version: int) -> bool:
    return True


def firstBadVersion(n: int) -> int:
    low = 0
    high = n

    while low <= high:
        curr = (low + high) // 2

        if isBadVersion(curr):
            break
        else:
            low = curr + 1

    if not isBadVersion(curr):
        return -1

    high = curr - 1
    while low <= high:
        curr = (low + high) // 2
        if isBadVersion(curr):
            high = curr - 1
            if not isBadVersion(curr - 1):
                return curr
        else:
            low = curr + 1

    return high + 1