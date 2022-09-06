# Two Pointer | O(N) and O(1)
def longestPeak(array):
    # Write your code here.
    dec = 0
    inc = 0
    peak = 0
    for index in range(len(array) - 1):
        if array[index] < array[index + 1]:
            if dec != 0:
                dec = 0
                inc = 0
            inc += 1
        elif array[index] > array[index + 1]:
            dec += 1
        else:
            inc = 0
            dec = 0
        print(inc, dec)
        if dec != 0 and inc != 0 and dec + inc + 1> peak:
            peak = dec + inc + 1
    return peak


arr = [5, 4, 3, 2, 1, 2, 1]

print(longestPeak(arr))
