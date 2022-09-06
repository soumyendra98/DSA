# Sorting and Algebra | O(N^2) and O(N)
def threeNumberSum(array, targetSum):
    # Write your code here.
    array.sort()
    target_array = []
    for i in range(len(array) - 2):
        left = i + 1
        right = len(array) - 1
        while left < right:
            currentSum = array[i] + array[left] + array[right]
            if currentSum == targetSum:
                target_array.append([array[i], array[left], array[right]])
                left += 1
                right -= 1
            elif currentSum < targetSum:
                left += 1
            else:
                right -= 1
    return target_array


arr = [1, 2, 3]
targetsum = 6
print(threeNumberSum(arr, targetsum))
