# 609, Hashmap | O(M) and O(N) where M is the no of unique file content.
from collections import defaultdict
from typing import List


def findDuplicate(paths: List[str]) -> List[List[str]]:
    content_dict = defaultdict(list)

    for val in paths:
        files = val.split(" ")
        dr = files[0]
        for i in range(1, len(files)):
            name, content = files[i].split("(")[0], files[i].split("(")[1][:-1]
            content_dict[content].append(dr + "/" + name)

    output = []

    for val in content_dict.values():
        if len(val) > 1:
            output.append(val)

    return output

