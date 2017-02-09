"""
Can you hear me? You went black
Try refreshing page :)

"""
"""
may be the connetion is weak
let me refresh

can you hear m?

tree root

   left right key
"""

"""
x = 5, result = 1
   5
  1 7
  
x = 1, result = None
   5
  1 7

x = 4
looking for node with value 3
    5
  2   7
    4

class Node:
   val -> int
   left -> node or None
   right -> node or None
   
keys are unique

Strategy:
   Search for x in tree:
      If I find x, get largest value smaller than result
      If I don't find x, return resulting value

class Node:
   def __init__(self,val):
      self.val = val
      self.left = None
      self.right = None

"""

def largest_smaller_key(root,x):
   result_node = find_node(root,x-1)
   return result_node.value if result_node is not None else None

def find_node(tree,val):
   node = tree
   prev = None
   while node.val != val:
      if node.val < val:
         if node.right:
            prev = node
            node = node.right
         else:
            break
      elif node.val > val:
         if node.left:
            prev = node
            node = node.left
         else:
            node = prev
            break
   return node
   12       10  11
    10
               log(n)
  4    15
1   6 11  16
       
   jian wang
   stevens
   
   
function findLargestSmallerKey(root, x):
   result = null
   while (root != null):
      if (root.key < x):
         result = root.key
         root = root.right
      else
         root = root.left
   return result
   