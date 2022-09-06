# Using Hash Table | O(N + M) and O(N)
def generateDocument(characters, document):
    # Write your code here.
    count1 = {}

    for i in characters:
        if i in count1:
            count1[i] += 1
        else:
            count1[i] = 1
    for i in document:
        if i not in count1 or count1[i] - 1 < 0:
            return False
        count1[i] -= 1

    return True


str1 = "aheaolabbhb"
str2 = "hello"

print(generateDocument(str1, str2))
