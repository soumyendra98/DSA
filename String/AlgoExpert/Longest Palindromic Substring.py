# Starting with the center | O(N^2) and O(N)
def longestPalindromicSubstring(string):
    if len(string) == 1:
        return string
    output = ''
    for i in range(1, len(string)):
        l1, r1 = i - 1, i
        l2, r2 = i - 1, i + 1
        while l1 >= 0 and r1 < len(string):
            if string[l1] != string[r1]:
                flag1 = True
                break
            l1 -= 1
            r1 += 1

        if len(string[l1 + 1: r1]) > len(output):
            output = string[l1 + 1: r1]

        while l2 >= 0 and r2 < len(string):
            if string[l2] != string[r2]:
                flag2 = True
                break
            l2 -= 1
            r2 += 1
        if len(string[l2 + 1: r2]) > len(output):
            output = string[l2 + 1: r2]

    return output


string1 = 'aca'

print(longestPalindromicSubstring(string1))
