# 224, Single Pass Stack | O(N) and O(N)
def calculate(s: str) -> int:
    n = len(s)
    num = 0
    sign = 1
    stack = [0]

    for char in s:
        if char == ' ':
            continue
        elif char.isdigit():
            num = num * 10 + int(char)
        elif char == '-':
            stack[-1] += num * sign
            sign = -1
            num = 0
        elif char == '+':
            stack[-1] += num * sign
            sign = 1
            num = 0
        elif char == '(':
            stack += [sign, 0]
            sign = 1
        elif char == ')':
            stack[-1] += num * sign
            temp_val = stack.pop()
            temp_sign = stack.pop()
            stack[-1] += temp_sign * temp_val
            num = 0
            sign = 1

    stack[-1] += sign * num
    return stack.pop()
