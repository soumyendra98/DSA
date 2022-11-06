# Using Max Heap and Counter() | O(NLogN) and O(N)
from typing import List
from collections import Counter
from heapq import heappush, heappop, heapify


class MaxHeap:
    def __init__(self):
        self.queue = []
        heapify(self.queue)

    def push(self, count, word):
        heappush(self.queue, (-count, word))

    def pop(self):
        return heappop(self.queue)


def topKFrequent(words: List[str], k: int) -> List[str]:
    word_count = Counter(words)
    p_q = MaxHeap()

    for word, count in word_count.items():
        p_q.push(count, word)

    return [p_q.pop()[1] for key in range(k)]


# Using Sorted and heap
# def topKFrequent(self, words: List[str], k: int) -> List[str]:
#     word_map = Counter(words)
#     # sorted_words = sorted(word_map.items(), key=lambda x: (-x[1], x[0]))
#     # return [val for val, _ in sorted_words[:k]]
#     max_heap = []
#
#     for key, val in word_map.items():
#         heappush(max_heap, (-val, key))
#
#     return [heappop(max_heap)[1] for _ in range(k)]
