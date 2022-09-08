# Simple Multiplication of two numbers | O(N*M) and O(N * M + 1)
def multiply(num1: str, num2: str) -> str:
    output = 0
    po2 = 1
    for idx1, val1 in enumerate(reversed(num1)):
        po = 1
        carry = 0
        curr_sum = 0
        for idx2, val2 in enumerate(reversed(num2)):
            curr_sum += carry * po
            prod = int(val1) * int(val2)
            carry = prod // 10
            curr_sum += prod % 10 * po
            po *= 10
        output += (curr_sum + carry * po) * po2
        po2 *= 10

    return str(output)