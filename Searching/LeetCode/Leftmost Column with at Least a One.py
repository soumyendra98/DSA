# 1428, Using Binary Search Left | O(R * Log(C)) and O(1)

def leftMostColumnWithOne(binaryMatrix: 'BinaryMatrix') -> int:
    rows, cols = binaryMatrix.dimensions()

    def binarySearch(row):
        l, h = 0, cols - 1

        while l < h:
            mid = (l + h) // 2

            if binaryMatrix.get(row, mid) == 0:
                l = mid + 1
            else:
                h = mid

        return l if binaryMatrix.get(row, l) == 1 else rows

    min_val = float('inf')

    for i in range(rows):
        min_val = min(min_val, binarySearch(i))

    return min_val if min_val != rows else -1
