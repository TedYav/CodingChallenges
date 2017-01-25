from math import sqrt, ceil, floor
s = input().strip()
rows,cols = floor(sqrt(len(s))), floor(sqrt(len(s)))
if rows*cols < len(s): cols += 1
if rows*cols < len(s): rows += 1
s = s + ''.join([' ' for i in range(rows*cols - len(s))])
matrix = [[c for c in s[i*cols:(i+1)*cols]] for i in range(rows)]
print(' '.join([''.join([matrix[row][col] for row in range(rows)]).strip() for col in range(cols)]))