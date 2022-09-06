# Using Dictionary and Counter | O(N*L) and O(C)
from collections import Counter


def minimumCharactersForWords(words):
    # Write your code here.
    letter_dict = {}
    output = []
    for word in words:
        word_count = Counter(word)
        for key in word_count.keys():
            if key in letter_dict:
                letter_dict[key] = max(word_count[key], letter_dict[key])
            else:
                letter_dict[key] = word_count[key]

    for key in letter_dict.keys():
        for l in range(letter_dict[key]):
            output.append(key)

    return output

