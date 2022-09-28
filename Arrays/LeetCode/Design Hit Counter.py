# 362, Using Hashmap to store the freq | O(H * G) and O(H) where H is the number of hits and G is no of getHits
class HitCounter:

    def __init__(self):
        self.counter = {}

    def hit(self, timestamp: int) -> None:
        if timestamp in self.counter:
            self.counter[timestamp] += 1
        else:
            self.counter[timestamp] = 1

    def getHits(self, timestamp: int) -> int:
        if timestamp > 300:
            min_val = timestamp - 300 + 1
        else:
            min_val = 1
        total_count = 0
        for time, hits in self.counter.items():
            if min_val <= time <= timestamp:
                total_count += hits
        print(self.counter)
        return total_count


# Your HitCounter object will be instantiated and called as such:
# obj = HitCounter()
# obj.hit(timestamp)
# param_2 = obj.getHits(timestamp)
