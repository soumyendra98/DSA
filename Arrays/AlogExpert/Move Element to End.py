# Two Pointer | O(N) and O(1)
def moveElementToEnd(array, toMove):
    # Write your code here.
    left = 0
    right = len(array) - 1

    while left < right:
        if array[left] == toMove:
            if array[right] != toMove:
                array[left] = array[right]
                array[right] = toMove
            else:
                right -= 1
                continue
        left += 1
    return array


arr = [2, 1, 2, 2, 2, 3, 4, 2]
element = 2
print(moveElementToEnd(arr, element))
