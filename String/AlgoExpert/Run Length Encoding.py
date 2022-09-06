# Single Pass | O(N) and O(N)
def runLengthEncoding(string):
    # Write your code here.
    prev = string[0]
    count = 1
    output = ''
    i = 1
    while i < len(string):
        if string[i] == prev:
            if count < 9:
                count += 1
            else:
                output += str(count) + string[i]
                count = 1
        else:
            output += str(count) + prev
            count = 1
        prev = string[i]
        i += 1
    output += str(count) + string[i - 1]
    return output


str1 = 'AAABBCCC'

print(runLengthEncoding(str1))