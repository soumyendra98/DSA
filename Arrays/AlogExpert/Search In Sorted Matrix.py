# Directional Traversal | O(M+N) and O(1)
def searchInSortedMatrix(matrix, target):
    # Write your code here.
    i, j = 0, len(matrix[0]) - 1

    while i < len(matrix) and j >= 0:
        if matrix[i][j] < target:
            i += 1
        elif matrix[i][j] > target:
            j -= 1
        else:
            return [i, j]
    return [-1, -1]



arr = [
    [1, 4, 7, 12, 15, 1000],
    [2, 5, 19, 31, 32, 1001],
    [3, 8, 24, 33, 35, 1002],
    [40, 41, 42, 44, 45, 1003],
    [99, 100, 103, 106, 128, 1004]
  ]

print(searchInSortedMatrix(arr, 4))
