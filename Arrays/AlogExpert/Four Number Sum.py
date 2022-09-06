# Sorting and Two Pointer | O(N^2)[Average Case], O(N^3)[Worst Case] and O(N)
from itertools import combinations


# Permutation Using Recursion
def permutePairs(array, index, length):
    if index == length - 1:
        print(array[index-1:index+1])
    else:
        for i in range(index, length):
            array[index], array[i] = array[i], array[index]
            permutePairs(array, index + 1, length)
            array[index], array[i] = array[i], array[index]


def fourNumberSum(array, targetSum):
    # Write your code here.

    # Making pairs using enumerate
    # pairs = [(i, j) for i, val in enumerate(array) for j in range(i + 1, len(array))]

    # Making pairs using itertools.combinations()
    # pairs = list(combinations(array, 2))
    array.sort()
    all_sums = {}
    output = []
    for i in range(1, len(array) - 1):
        for j in range(i+1, len(array)):
            current_sum = array[i] + array[j]
            if targetSum - current_sum in all_sums:
                for pair in all_sums[targetSum - current_sum]:
                    output.append([*pair, array[i], array[j]])

        for k in range(0, i):
            current_sum = array[i] + array[k]
            if current_sum not in all_sums:
                all_sums[current_sum] = [[array[k], array[i]]]
            else:
                all_sums[current_sum].append([array[k], array[i]])
    return output


arr = [7, 6, 4, -1, 1, 2]

print(fourNumberSum(arr, 16))
