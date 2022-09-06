# Finding all possible combinaitons one digit at a time | O(4^N) and O(4^N)
def phoneNumberMnemonics(phoneNumber):
    # Write your code here.
    output = []
    helper(0, phoneNumber, output)
    return output


def helper(idx, string, mnemonics):
    if idx == len(string):
        mnemonics.append(string)
    else:
        digit = string[idx]
        for val in digit_map[int(digit)]:
            string = string[:idx] + val + string[idx + 1:]
            helper(idx + 1, string, mnemonics)
            string = string[:idx] + digit + string[idx + 1:]


digit_map = {
    0:["0"],
    1:["1"],
    2:["a", "b", "c"],
    3:["d", "e", "f"],
    4:["g", "h", "i"],
    5:["j", "k", "l"],
    6:["m", "n", "o"],
    7:["p", "q", "r", "s"],
    8:["t", "u", "v"],
    9:["w", "x", "y", "z"],
}