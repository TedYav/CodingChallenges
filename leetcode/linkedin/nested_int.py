# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger(object):
#    def isInteger(self):
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        :rtype bool
#        """
#
#    def getInteger(self):
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        :rtype int
#        """
#
#    def getList(self):
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        :rtype List[NestedInteger]
#        """


"""

    NESTED INTEGER:
        Recursion or Stack --> I'm basically reducing a sum with initial value 0.
        Adding sum of all lists, + their depth.
        
    SOLUTION:
        Use a Stack:
            Push initial list onto stack as tuple (1,nestedList)
            For each element in stack, pop it
            Iterate through it. If it's a list, push it to stack at (depth+1,nestedList)
            If it's int, add to total * depth.
            Return sum.

"""

class Solution(object):
    def depthSum(self, nestedList):
        """
        :type nestedList: List[NestedInteger]
        :rtype: int
        """
        stack = [(1,nestedList)]
        total = 0
        while stack:
            currentDepth, currentList = stack.pop()
            for nestedInt in currentList:
                if nestedInt.isInteger():
                    total += nestedInt.getInteger() * currentDepth
                else:
                    stack.append((currentDepth + 1, nestedInt.getList()))
        return total
