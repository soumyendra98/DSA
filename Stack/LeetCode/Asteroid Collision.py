# Creating and output stack and treating asteroids as a stack | 0(N) and O(N)
from typing import List


def asteroidCollision(asteroids: List[int]) -> List[int]:
    stack = [asteroids.pop()]

    while len(asteroids) > 0:
        val = asteroids.pop()
        while len(stack) and (val ^ stack[-1]) < 0:
            if stack[-1] < 0:
                curr = stack.pop()
                if abs(curr) > abs(val):
                    val = curr
                elif abs(curr) == abs(val):
                    val = None
                    break
            else:
                break
        if val is not None:
            stack.append(val)

    return stack[::-1]
