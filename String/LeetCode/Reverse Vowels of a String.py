# 345, Two pointers | O(N) and O(1)

def reverseVowels(s: str) -> str:
    n = len(s)
    s = list(s)
    left = 0
    right = n - 1
    vowels = set(['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'])
    while left < right:
        if s[left] not in vowels:
            left += 1
        if s[right] not in vowels:
            right -= 1
        if s[left] in vowels and s[right] in vowels:
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1

    return "".join(s)
