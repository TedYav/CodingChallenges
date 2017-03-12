"""

    Abbreviation:
        Let's define function f(i,j) = 1 if first i characters of A can produce first j characters of B, 0 if not
        We want to see if f(len(a),len(b)) == 1.
        
        f(i,j) = 0 if j > i
        f(0,0) = 1
        f(i+1,j+1) = 1 if a[i+1].lower() == b[j+1].lower() and f(i,j) == 1
        f(i+1,j) = 1 if f(i,j) == 1 and a[i+1] is not capitalized
        f(i+1,j) = 1 if f(i,j) == 1 and a[i+1] == b[j] (and a[i] is capitalized) and f(i,j-1) == 1
        
        abcabcabcC ==> f(10,3) == 1
        ABC
   
        abcabcabcD ==> f(10,3) == 0
        ABCD
        
        abCabcabcC ==> f(10,3) == 0
        ABC
        
        aBcabcabcC ==> f(10,3) == 1 because f(9,2) == 1
        ABC
"""

def solve():
    q = int(input().strip())
    for _ in range(q):
        A = input().strip() # daBcd
        B = input().strip() # ABC
        print("YES" if can_abbreviate(A,B) else "NO")

def can_abbreviate(A,B):
    if len(A) < len(B): return False
    memo = [[0 if j > 0 else 1 for j in range(len(B)+1)] for i in range(len(A)+1)]
    for j in range(1,len(memo[0])):
        for i in range(1,len(memo)):
            if i < j: continue
            memo[i][j] = update_memo(memo,A,B,i,j)
    return memo[len(A)][len(B)] == 1

def update_memo(memo,A,B,i,j):
    if memo[i-1][j] == 1 and A[i-1].islower(): return 1
    elif memo[i-1][j-1] == 1 and A[i-1].lower() == B[j-1].lower(): return 1
    else: return 0
    
solve()
