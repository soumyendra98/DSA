# 227 Single Pass |O(N) and O(1)
def calculate(s: str) -> int:
    output = 0
    last = 0
    char_set = {'+', '-', '*', '/'}
    num = 0
    operation = '+'
    for idx in range(len(s)):
        if s[idx].isnumeric():
            num = num * 10 + int(s[idx])

        if s[idx] in char_set or idx == len(s) - 1:
            if operation == '+':
                output += last
                last = num
            elif operation == '-':
                output += last
                last = -num
            elif operation == "*":
                last *= num
            else:
                last = int(last / num)
            operation = s[idx]
            num = 0

    output += last
    return output


