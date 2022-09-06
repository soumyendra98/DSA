# Two  Pointer | O(N) and O(N)
def sortedSquaredArray(array):
    # Write your code here.
    left = 0
    right = len(array) - 1
    output = [0] * len(array)
    index = len(array) - 1 
    while left <= right:
        if abs(array[left]) < abs(array[right]):
            output[index] = array[right] * array[right]
            print(right)
            right -= 1
        else:
            output[index] = array[left] * array[left]
            left += 1
        index -= 1
    return output


arr = [1, 2, 3, 5, 6, 8, 9]
print(sortedSquaredArray(arr))