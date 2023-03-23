# 460, Ordered Dict | O(1) and O(1)
from collections import defaultdict, OrderedDict

class LFUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.frequency = defaultdict(int)
        self.lfu = defaultdict(OrderedDict)
        self.min_freq = 0

    def update(self, key, value):
        freq = self.frequency[key]
        val = self.lfu[freq].pop(key)
        if value is not None:
            val = value
        self.lfu[freq + 1][key] = val
        self.frequency[key] += 1
        if self.min_freq == freq and not self.lfu[freq]:
            self.min_freq += 1
        return val

    def get(self, key: int) -> int:
        if key in self.frequency:
            return self.update(key, None)
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.frequency:
            self.update(key, value)
        else:
            if len(self.frequency) == self.capacity:
                if self.capacity == 0:
                    return
                key_to_remove = self.lfu[self.min_freq].popitem(last=False)[0]
                self.frequency.pop(key_to_remove)

            self.min_freq = 1
            self.frequency[key] += 1
            self.lfu[1][key] = value

# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
