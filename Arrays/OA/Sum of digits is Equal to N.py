# Single Pass | O(N) and O(1)
def checkSum(n, x):
    if n > x:
        return 0
    if n > 27:
        return 1
    if x < 10:
        return 1
    count = 0
    for i in range(n, x+1):
        digit_sum = 0
        num = i
        while num > 0:
            digit_sum += num % 10
            num = num // 10
        if digit_sum == n:
            count += 1
    return count


print(checkSum(10, 20))