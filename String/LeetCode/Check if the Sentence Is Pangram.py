# 1832, Using Set | O(N) and O(1)
def checkIfPangram(sentence: str) -> bool:
    char_set = set()

    for char in sentence:
        char_set.add(char)
        if len(char_set) == 26:
            return True

    return False
