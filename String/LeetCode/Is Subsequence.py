# 392 Two Pointer | O(N) and O(1)

def isSubsequence(s, t) -> bool:
    index1 = 0
    if s == "":
        return True
    for char in t:
        if s[index1] == char:
            index1 += 1
            if index1 == len(s):
                return True

    return False


str1 = 'axc'
str2 = 'aghbdc'

print(isSubsequence(str1, str2))
