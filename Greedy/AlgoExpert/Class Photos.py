# Greedy Optimization | O(NlogN) and O(1)
def classPhotos(redShirtHeights, blueShirtHeights):
    # Write your code here.
    redShirtHeights.sort()
    blueShirtHeights.sort()
    val = True if redShirtHeights[0] > blueShirtHeights[0] else False
    for idx in range(len(redShirtHeights)):
        if redShirtHeights[idx] == blueShirtHeights[idx]:
            return False
        elif (redShirtHeights[idx] - blueShirtHeights[idx] > 0) != val:
            return False
    return True
