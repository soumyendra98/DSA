# Number Theory/Algebra | O(NlogN) and O(1)
def nonConstructableChange(coins):
    # Write your code here.
    coins.sort()
    total_sum = 0
    for coin in coins:
        if coin > (total_sum + 1):
            return total_sum + 1
        else:
            total_sum += coin
    return total_sum + 1


arr = [5, 7, 1, 1, 2, 3, 22]

print(nonConstructableChange(arr))
