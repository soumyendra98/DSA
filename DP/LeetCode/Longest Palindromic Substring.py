# 5, Expand in both directions | O(N ^ 2) and O(N)

def longestPalindrome(s: str) -> str:
    n = len(s)
    output = ""

    def check(left, right):
        while left >= 0 and right < n and s[right] == s[left]:
            left -= 1
            right += 1
        return s[left + 1: right]

    for i in range(n):
        val = check(i, i)
        if len(val) > len(output):
            output = val

        val = check(i, i + 1)
        if len(val) > len(output):
            output = val

    return output
