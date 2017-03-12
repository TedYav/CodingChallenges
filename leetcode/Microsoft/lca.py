# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        if p == root or q == root: return root
        else:
            p_pred,q_pred = get_pred_lists(root,p,q)
            return last_common_element(p_pred,q_pred)

def copy_pred(pred_stack):
    pred = []
    for i in range(len(pred_stack)):
        pred.append(pred_stack[i][0])
    return pred
    
def last_common_element(l1,l2):
    lce = None
    for i in range(min(len(l1),len(l2))):
        if l1[i] == l2[i]: lce = l1[i]
        else: break
    return lce

def get_pred_lists(root,p,q):
    stack = [[root,'l']]
    p_pred = None
    q_pred = None
    while stack and (p_pred is None or q_pred is None):
        node,next_move = stack[-1]
        if node == p and p_pred is None: p_pred = copy_pred(stack)
        if node == q and q_pred is None: q_pred = copy_pred(stack)
        
        if next_move == 'l':
            stack[-1][1] = 'r'
            if node.left is not None:
                stack.append([node.left,'l'])
        elif next_move == 'r':
            stack[-1][1] = ''
            if node.right is not None:
                stack.append([node.right,'l'])
        else:
            stack.pop()
    return (p_pred,q_pred)
    
