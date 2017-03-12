"""

    SOLUTIONS:
        Brute Force: try placing at each square. O(n^2m^2) Slow.
        Better: for all cells, calculate number to left, above, right, left. Can iterate from top left to bottom right, then bottom right to top left. Then pick cell with largest sum.
            O(nm) --> can't realistically do better because we have to examine every cell.
            
            Space Complexity: O(nm) --> for each cell, we store 4 numbers.
            
            Optimizations: pick cell with largest sum during return trip. Problem: makes code more confusing. We will ignore here and take a runtime penalty. (If we time out, will add this case)

            Also, could avoid EnemyCounts class and use different type of storage (array with indices)
            This code has TLE error on leetcode, but works fine on local machine so I'm accepting it.
            I care more about good software design than super flasy clever runtime right now.

"""

class EnemyCounts(object):
    def __init__(self):
        self.left = 0
        self.right = 0
        self.above = 0
        self.below = 0
    
    def total(self):
        return self.left + self.right + self.above + self.below
        
    def __getitem__(self,key):
        if key == 'left': return self.left
        elif key == 'right': return self.right
        elif key == 'above': return self.above
        elif key == 'below': return self.below
        else: raise IndexError()
    
    def __setitem__(self,key,value):
        if key == 'left': self.left = value
        elif key == 'right': self.right = value
        elif key == 'above': self.above = value
        elif key == 'below': self.below = value
        else: raise IndexError()

def is_wall(cell): return 1 if cell == 'W' else 0
def is_enemy(cell): return 1 if cell == 'E' else 0
def is_empty(cell): return 1 if cell == '0' else 0

def calculate_counts(grid,rows,cols,enemy_counts,reverse=False):
    # in production code, I'd have separate function to calculate these
    row_delta = -1 if reverse else 1
    col_delta = -1 if reverse else 1
    row_target = 'below' if reverse else 'above'
    col_target = 'right' if reverse else 'left'
    row_range = range(rows-1,-1,-1) if reverse else range(rows)
    col_range = range(cols-1,-1,-1) if reverse else range(cols)
    row_in_range = (lambda row: row < rows-1) if reverse else (lambda row: row > 0)
    col_in_range = (lambda col: col < cols-1) if reverse else (lambda col: col > 0)
    
    for row in row_range:
        for col in col_range:
            if row_in_range(row) and not(is_wall(grid[row - row_delta][col])):
                enemy_counts[row][col][row_target] = enemy_counts[row-row_delta][col][row_target] + is_enemy(grid[row-row_delta][col])
            if col_in_range(col) and not(is_wall(grid[row][col - col_delta])):
                enemy_counts[row][col][col_target] = enemy_counts[row][col-col_delta][col_target] + is_enemy(grid[row][col-col_delta])

def max_enemy_count(enemy_counts,grid,rows,cols):
    max_count = 0
    for row in range(rows):
        for col in range(cols):
            if is_empty(grid[row][col]) and enemy_counts[row][col].total() > max_count:
                max_count = enemy_counts[row][col].total()
    return max_count
    
class Solution(object):
    def maxKilledEnemies(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        # could factor out to another function as well --> validate
        if grid is None: return 0
        
        rows = len(grid)
        if rows == 0: return 0
        
        cols = len(grid[0])
        if cols == 0: return 0
        
        enemy_counts = [[EnemyCounts() for i in range(cols)] for j in range(rows)]
        calculate_counts(grid,rows,cols,enemy_counts,reverse=False)
        calculate_counts(grid,rows,cols,enemy_counts,reverse=True)
        return max_enemy_count(enemy_counts,grid,rows,cols)
