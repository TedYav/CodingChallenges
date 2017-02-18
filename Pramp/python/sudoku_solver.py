"""
- look for the first empty square
   - if the board is full, we check for correctness
- look for viable candidates in square
   - if none are found, we return false
- we pick one to fill, and make a recursive call
   - we keep picking until we've tried all of them
   - if none of them work we return false

"""



# TODO: FINISH






"""

   Sudoku Solver:
      Brute Force Way: Just try every combination. SLOW, exponential.
      Better:
         * Identify Missing #'s For Each Board --> create set with 1-9, remove elements as I find them, remaining elements are what I need
            Set([i for i in range(1,10)])
            For element in sub_board:
               if element:
                  set.remove(element)
         * Try every VALID combination -->
            * Try everything for first square, second square, etc

"""

"""

0 1 2
3 4 5
6 7 8

"""

# look up in STL
def copy(obj):
   return copy_of_obj

def get_needed_numbers(position,board_num):
   pass

   """
   
   Create set of 1-9, remove each number found in square
   
   """

def get_next_positions(position, board_num):
   """ Returns Array of Boards Possible from Current Position """
   """ Filling in Sub Board Board_Num """
   needed_numbers = get_needed_numbers(position,board_num)
   available_squares = get_available_squares(position,board_num)
   # available_squares: [(row,col),(row,col),(row,col)]
   # filled_squares: {(row,col):val,(row,col):val}
   valid_square_placements = []
   stack = [(set(needed_numbers),available_squares,{})]
   while stack:
      remaining_nums, available_squares, filled_squares = stack.pop()
      if len(available_squares) == 0:
         valid_square_placements.append(filled_squares)
      else:
         for num in remainin_nums:
            current_square = available_squares[0]
#             if valid_placement()
     """
     
        Create a copy of my filled_squares dict with each number placed
        Check if it's valid
        If it's valid, append this to stack, removing current number from remaining_nums and first entry from available_squares
        
        At the end, call helper function make_positions(position,valid_square_placements)
        Returns array of positions resulting from each square placement
     
     """
      
def make_positions(position,valid_square_placements)
"""

"""

def sudoku_solver(board):
   """ Determines if a Sudoku Board is solvable, returns True / False """
   stack = [(board,0)]
   while(stack):
      position,board_num = stack.pop()
      if board_num == 9:
         return True
      next_positions = get_next_positions(position,board_num) # gives me all possible next positions
      for next_position in next_positions:
         stack.append((next_position,board_num + 1))
      # if we've filled in the entire board, return True
      # if we reach a position and there are no available moves, return False
   return False