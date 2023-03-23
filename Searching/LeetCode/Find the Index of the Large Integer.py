# 1533, Binary Search | O(Log(N)) and O(1)

# class ArrayReader(object):
# 	 # Compares the sum of arr[l..r] with the sum of arr[x..y]
# 	 # return 1 if sum(arr[l..r]) > sum(arr[x..y])
# 	 # return 0 if sum(arr[l..r]) == sum(arr[x..y])
# 	 # return -1 if sum(arr[l..r]) < sum(arr[x..y])
#    def compareSub(self, l: int, r: int, x: int, y: int) -> int:
#
# 	 # Returns the length of the array
#    def length(self) -> int:
#


def getIndex(reader: 'ArrayReader') -> int:
    left, right = 0, reader.length() - 1
    while left < right:
        mid = (left + right) // 2
        even_size = (right - left + 1) % 2 == 0
        if even_size:
            val = reader.compareSub(left, mid, mid + 1, right)
        else:
            val = reader.compareSub(left, mid, mid, right)

        if val == -1:
            if even_size:
                left = mid + 1
            else:
                left = mid
        elif val == 1:
            right = mid
        else:
            return mid

    return left
