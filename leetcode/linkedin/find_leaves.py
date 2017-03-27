"""

Find Leaves in Tree:

Strategy:
    1. Determine maximum depth of tree (may be unnecessary)
        OPTIMIZATION: DO NOT DO THIS AND JUST APPEND
    2. Create array of len(max_depth + 1)
    3. Calculate removal order:
        - removal order of node = max(removal order of children) + 1
        - if no children, removal order of children = -1, thus it goes in element 0 of output array, etc
        - use stack to add children recursively in this manner :)

"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

def order_nodes_for_removal(node,removal_order):
    if node is None:
        return -1
    else:
        removal_round = max(order_nodes_for_removal(node.left,removal_order),order_nodes_for_removal(node.right,removal_order)) + 1
        if removal_round + 1 > len(removal_order): removal_order.append([])
        removal_order[removal_round].append(node.val)
        return removal_round

class Solution(object):
    def findLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        removal_order = []
        order_nodes_for_removal(root,removal_order)
        return removal_order
