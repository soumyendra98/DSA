# 12, Simple Math | O(1) and O(1)

def intToRoman(num: int) -> str:
    symbol_map = {
        1: 'I',
        4: 'IV',
        5: 'V',
        9: 'IX',
        10: 'X',
        40: 'XL',
        50: 'L',
        90: 'XC',
        100: 'C',
        400: 'CD',
        500: 'D',
        900: 'CM',
        1000: 'M',
    }

    def getVal(n, pow):
        roman = ''
        if n <= 3:
            roman += n * symbol_map[pow]
        elif n in (1, 4, 9, 5):
            roman += symbol_map[n * pow]
        elif n <= 8:
            roman += symbol_map[5 * pow] + (n - 5) * symbol_map[pow]
        return roman

    output = ''
    curr_pow = 1

    while num > 0:
        output = getVal(num % 10, curr_pow) + output
        num = num // 10
        curr_pow *= 10

    return output
