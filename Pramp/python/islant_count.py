"""
0  1  0  2  0
0  0  2  *  2
3  0  0  2  0
0  5  #  0  0
4  0  5  0  6

Strategy:
   * Go through row by row
   * Explore each island, change to -1
   * Increase island count the first time each one is encountered
   
   m x n matrix.
   O(m*n)

   EXTENSION: Island Groups (connected by -1) and Average Per Group
            USE STACK instead of recursion

"""

def island_count(matrix):
   island_count = 0
   for row in range(len(matrix)):
      for col in range(len(row)):
         if matrix[row][col] == 1:
            island_count += 1
            explore(matrix,row,col)
   return island_count

def explore(matrix,row,col):
   if row < 0 or row >= len(matrix) or col < 0 or col >= len(matrix[0]):
      return
   elif matrix[row][col] != 1:
      return
   else:
      matrix[row][col] = -1
      explore(matrix,row+1,col)
      explore(matrix,row-1,col)
      explore(matrix,row,col+1)
      explore(matrix,row,col-1)