# Counter and Search | O(N) and O(1)
from collections import Counter


def firstNonRepeatingCharacter(string):
    # Write your code here.
    s_count = Counter(string)

    for idx,s in enumerate(string):
        if s_count[s] == 1:
            return idx
    return -1

