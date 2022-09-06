# Left and Right Running Products (Two Pointer)| O(N) and O(N)
def arrayOfProducts(array):
    # Write your code here.
    output = [1] * len(array)
    leftRunningProduct = 1
    rightRunningProduct = 1

    for index in range(len(array)):
        output[index] = leftRunningProduct
        leftRunningProduct *= array[index]

    for index in reversed(range(len(array))):
        output[index] *= rightRunningProduct
        rightRunningProduct *= array[index]

    return output


arr = [5, 1, 4, 2]
print(arrayOfProducts(arr))
