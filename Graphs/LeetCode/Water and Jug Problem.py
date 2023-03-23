# 365, Bezout's Lemma (GCD) | O(1) and O(1)
# Bezout's Lemma states that if x and y are nonzero integers and g = gcd(x,y),
# then there exist integers a and b such that ax+by=g.
# In other words, there exists a linear combination of x and y equal to g.
# Furthermore, g is the smallest positive integer that can be expressed in this form,
# i.e. g = min{ax+by | a, b in Z, ax+by > 0}.
def canMeasureWater(jug1Capacity: int, jug2Capacity: int, targetCapacity: int) -> bool:
    def gcd(a, b):
        if a == b:
            return a
        elif a > b:
            return gcd(a - b, b)
        else:
            return gcd(a, b - a)

    fac = gcd(jug1Capacity, jug2Capacity)

    return targetCapacity % fac == 0 if targetCapacity <= jug2Capacity + jug1Capacity else False
