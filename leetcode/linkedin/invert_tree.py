"""

    FLIP BINARY TREE:
    
    Given a binary tree {1,2,3,4,5},
        1
       / \
      2   3
     / \
    4   5
       / \
      6   7
    return the root of the binary tree [4,5,2,#,#,3,1].
        4
      /  \
     5    2
    / \  / \
        3   1  
       

    STRATEGY:
    * Recursive function InvertTree:
        * Go all the way to the left, pushing nodes onto stack.
        * Last node encountered becomes new root
        * Recurse upwards on stack
            * Each node popped becomes right child of previous node
            * Call Invert Tree for right child, append result as left child of previous node
    * Return root

"""


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

"""
    Given a binary tree {1,2,3,4,5},
        1
       / \
      2   3
     / \
    4   5
       / \
      6   7
    return the root of the binary tree [4,5,2,#,#,3,1].
        4
      /  \
     5    2
    / \  / \
        3   1  
"""

def invertTree(root):
    """
    :type root: TreeNode
    :rtype: TreeNode
    """
    if root is None: return None
    
    stack = [root]
    node = root
    while node.left:
        stack.append(node.left)
        node = node.left
    new_root = stack.pop()
    
    node = new_root
    while stack:
        node.right = stack.pop()
        node.left = invertTree(node.right.right)
        node.right.right = None
        node.right.left = None
        node = node.right
    
    return new_root

class Solution(object):
    def upsideDownBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        
        return invertTree(root)
        
