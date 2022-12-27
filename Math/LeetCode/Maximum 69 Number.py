# 1323, Replace the first 6 from left | O(N) and O(1)
def maximum69Number(num: int) -> int:
    num = list(str(num))
    for idx in range(len(num)):
        if num[idx] == '6':
            num[idx] = '9'
            break

    return int("".join(num))
