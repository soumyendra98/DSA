# Kadane's Algorithm | O(N) and O(1)
def kadanesAlgorithm(array):
    # Write your code here.
    max_till_now = float('-inf')
    curr_sum = 0
    for val in array:
        curr_sum += val
        max_till_now = max(max_till_now, curr_sum)
        if curr_sum < 0:
            curr_sum = 0
    return max_till_now
