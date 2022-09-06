# Simple Recursion | O(N) and O(N)


def productSum(array, mul=1):
    # Write your code here.
    sum1 = 0

    for val in array:
        if type(val) is list:
            sum1 += productSum(val, mul + 1)
        else:
            sum1 += val
    return sum1 * mul

