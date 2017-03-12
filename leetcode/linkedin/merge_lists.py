# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

def duplicate_list(lst):
    result = ListNode(lst.val)
    tail = result
    node = lst.next
    while node is not None:
        tail.next = ListNode(node.val)
        tail = tail.next
        node = node.next
    return result
        
class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if l1 is None and l2 is None: return None
        elif l2 is None: return duplicate_list(l1)
        elif l1 is None: return duplicate_list(l2)
        else:
            node1,node2 = l1,l2
            if l1.val < l2.val:
                result = ListNode(l1.val)
                node1 = node1.next
            else:
                result = ListNode(l2.val)
                node2 = node2.next
            tail = result
            while node1 is not None and node2 is not None:
                if node1.val < node2.val:
                    tail.next = ListNode(node1.val)
                    node1 = node1.next
                else:
                    tail.next = ListNode(node2.val)
                    node2 = node2.next
                tail = tail.next
            if node1 is None:
                tail.next = duplicate_list(node2)
            else:
                tail.next = duplicate_list(node1)
            return result
            
        result = ListNode()
