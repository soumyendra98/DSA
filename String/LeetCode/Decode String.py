# Stack and Recursion | O(N) and O(M) M is the length of the output string 
def decodeString(s: str) -> str:
    idx = 0
    output = ''
    while idx < len(s):
        if not s[idx].isdigit():
            output += s[idx]
        else:
            start = s.index('[', idx)
            num = int(s[idx: start])
            curr = start + 1
            count = 1
            temp = ''

            while True:
                if s[curr] == ']':
                    count -= 1
                elif s[curr] == '[':
                    count += 1
                if count != 0:
                    temp += s[curr]
                else:
                    break
                curr += 1

            temp = decodeString(temp)
            temp = num * temp
            output += temp
            idx = curr
        idx += 1

    return output


str1 = "3[a]2[bc]d"
print(decodeString(str1))
