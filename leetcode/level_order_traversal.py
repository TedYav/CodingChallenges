"""

    Level Order from Bottom Traversal:
        Strategy:
            Do in-order traversal, but add nodes to hash table indexed by depth.
            Return list of nodes in depth order.

"""


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None



import Queue
class Solution(object):
    def levelOrderBottom(self,root):
        traversal = []
        if root:
            stack = [(0,root)]
            while stack:
                depth, node = stack.pop()
                if depth == len(traversal): traversal.append([])
                traversal[depth].append(node.val)
                if node.right: stack.append((depth+1,node.right))
                if node.left: stack.append((depth+1,node.left))
        return traversal[::-1]


# SLOW
"""
def levelOrderBottom(self, root):
        if root is None: return []
        traversal = []
        node_queue = Queue.Queue()
        node_queue.put((0,root))
        
        while not node_queue.empty():
            depth, node = node_queue.get()
            
            if depth >= len(traversal):
                traversal.append([])
            
            traversal[depth].append(node.val)
                
            if node.left is not None:
                node_queue.put((depth+1,node.left))
            if node.right is not None:
                node_queue.put((depth+1,node.right))
        
        return traversal[::-1]

"""