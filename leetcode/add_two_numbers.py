# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

"""

    Strategy:
        Add digit by digit
        Carry over one digit if needed after each addition.
    
    Can add one list to another -- when list ends and carry is 0, then return it if it's the longer list.
    If it's the shorter list that we've been adding to, then once everything is added, attach it to the longer list. (Don't have to create a new list and iterate).
    O(min(m,n)) where m=len(list1), n=len(list2)

"""

def make_list(num):
    head = ListNode(num%10)
    node = head
    num //= 10
    while num > 0:
        node.next = ListNode(num%10)
        node = node.next
        num //= 10
    return head

def val(node):
    pow = 0
    result = 0
    while node is not None:
        result += (10**pow) * node.val
        pow += 1
    return result
    
def list_eq(node,arr):
    for element in arr:
        if node is None or node.val != element: return False
        node = node.next
    return True if node is None else False ## could do retur node is None
        

def test_add_two_numbers():
    solution = Solution()
    add = solution.addTwoNumbers
    
    # single digit lists, single digit results
    list1 = make_list(4)
    list2 = make_list(4)
    assert list_eq(add(list1,list2),[8]), "TC1"         # PASS
    
    list1 = make_list(4)
    list2 = make_list(0)
    assert list_eq(add(list1,list2),[4]), "TC2"         # PASS
    
    # single digit lists, two digit results
    list1 = make_list(6)
    list2 = make_list(8)
    assert list_eq(add(list1,list2),[4,1]), "TC3"       # PASS
    
    # first number longer than second number
    list1 = make_list(100)
    list2 = make_list(2)
    assert list_eq(add(list1,list2),[2,0,1]), "TC4"     # PASS
    
    # first number longer than second number, carry
    list1 = make_list(105)
    list2 = make_list(9)
    assert list_eq(add(list1,list2),[4,1,1]), "TC5"     # PASS
    
    # first number longer than second, string of 9's
    list1 = make_list(999)
    list2 = make_list(1)
    assert list_eq(add(list1,list2),[0,0,0,1]), "TC6"   # PASS
    
    # second number larger than first, no carry
    list1 = make_list(2)
    list2 = make_list(100)
    assert list_eq(add(list1,list2),[2,0,1]), "TC7"     # PASS
    
    # second number larger than first, carry
    list1 = make_list(9)
    list2 = make_list(105)
    assert list_eq(add(list1,list2),[4,1,1]), "TC8"     # PASS
    
    # second number longer than second, string of 9's
    list1 = make_list(1)
    list2 = make_list(999)
    assert list_eq(add(list1,list2),[0,0,0,1]), "TC9"   # PASS
    
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        
        head = l1
        carry = 0
        while l1 and l2:
            l1.val += l2.val + carry
            carry = 0

            if l1.val >= 10:
                carry = 1
                l1.val %= 10
            
            tail = l1
            l1 = l1.next
            l2 = l2.next
        
        if l2 is not None: # l2 is longer list
            tail.next = l2
            l1 = l2
        
        if carry == 1:
            if l1 is not None:
                l1.val += 1
                while l1 is not None:
                    if l1.val < 10:
                        carry = 0
                        break
                    else:
                        l1.val %= 10
                        tail = l1
                        l1 = l1.next
                        if l1 is not None: l1.val += 1
                    
            if carry == 1:
                tail.next = ListNode(carry)
                tail = tail.next
            
        return head
        
test_add_two_numbers()