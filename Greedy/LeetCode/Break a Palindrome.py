# 1328, Simple Greedy Approach | O(N) and O(1)
def breakPalindrome(palindrome: str) -> str:
    if len(palindrome) == 1:
        return ""

    for idx in range(len(palindrome) // 2):
        val = palindrome[idx]
        if val != 'a':
            palindrome = palindrome[:idx] + 'a' + palindrome[idx + 1:]
            return palindrome

    palindrome = palindrome[:len(palindrome) - 1] + 'b'
    return palindrome
