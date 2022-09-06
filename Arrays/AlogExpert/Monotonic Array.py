# Algebra | O(N) and O(1)
def isMonotonic(array):
    # Write your code here.
    if len(array) < 2:
        return True

    i = 0
    isState = False
    while not isState and i < len(array) - 1:
        if array[i] != array[i + 1]:
            state = array[i] < array[i + 1]
            isState = True
        i += 1

    while i < len(array) - 1:
        if array[i] == array[i + 1]:
            i += 1
            continue
        if state != (array[i] < array[i + 1]):
            return False
        i += 1
    return True


arr = [-1, -1, -2, -3, -4, -5, -5, -5, -6, -7, -8, -8, -9, -10, -11]
print(isMonotonic(arr))
