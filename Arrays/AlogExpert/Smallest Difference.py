# Sorting and Two Pointer | O(Nlog(N) + Mlog(M)) and O(1)
def smallestDifference(arrayOne, arrayTwo):
    # Write your code here.
    outputArray = [0] * 2
    arrayOne.sort()
    arrayTwo.sort()
    indexOne = 0
    indexTwo = 0
    diff = abs(arrayOne[indexOne] - arrayTwo[indexTwo])

    while indexOne < len(arrayOne) and indexTwo < len(arrayTwo):
        currentDiff = abs(arrayOne[indexOne] - arrayTwo[indexTwo])

        if diff > currentDiff:
            diff = currentDiff
            outputArray[0], outputArray[1] = arrayOne[indexOne], arrayTwo[indexTwo]

        if diff == 0:
            break
        if arrayOne[indexOne] < arrayTwo[indexTwo]:
            indexOne += 1
        else:
            indexTwo += 1

    return outputArray


arrayOne = [-1, 5, 10, 20, 28, 3]
arrayTwo = [26, 134, 135, 15, 17]

print(smallestDifference(arrayOne,arrayTwo))