"""

CROSSWORD:
Strategy:
    Place 1 word, recurse on smaller board.
    When no words remaining in word list, return board

Optimizations:
    * Use stack instead of recursion
    * Precalculate word start positions and lengths
    * Precalculate word lengths

"""

def solve():
    board = []
    for _ in range(10):
        board.append(list(input().strip()))
    words = input().strip().split(';')
    solve_board(board,words)

def solve_board(board,words):
    word_positions = find_word_positions(board)
    word_map = generate_word_map(words)
    stack = [[]]
    while len(stack[-1]) < len(word_positions):
        current_words = stack.pop()
        possible_words = get_possible_words(current_words,word_positions,board,word_map)
        for word in possible_words:
            stack.append([w for w in current_words] + [word])
    solution = stack[-1]
    write_position(solution,word_positions,board)
    print_board(board)
    
def get_possible_words(current_words,word_positions,board,word_map):
    next_position = word_positions[len(current_words)]
    next_length = next_position[2]
    
    # VERY WASTEFUL doing this in here
    # okay for small coding challenge like this
    # better refactor and move to solve_board function
    # so we can control when and how the board is updated
    write_position(current_words,word_positions,board)
    
    possible_words = word_map[next_length].difference(set(current_words))
    possible_words = filter(lambda word: word_can_be_placed(word,next_position,board),possible_words)
    possible_words = list(possible_words)
    
    erase_position(current_words,word_positions,board)
    return possible_words

def word_can_be_placed(word,position,board):
    row,col,length,direction = position
    row_delta,col_delta = get_deltas(direction)
    for char,c_row,c_col in zip(word,\
        (row + i*row_delta for i in range(length)),\
        (col + i*col_delta for i in range(length))):
            if board[c_row][c_col] != '.' and board[c_row][c_col] != char:
                return False
    return True
    
def generate_word_map(words):
    word_map = {}
    for word in words:
        if len(word) not in word_map:
            # optimization: use indices instead of whole word
            # doesn't matter for 10x10 board
            word_map[len(word)] = set([word])
        else:
            word_map[len(word)].add(word)
    return word_map

def write_position(current_words,word_positions,board):
    for word,position in zip(current_words,word_positions):
        write_word(word,position,board)

def erase_position(current_words,word_positions,board):
    for word,position in zip(current_words,word_positions):
        erase_word(position,board)
        
def write_word(word,position,board):
    row,col,length,direction = position
    row_delta,col_delta = get_deltas(direction)
    for char in word:
        board[row][col] = char
        row += row_delta
        col += col_delta

def print_board(board):
    print('\n'.join(map(lambda row: ''.join(row),board)))
        
def find_word_positions(board):
    word_positions = []
    for i in range(len(board)):
        for j in range(len(board[0])):
            while word_starts_at(board,i,j):
                word_positions.append(precalculate_word(board,i,j))
                erase_word(word_positions[-1],board)
    return word_positions

# if this were production code, I'd avoid these side effects
def precalculate_word(board,i,j):
    length = 1
    if i + 1 < len(board) and board[i+1][j] == '-':
        direction = 'DOWN'
    else:
        direction = 'ACROSS'

    row_delta,col_delta = get_deltas(direction)
    
    row,col = i,j
    while row + row_delta < len(board) \
        and col + col_delta < len(board[0]) \
        and board[row+row_delta][col+col_delta] != '+':
            row += row_delta
            col += col_delta
            length += 1
    
    return (i,j,length,direction)

def get_deltas(direction):
    if direction == 'DOWN':
        return (1,0)
    else:
        return (0,1)

def erase_word(word_position,board):
    row,col,length,direction = word_position
    row_delta,col_delta = get_deltas(direction)
    for i in range(length):
        board[row][col] = '.'
        row += row_delta
        col += col_delta

def word_starts_at(board,i,j):
    if board[i][j] == '-': return True
    elif board[i][j] == '.':
        if i + 1 < len(board) and board[i+1][j] == '-': return True
        elif j + 1 < len(board[0]) and board[i][j+1] == '-': return True
    return False    
            
solve()
