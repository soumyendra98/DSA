# Moving along the array one val at a time | O(N*N!) and O(N*N!)
def getPermutations(array):
    # Write your code here.
    if len(array) == 0:
        return []
    output = []
    helper(0, array, output)
    return output


def helper(idx, arr, permutations):
    if idx == len(arr) - 1:
        permutations.append(arr[:])
    else:
        for j in range(idx, len(arr)):
            arr[idx], arr[j] = arr[j], arr[idx]
            helper(idx + 1, arr, permutations)
            arr[idx], arr[j] = arr[j], arr[idx]
