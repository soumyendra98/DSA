# Similar to Largest Increasing Subsequence | O(N ^ 2) and O(N)

def maxSumIncreasingSubsequence(array):
    # Write your code here.
    dp = [0 for _ in range(len(array))]
    seq = [None for _ in range(len(array))]
    max_val = -1
    max_idx = 0
    for i in range(len(array)):
        dp[i] = array[i]
        for j in range(i):
            if array[j] < array[i] and dp[i] < array[i] + dp[j]:
                dp[i] = array[i] + dp[j]
                seq[i] = j
        if max_val < dp[i]:
            max_val = dp[i]
            max_idx = i

    output = [array[max_idx] if max_val > -1 else -1]

    while seq[max_idx] is not None:
        output.append(array[seq[max_idx]])
        max_idx = seq[max_idx]

    return [max_val, output[::-1]]

