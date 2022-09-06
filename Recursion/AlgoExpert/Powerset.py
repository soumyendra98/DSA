# Recursion | O(N*2^N) and O(N*2^N)
# Iterative
def powerset(array):
    # Write your code here.
    if len(array) == 0:
        return [[]]

    output = [[]]

    for val in array:
        for idx in range(len(output)):
            curr = output[idx]
            output.append(curr + [val])

    return output


# Recursive solution
# def powerset(array, idx=None):
#     # Write your code here.
#     if idx is None:
#         idx = len(array) - 1
#     if idx < 0:
#         return [[]]
#     val = array[idx]
#     output = powerset(array, idx - 1)
#
#     for i in range(len(output)):
#         curr = output[i]
#         output.append(curr + [val])
#
#     return output