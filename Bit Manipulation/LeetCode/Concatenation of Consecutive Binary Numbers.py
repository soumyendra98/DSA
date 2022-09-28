# Bitwise Manipulation | O(N) and O(1)
# Check if the length of the binary has increased --> 3, 4 [11, 100]
# Add the new bits to the end << and | and modulo the result
def concatenatedBinary(n: int) -> int:
    length_binary = 0
    output = 0

    for i in range(1, n + 1):
        if i & i - 1 == 0:
            length_binary += 1
        output = ((output << length_binary) | i) % (10 ** 9 + 7)
    return output
