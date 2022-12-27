# 246, Simulation | O(N) and O(1)
def isStrobogrammatic(num: str) -> bool:
    strobogrammatic = {'6': '9', '9': '6', '8': '8', '1': '1', '0': '0'}
    l, r = 0, len(num) - 1
    while l <= r:
        if num[l] not in strobogrammatic or num[r] not in strobogrammatic:
            return False
        if strobogrammatic[num[l]] != num[r] and strobogrammatic[num[r]] != num[l]:
            return False
        l += 1
        r -= 1
    return True
