# Greedy Optimization | O(NlogN) and O(1)
def tandemBicycle(redShirtSpeeds, blueShirtSpeeds, fastest):
    # Write your code here.
    total = 0
    if fastest:
        redShirtSpeeds.sort()
        blueShirtSpeeds.sort(reverse=True)
    else:
        redShirtSpeeds.sort()
        blueShirtSpeeds.sort()

    for idx in range(len(redShirtSpeeds)):
        total += max(redShirtSpeeds[idx], blueShirtSpeeds[idx])

    return total
