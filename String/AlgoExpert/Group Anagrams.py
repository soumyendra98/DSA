#
def groupAnagrams(words):
    # Write your code here.
    words_dict = {}
    for word in words:
        temp = "".join(sorted(word))
        if temp in words_dict:
            words_dict[temp].append(word)
        else:
            words_dict[temp] = [word]

    return list(words_dict.values())


arr1 = ["yo", "act", "flop", "tac", "foo", "cat", "oy", "olfp"]

print(groupAnagrams(arr1))