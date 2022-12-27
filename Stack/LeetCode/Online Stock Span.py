# 901, Monotonic Stack | O(1) amortized and O(N)

class StockSpanner:

    def __init__(self):
        self.prices = []
        self.idx = 0

    def next(self, price: int) -> int:
        if not self.prices:
            self.prices.append((self.idx, price))
            self.idx += 1
            return 1

        while self.prices and self.prices[-1][1] <= price:
            self.prices.pop()

        top = self.prices[-1][0] if self.prices else -1

        val = self.idx - top

        self.prices.append((self.idx, price))
        self.idx += 1

        return val

    # Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)
