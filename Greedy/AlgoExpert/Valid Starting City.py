# Greedy Optimization | O(N) and O(1)
def validStartingCity(distances, fuel, mpg):
    # Write your code here.
    gain = 0
    output = 0
    min_val = float('inf')
    for idx, val in enumerate(distances):
        if gain < min_val:
            min_val = gain
            output = idx
        gain += fuel[idx] * mpg - val

    return output
