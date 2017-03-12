"""

    Count Battleships:
    
    EASY SOLUTION (non constant memory) (not guaranteed one pass):
        Iterate over board.
        When encounter new battleship, call subroutine that will recursively explore it
        Mark this battleship as visited
    ISSUE:
        Stack uses non-constant memory
        Modifies input board, or requires duplicating the board
    
    O(1) One Pass Solution:
        Use Logic: if we go left to right, top to bottom, we only count a battleship the **first** time we encounter it.
        When we encounter a ship square, we check above and left. If there is a ship square in either, we don't count this square.
        This will result in Maximum O(n) operations (because we may do 2 additional checks on some squares). And we have constant memory --> just the count of ships.

"""


def is_battleship(board,row,col):
    return board[row][col] == 'X'
    
def already_counted(board,row,col):
    conditions = []
    if row - 1 >= 0: conditions.append(is_battleship(board,row-1,col))
    if col - 1 >= 0: conditions.append(is_battleship(board,row,col-1))
    return any(conditions)

class Solution(object):
    def countBattleships(self, board):
        """
        :type board: List[List[str]]
        :rtype: int
        """
        battleship_count = 0
        rows,cols = len(board),len(board[0])
        for row in range(rows):
            for col in range(cols):
                if is_battleship(board,row,col) and not already_counted(board,row,col):
                    battleship_count += 1
        return battleship_count



tc_num = 0
sut = Solution()
def test(func,args,expected):
        global tc_num, sut
        assert func(*args) == expected, "TC%d FAIL" % tc_num
        print("TC%d PASS" % tc_num)
        tc_num += 1

def test_count_battleships():
    global sut
    f = sut.countBattleships
    print("Testing Count Battleships")
    test(f,[[['.']]],0)                                         # PASS
    test(f,[[['X']]],1)                                         # PASS

def test_is_battleship():
    f = is_battleship
    print("Testing Is Battleship")
    test(f,[ [['.']], 0, 0], False)     # PASS
    test(f,[ [['X']], 0, 0], True)      # PASS

def test_already_counted():
    f = already_counted
    print("Testing Already Counted")
    test(f,[ [['X']], 0, 0], False)             # PASS
    test(f,[ [['.','X']], 0, 1], False)         # PASS
    test(f,[ [['X','X']], 0, 1], True)          # PASS
    test(f,[ [['X','.'],['X','.']],1,0], True)  # PASS
    test(f,[ [['X','.'],['.','X']],1,1], False) # PASS
    test(f,[ [['.','X'],['X','.']],1,0], False) # PASS

def run_tests():
    test_is_battleship()
    test_already_counted()
    test_count_battleships()

# run_tests()
