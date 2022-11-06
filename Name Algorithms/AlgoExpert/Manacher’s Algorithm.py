# Implementation of Manacher's Algorithm.
#

def longestPalindrome(s: str) -> str:
    if len(s) == 1:
        return s
    n = 2 * len(s) + 1
    radius = [0] * n
    radius[1] = 1
    max_lps_length = 0
    max_lps_center = 0
    center = 1
    right = 2
    left = 0

    for i in range(2, n):
        left = 2 * center - i
        diff = right - i
        radius[i] = 0
        if diff > 0:
            radius[i] = min(radius[left], diff)
        while (i + radius[i]) < n - 1 and (i - radius[i]) > 0:
            if (i + radius[i] + 1) % 2 == 0:
                radius[i] += 1
            elif s[(i + radius[i] + 1) // 2] == s[(i - radius[i] - 1) // 2]:
                radius[i] += 1
            else:
                break

        if radius[i] > max_lps_length:
            max_lps_length = radius[i]
            max_lps_center = i

        if i + radius[i] > right:
            center = i
            right = i + radius[i]

    start = (max_lps_center - max_lps_length) // 2
    end = start + max_lps_length - 1
    return s[start: end + 1]