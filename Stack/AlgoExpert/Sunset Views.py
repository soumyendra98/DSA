# Using Kadane's | O(N) and O(N)
def sunsetViews(buildings, direction):
    # Write your code here.
    max_val = -1
    output = []

    if direction == 'EAST':
        for idx in reversed(range(len(buildings))):
            if buildings[idx] > max_val:
                output.append(idx)
            max_val = max(max_val, buildings[idx])
        output.reverse()
        return output

    else:
        for idx in range(len(buildings)):
            if buildings[idx] > max_val:
                output.append(idx)
            max_val = max(max_val, buildings[idx])
        return output

    return output
