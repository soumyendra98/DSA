# Using Sliding Window | O(N) and O(N)
def staircaseTraversal(height, maxSteps):
    # Write your code here.
    steps = [1]
    curr_steps = 0

    for idx in range(1, height + 1):
        start = idx - maxSteps - 1

        if start >= 0:
            curr_steps -= steps[start]

        curr_steps += steps[idx - 1]
        steps.append(curr_steps)

    return steps[height]
