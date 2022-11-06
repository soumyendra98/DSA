# 835, Create image Location arrays and count overlap for all the translations | O(N^2) and O(M1 + M2)
# where M1 and M2 are the respective no of 1's in img1 and img2.
from collections import Counter
from typing import List


def largestOverlap(img1: List[List[int]], img2: List[List[int]]) -> int:
    n = len(img1)
    # def count_overlap(row, col):
    #     curr_count = 0
    #     for i in range(n):
    #         for j in range(n):
    #             if img2[i][j]:
    #                 r = i + row - n + 1
    #                 c = j + col- n + 1
    #                 if -1 < r < n and -1 < c < n and img1[r][c]:
    #                     curr_count += 1
    #     return curr_count

    # total = 0

    # for i in range(2 * n -1):
    #     for j in range(2 * n -1):
    #         temp = count_overlap(i, j)
    #         if temp > total:
    #             total = temp

    ones_img1 = [(i, j) for i in range(n) for j in range(n) if img1[i][j]]
    ones_img2 = [(i, j) for i in range(n) for j in range(n) if img2[i][j]]

    translations = Counter((x1 - x2, y1 - y2) for x1, y1 in ones_img1 for x2, y2 in ones_img2)

    return translations.most_common(1)[0][1] if len(translations) else 0
