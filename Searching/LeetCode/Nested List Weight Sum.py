# 339, Simple DFS | O(N) and O(H)

# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
class NestedInteger:
   def __init__(self, value=None):
       """
       If value is not specified, initializes an empty list.
       Otherwise initializes a single integer equal to value.
       """

   def isInteger(self):
       """
       @return True if this NestedInteger holds a single integer, rather than a nested list.
       :rtype bool
       """

   def add(self, elem):
       """
       Set this NestedInteger to hold a nested list and adds a nested integer elem to it.
       :rtype void
       """

   def setInteger(self, value):
       """
       Set this NestedInteger to hold a single integer equal to value.
       :rtype void
       """

   def getInteger(self):
       """
       @return the single integer that this NestedInteger holds, if it holds a single integer
       Return None if this NestedInteger holds a nested list
       :rtype int
       """

   def getList(self):
       """
       @return the nested list that this NestedInteger holds, if it holds a nested list
       Return None if this NestedInteger holds a single integer
       :rtype List[NestedInteger]
       """


def depthSum(nestedList: List[NestedInteger]) -> int:
    def dfs(nested_val, level, d_sum):
        if nested_val.getInteger():
            d_sum += nested_val.getInteger() * level
        for new_val in nested_val.getList():
            d_sum = dfs(new_val, level + 1, d_sum)

        return d_sum

    total = 0
    for val in nestedList:
        total += dfs(val, 1, 0)
    return total
