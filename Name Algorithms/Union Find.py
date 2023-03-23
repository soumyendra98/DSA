# Union find with path compression and rank | O(N * log(N)) and O(N)
class UF:
    def __init__(self, n):
        self.uf = {i: i for i in range(n + 1)}
        self.rank = {i: 1 for i in range(n + 1)}

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
            return True
        return False

