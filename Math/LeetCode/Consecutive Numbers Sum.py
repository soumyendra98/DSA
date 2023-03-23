# 829, N = x + (x + 1) .... + (x + k) --> (N - (k * (k - 1) / 2)) / k = x | O(N ^ 0.5) and O(1)
def consecutiveNumbersSum(n: int) -> int:
    val, ans = 1, 0

    while n > val * (val - 1) // 2:
        if (n - (val * (val - 1) // 2)) % val == 0:
            print(val)
            ans += 1
        val += 1
    return ans
