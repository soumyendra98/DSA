# Single pass and Join | O(N) and O(1)
def reverseWordsInString(string):
    # Write your code here.
    output = []
    temp = ''
    for i in string:
        if i == ' ':
            output = [temp] + output
            temp = ''
        else:
            temp += i

    output = [temp] + output

    return " ".join(output)


str1 = 'AlgoExpert is the best!'

print(reverseWordsInString(str1))
