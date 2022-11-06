# Tabulation | O(N * M) and O(N * M)

def numberOfWaysToTraverseGraph(width, height):
    # Write your code here.
    dp = [[0 for _ in range(width)] for _ in range(height)]

    for i in range(width):
        dp[0][i] = 1

    for i in range(height):
        dp[i][0] = 1

    for i in range(1, height):
        for j in range(1, width):
            dp[i][j] = dp[i - 1][j] + dp[i][j - 1]

    return dp[height - 1][width - 1]
#     return factorial(height + width - 2) // (factorial(height - 1) * factorial(width - 1))

# def factorial(num):
#     val = 1
#     for i in range(1, num + 1):
#         val *= i
#     return val
