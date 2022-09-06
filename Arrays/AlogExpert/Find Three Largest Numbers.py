# Maximum of given numbers | O(N) and O(1)
import sys


def findThreeLargestNumbers(array):
    # Write your code here.
    output = [ -sys.maxsize - 1] * 3

    for val in array:
        if output[2] < val:
            output = [output[1], output[2], val]
        elif output[1] < val:
            output = [output[1], val, output[2]]
        elif output[0] < val:
            output[0] = val

    return output