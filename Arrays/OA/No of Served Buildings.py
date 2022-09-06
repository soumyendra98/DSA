from typing import List


def countBuildingsServed(build_count: List[int], router_location: List[int], router_range: List[int]) -> int:
    router_info = [0] * len(build_count)
    for i in range(len(router_location)):
        router_info[max(0, router_location[i] - router_range[i] - 1)] += 1

        if 0 <= router_location[i] + router_range[i] < len(build_count):
            router_info[router_location[i] + router_range[i]] -= 1
    total = 0
    curr = 0
    for i in range(len(build_count)):
        curr += router_info[i]
        print(curr, build_count[i])
        if build_count[i] <= curr:
            total += 1
    return total


building = [1, 2, 1, 2, 2]
router_l = [3, 1]
router_r = [1, 2]

print(countBuildingsServed(building, router_l, router_r))
