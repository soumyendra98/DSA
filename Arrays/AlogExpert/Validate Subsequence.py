# Brute Force | O(N) and O(1)
def isValidSubsequence(array, sequence):
    # Write your code here.
    seqIndex = 0
    for i in array:
        if sequence[seqIndex] == i and seqIndex < len(sequence):
            seqIndex += 1
        if seqIndex == len(sequence):
            return True
    return False


arr = [5, 1, 22, 25, 6, -1, 8, 10]

seq = [1, 6, -1, 10]

print(isValidSubsequence(arr, seq))
