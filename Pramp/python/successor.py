"""

         n:
         val = x
left = node   right = node

Cases:
1. Simple -> right node is a leaf. return n.right
2. Right child, not a leaf -> go to right node, then go left as far as possible

3. No right children -> find first parent for which given node is on the left
4. Largest node in tree -> follow case 2 until node doesn't have a parent. Then return None

"""

def successor(node):
   if node is None: return None
   
   if node.right is not None:
      node = node.right
      while node.left is not None:
         node = node.left
      return node
   
   else:
      prev = node
      node = node.parent
      while node is not None:
         if node.left is not None and node.left == prev: break
         prev = node
         node = node.parent
      return node
         