# HashMap | O(N) and O(1)
def firstDuplicateValue(array):
    # Write your code here.
    elementDict = {}

    for i in array:
        if i in elementDict:
            return i
        else:
            elementDict[i] = True
    return -1


arr = [2, 1, 5, 2, 3, 3, 4]
print(firstDuplicateValue(arr))
