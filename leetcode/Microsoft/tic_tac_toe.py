"""

TicTacToe:
Observations:
* on an NxN board, NOBODY can win until the 2N - 1st move has been made. Thus we do not need to check for winners until this point
* we only ever need to check if the current piece has won the game, because previous pieces will have been checked on previous turns
    * corollary: we can short circuit this check as soon as a blocking piece or empty square is found

Optimization:
* once a piece becomes blocked from winning in a given direction, we can mark it, and all pieces in that direction, as unable to win in that direction. If N is large, this could save many checks (i.e. if N == 1000 and p1 has 999 pieces in a row and then there's 1 piece from p2). Not implemented here.

Strategy:
board initialized to 0, we set 1 or 2 to mark whether p1 or p2 has left piece
move:
    * place piece on board (we can assume move is proper)
    * if current_move # >= 2N - 1, check for winner from current piece
        * check to left and to right, return false if any numbers do not equal current player #
        * check above and below
        * if square_number is equal to (i,i) or (i,n-i-1): check diagonal up left, down right, up right, down left as well
        * check function can be parametrized using delta row, delta col rather than having different ones for each direction
        * if move results in winner, return current player #
    * if current_move # == N^2, return 0 --> tie, no winner

"""

class TicTacToe(object):

    def __init__(self, n):
        """
        Initialize your data structure here.
        :type n: int
        """
        self.__board = [[0] * n for j in range(n)]
        self.__max_moves = n*n
        # players can move out of order
        self.__first_win_move = n
        self.__move_num = 0

    def move(self, row, col, player):
        """
        Player {player} makes a move at ({row}, {col}).
        @param row The row of the board.
        @param col The column of the board.
        @param player The player, can be either 1 or 2.
        @return The current winning condition, can be either:
                0: No one wins.
                1: Player 1 wins.
                2: Player 2 wins.
        :type row: int
        :type col: int
        :type player: int
        :rtype: int
        """
        if self.__move_num < self.__max_moves:
            self.__board[row][col] = player
            self.__move_num += 1
            if self.__move_num >= self.__first_win_move and self.__check_for_winner(player,row,col):
                return player
        return 0

    def __check_for_winner(self,player,row,col):
        won = False
        if self.__has_won(player,row,col,1,0) \
            or self.__has_won(player,row,col,0,1) \
            or (row == col and self.__has_won(player,row,col,1,1)) \
            or (row == len(self.__board) - col - 1 and self.__has_won(player,row,col,-1,1)):
                won = True
        return won
    
    def __has_won(self,player,row,col,row_delta,col_delta):
        return self.__verify_win(player,row,col,row_delta,col_delta) and self.__verify_win(player,row,col,row_delta * -1, col_delta * -1)
    
    def __verify_win(self,player,row,col,row_delta,col_delta):
        current_cell = [row + row_delta,col + col_delta]
        while self.__valid_cell(current_cell):
            if self.__board[current_cell[0]][current_cell[1]] != player:
                return False
            current_cell[0] += row_delta
            current_cell[1] += col_delta
        return True
    
    def __valid_cell(self,cell):
        return cell[0] >= 0 and cell[1] >= 0 and cell[0] < len(self.__board) and cell[1] < len(self.__board)

# Your TicTacToe object will be instantiated and called as such:
# obj = TicTacToe(n)
# param_1 = obj.move(row,col,player)
