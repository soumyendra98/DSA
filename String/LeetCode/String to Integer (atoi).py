# 8, String Traversal with Conditions | O(N) and O(1)
def myAtoi(s: str) -> int:
    digits = {}
    for i in range(10):
        digits[str(i)] = i

    found = False
    output = 0
    isNegative = False
    sign = False
    for char in s:
        if not found and not sign and char in '+-':
            isNegative = char == '-'
            sign = True
        elif char in digits:
            if not found:
                found = True
            output = output * 10 + digits[char]
        elif found or sign or char != ' ':
            break
    if not isNegative:
        if output > 2 ** 31 - 1:
            output = 2 ** 31 - 1
    else:
        if output > 2 ** 31:
            output = 2 ** 31
    return -output if isNegative else output
