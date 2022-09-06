from typing import List


def getPoints(position: int) -> int:
    if position == 1:
        return 10
    elif position == 2:
        return 6
    elif position == 3:
        return 4
    elif position == 4:
        return 3
    elif position == 5:
        return 2
    elif position == 6:
        return 1
    else:
        return 0

def racingResults(database: List[List[int]]) -> List[int]:
    point_table = {}
    for val in database:
        if val[1] in point_table:
            point_table[val[1]][0] += getPoints(val[2])
            point_table[val[1]][1] += 1
        else:
            point_table[val[1]] = [getPoints(val[2]), 1]

    max_val = max(point_table.values())[0]
    keys = [key for key, val in point_table.items() if val[0] == max_val]
    winner = [0, max_val]
    curr_min = 101
    for key in keys:
        if point_table[key][1] < curr_min:
            winner[0] = key
            curr_min = point_table[key][1]

    return winner


arr = [
    [2001, 1001, 3],
    [2001, 1002, 2],
    # [2001, 1003, 1],
    [2002, 1001, 2],
    [2002, 1002, 3],
    [2002, 1003, 1],
]

print(racingResults(arr))