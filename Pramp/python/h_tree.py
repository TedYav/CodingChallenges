"""

   HTree:
      Given: x and y coordinates for center, starting_length = length of first horizontal line
            Depth = number of H's to draw
            
          H   H
            H    Depth 1
          H   H

   Strategy:
      O(4^depth) == running time, have to draw all line segments
   
   Draw_H:
      * Draw line of length starting_length at center coordinates (extending in either direction)
      * Draw vertical lines of length starting_length at end coordinates of center line
      * If depth > 0: recursively call Draw_H at each corner with starting_length / sqrt(2) and new center, depth - 1

"""

from Math import sqrt

class Coord:
   def __init(self,x,y):
      self.x = x
      self.y = y

def draw_line(start,end):
   pass

def get_end_coordinates_of_line(center,length,vertical=False):
   if vertical:
      return [(center.x, center.y - (length/2.0)),(center.x, center.y + (length/2.0))]
   else:
      return [(center.x - (length/2.0), center.y),(center.x + (length/2.0), center.y)]

def draw_h(center,starting_length,depth):
   if depth < 0 or starting_length < 0 or not center: return
   else:
      left,right = get_end_coordinates_of_line(center,length)
      draw_line(left,right)
      
      l_start,l_end = get_end_coordinates_of_line(left,length,vertical=True)
      draw_line(l_start,l_end)
      
      r_start,r_end = get_end_coordinates_of_line(right,length,vertical=True)
      draw_line(r_start,r_end)
      
      if depth > 0:
         new_length = starting_length / sqrt(2)
         new_depth = depth - 1
         draw_h(l_start,new_length,new_depth)
         draw_h(l_end,new_length,new_depth)
         draw_h(r_start,new_length,new_depth)
         draw_h(r_end,new_length,new_depth)

# O(4^(depth+1) - 1)
# Space complexity == O(depth) --> longest path
# T(depth) = 3*O(1) + 4*T(depth-1)
# 4^0 + 4^1 + 4^2 + ... + 4^depth <-- exact running time