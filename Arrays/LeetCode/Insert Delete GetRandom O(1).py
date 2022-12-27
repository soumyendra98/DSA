# 380, HashMap | O(1) and O(N)
from random import choice


class RandomizedSet:

    def __init__(self):
        self.map = {}
        self.values = []

    def insert(self, val: int) -> bool:
        if val not in self.map:
            self.map[val] = len(self.values)
            self.values.append(val)
            return True
        return False

    def remove(self, val: int) -> bool:
        if val in self.map:
            if len(self.values) > 1:
                temp_idx, temp_val = self.map[val], self.values[-1]
                self.values[-1], self.values[temp_idx] = val, temp_val
                self.map[temp_val] = temp_idx
            del self.map[val]
            self.values.pop()
            return True
        return False

    def getRandom(self) -> int:
        return choice(self.values)


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()