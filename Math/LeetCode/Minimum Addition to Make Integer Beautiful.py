# 2457, Eat from Right | O(1) and O(1)

def makeIntegerBeautiful(n: int, target: int) -> int:
    def digitSum(num):
        curr_sum = 0
        while num != 0:
            curr_sum += num % 10
            num = num // 10
        return curr_sum

    val = 0
    power = 10
    while digitSum(n) > target:
        curr = power - n % power
        val += curr
        n += curr
        power *= 10
    return val
