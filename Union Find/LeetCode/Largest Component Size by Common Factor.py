# 952, Prime Factorization and UF | O(N * sqrt(M)) and O(N * Log(M))
from collections import defaultdict
from typing import List


def largestComponentSize(nums: List[int]) -> int:
    def primeFactors(n):
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return primeFactors(n // i) | {i}
        return {n}

    uf = UF(len(nums))
    primes = defaultdict(set)

    for i, num in enumerate(nums):
        for factor in primeFactors(num):
            primes[factor].add(i)

    for _, values in primes.items():
        values = list(values)
        for i in range(1, len(values)):
            uf.union(values[i], values[i - 1])

    size = defaultdict(int)
    for i in range(len(nums)):
        size[uf.find(i)] += 1

    return max(size.values())


# Union find with path compression and rank | O(N * log(N)) and O(N)
class UF:
    def __init__(self, n):
        self.uf = {i: i for i in range(n)}
        self.rank = {i: 1 for i in range(n)}

    def find(self, x):
        if x != self.uf[x]:
            self.uf[x] = self.find(self.uf[x])
        return self.uf[x]

    def union(self, x, y):
        rx = self.find(x)
        ry = self.find(y)

        if rx != ry:
            if self.rank[rx] < self.rank[ry]:
                self.uf[rx] = ry
                self.rank[ry] += self.rank[rx]
            else:
                self.uf[ry] = rx
                self.rank[rx] += self.rank[ry]


