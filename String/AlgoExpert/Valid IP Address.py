def validIPAddresses(string):
    # Write your code here.
    output = []
    string_len = len(string)
    for i in range(1, min(string_len, 4)):
        temp = [''] * 4
        temp[0] = string[:i]
        if not isValid(temp[0]):
            continue
        for j in range(1, min(string_len - i, 4)):
            temp[1] = string[i: i + j]
            if not isValid(temp[1]):
                continue
            for k in range(1, min(string_len - i - j, 4)):
                temp[2] = string[i + j: i + j + k]
                if not isValid(temp[2]):
                    continue
                temp[3] = string[i + j + k:]
                if isValid(temp[3]):
                    output.append('.'.join(temp))
    return output


def isValid(string) -> bool:
    if int(string) > 255:
        return False
    return len(string) == len(str(int(string)))


str1 = '1921680'

print(validIPAddresses(str1))
