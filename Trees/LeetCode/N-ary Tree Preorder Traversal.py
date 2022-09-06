# 589, Recursion | O(N) and O(N)
from typing import List


def preorder(self, root: 'Node') -> List[int]:
    output = []
    if root:
        output.append(root.val)
        for i in root.children:
            output += self.preorder(i)
    return output

