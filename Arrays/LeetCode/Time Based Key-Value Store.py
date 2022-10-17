# 981 Using Dictionary | O(1) and O(N)

class TimeMap:

    def __init__(self):
        self.dict = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.dict[(timestamp, key)] = value

    def get(self, key: str, timestamp: int) -> str:
        for i in reversed(range(1, timestamp + 1)):
            if (i, key) in self.dict:
                return self.dict[(i, key)]
        return ""


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)
