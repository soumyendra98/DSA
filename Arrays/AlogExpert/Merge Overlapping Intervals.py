# Sorting | O(NlogN) and O(N)
def mergeOverlappingIntervals(intervals):
    # Write your code here.
    output = []
    intervals = sorted(intervals, key=lambda row: row[0])
    currentInterval = intervals[0]
    output.append(currentInterval)
    for interval in intervals:
        start, end = currentInterval
        nextStart, nextEnd = interval

        if end >= nextStart:
            currentInterval[1] = max(nextEnd, end)
        else:
            currentInterval = interval
            output.append(currentInterval)

    return output


arr = [
    [1, 2],
    [3, 5],
    [4, 7],
    [6, 8],
    [9, 10]
]
print(mergeOverlappingIntervals(arr))
