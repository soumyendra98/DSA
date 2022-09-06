# Brute Force | O(N^2) and O(1)
def twoNumberSum1(array, targetSum):
    # Write your code here.
    for i in range(len(array) - 1):
        for j in range(i + 1, len(array)):
            if array[i] + array[j] == targetSum:
                return [array[i], array[j]]
    return []


# O(N) and O(N) approach

# def twoNumberSum2(array, targetSum):
#     # Write your code here.
#     targetNumDict = {}
#     for i in range(0, len(array)):
#         targetNumDict[targetSum - array[i]] = i
#     for i in range(0, len(array)):
#         if array[i] in targetNumDict and targetNumDict[array[i]] != i:
#             return [array[i], targetSum - array[i]]
#     return []

# AlgoExpert Solution
def twoNumberSum2(array, targetSum):
    # Write your code here.
    numDict = {}
    for i in array:
        targetNum = targetSum - i
        if targetNum in numDict:
            return [targetNum, i]
        else:
            numDict[i] = True
    return []


# Binary Search Approach | O(NlogN) and O(1)
def twoNumberSum3(array, targetSum):
    # Write your code here.
    array.sort()
    left = 0
    right = len(array) - 1

    while left < right:
        sum = array[left] + array[right]

        if sum == targetSum:
            return [array[left], array[right]]
        elif sum < targetSum:
            left += 1
        else:
            right -= 1

    return []


arr = [3, 5, -4, 8, 11, 1, -1, 6]

target_sum = 10

print(twoNumberSum3(arr, target_sum))
