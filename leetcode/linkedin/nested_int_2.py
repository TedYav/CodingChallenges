# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger(object):
#    def __init__(self, value=None):
#        """
#        If value is not specified, initializes an empty list.
#        Otherwise initializes a single integer equal to value.
#        """
#
#    def isInteger(self):
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        :rtype bool
#        """
#
#    def add(self, elem):
#        """
#        Set this NestedInteger to hold a nested list and adds a nested integer elem to it.
#        :rtype void
#        """
#
#    def setInteger(self, value):
#        """
#        Set this NestedInteger to hold a single integer equal to value.
#        :rtype void
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

    STRATEGY:
        * Same as previous, use stack with (depth,NestedInteger) placed on it
        * DIFFERENCE: this time, start depth at 0. Each time we encounter a single number, DO NOT ADD IT.
            * Push to second stack with its depth and value
        * Keep track of maximum depth we've encountered.
        * Once we've placed all numbers on second stack along with their depth, multiply them all my max_depth - their_depth and add to sum

"""

def flatten_list(nestedList):
    input_stack = [(0,nestedList)]
    output_stack = []
    max_depth = 0
    while input_stack:
        current_depth,current_list = input_stack.pop()
        for nestedInt in current_list:
            if nestedInt.isInteger():
                output_stack.append((current_depth,nestedInt.getInteger()))
            else:
                input_stack.append((current_depth + 1, nestedInt.getList()))
        if current_depth > max_depth:
            max_depth = current_depth
    max_depth += 1
    return (output_stack,max_depth)

from functools import reduce
def sum_by_depth(sum_stack,max_depth):
    return reduce(lambda s,t: s + ((max_depth - t[0]) * t[1]),sum_stack,0)

class Solution(object):
    def depthSumInverse(self, nestedList):
        """
        :type nestedList: List[NestedInteger]
        :rtype: int
        """
        if not nestedList: return 0
        else:
            sum_stack,max_depth = flatten_list(nestedList)
            return sum_by_depth(sum_stack,max_depth)
