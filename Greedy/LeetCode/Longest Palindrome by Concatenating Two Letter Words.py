# Greedy approach to the given conditions | O(N) and O(K) where k is the number of unique words
from typing import List
from collections import Counter


def longestPalindrome(words: List[str]) -> int:
    word_count = Counter(words)
    max_len = 0
    flag = True
    for word in set(words):
        rev_word = word[-1::-1]
        if word != rev_word and rev_word in word_count:
            max_len += 2 * min(word_count[word], word_count[rev_word])
        elif word == rev_word:
            if word_count[word] % 2 == 0:
                max_len += 2 * word_count[word]
            else:
                if flag:
                    max_len += 2 * word_count[word]
                    flag = False
                else:
                    max_len += 2 * (word_count[word] - 1)

    return max_len