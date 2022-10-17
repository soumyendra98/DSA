# 680, Two Pointer | O(N) and O(1)

def validPalindrome(s: str) -> bool:
    l, r = 0, len(s) - 1
    while l <= r:
        if s[l] != s[r]:
            sl, sr = s[l + 1: r + 1], s[l:r]
            return sl == sl[::-1] or sr == sr[::-1]
        l += 1
        r -= 1
    return True
