# 1093, Statistics from a Large Sample | O(N) and O(1)
from typing import List


def sampleStats(count: List[int]) -> List[float]:
    # min_val = 256
    # max_val = 0
    # curr_sum = 0
    # total = 0
    # max_frequency = 0
    # mode = 0
    # for i in range(len(count)):
    #     curr_sum += (i * count[i])
    #     total += count[i]
    #     if count[i] > max_frequency:
    #         mode = i
    #         max_frequency = count[i]
    #     if count[i] != 0:
    #         min_val = min(min_val, i)
    #         max_val = max(max_val, i)
    #
    # mean = curr_sum / total
    # mid = 0
    # found = False
    # mid_sum = total // 2
    # median = 0
    # prev = 0
    #
    # for i in range(len(count)):
    #     mid += count[i]
    #     if mid >= mid_sum:
    #         if mid >= mid_sum + 1:
    #             median = i
    #             break
    #         if found:
    #             median = (prev + i) / 2
    #             break
    #         found = True
    #         prev = i
    #         mid_sum += 1
    #
    # return [min_val, max_val, mean, median, mode]
    output = [0] * 5
    output[0] = 256
    curr_sum = 0
    total = 0
    max_frequency = 0
    median1 = -1
    median2 = -1
    for index, val in enumerate(count):
        if val != 0:
            output[1] = max(index, output[1])
            output[0] = min(index, output[0])
        curr_sum += val * index
        total += val
        if val > max_frequency:
            output[4] = index
            max_frequency = val

    output[2] = curr_sum / total

    running_sum = 0

    for index, val in enumerate(count):
        running_sum += val
        if running_sum >= total // 2 and median1 == -1:
            median1 = index
        if running_sum >= total // 2 + 1:
            median2 = index
            break
    print(median1, median2, total)
    if total % 2 == 0:
        output[3] = (median1 + median2) / 2
    else:
        output[3] = median2
    return output


arr = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,1,0,0,0,0,3,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
print(sampleStats(arr))
