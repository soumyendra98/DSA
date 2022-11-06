# 38, Simple string manipulation | O(N * L) and O(L) where L is the length of the final output

def countAndSay(n: int) -> str:
    output = '1'
    curr = '1'
    for i in range(1, n):
        count = 0
        prev = ''
        output = ''
        for s in curr:
            if s == prev:
                count += 1
            else:
                if count != 0:
                    output += str(count) + prev
                prev = s

                count = 1
        output += str(count) + prev
        curr = output
    return output
