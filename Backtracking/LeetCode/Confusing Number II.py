# 1088, DFS | O((N ^ log(5) * log(N)) and (log(N))

def confusingNumberII(n: int) -> int:
    res = 0
    digits = {0: 0, 1: 1, 6: 9, 8: 8, 9: 6}

    def backtrack(number, rotated, unit):
        if number != rotated:
            nonlocal res
            res += 1
        for digit, inv in digits.items():
            if digit == 0 and number == 0:
                continue
            if number * 10 + digit > n:
                break
            backtrack(number * 10 + digit, inv * unit + rotated, unit * 10)

    backtrack(0, 0, 1)
    return res
