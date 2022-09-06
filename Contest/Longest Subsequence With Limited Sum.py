from typing import List


def answerQueries(nums: List[int], queries: List[int]) -> List[int]:
    output = []
    nums.sort()
    sum = 0
    q = 0
    for i in range(len(nums)):
        sum += nums[i]
        if queries[q] == sum:
            q += 1
            output.append(i+1)
        elif queries[q] < sum:
            output.append(i)
            q+=1
    while q < len(queries):
        output.append(i+1)
        q += 1
    return output


arr = [4, 5, 2, 1]
query = [3, 10, 21]
print(answerQueries(arr, query))
