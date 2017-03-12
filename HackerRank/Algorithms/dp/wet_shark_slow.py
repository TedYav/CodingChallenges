"""

Wet Shark:
Observations:
Sum(x_ai + x_bi) = R
Sum(x_ai - x_bi) = S

==>

2*Sum(x_ai) = R + S
2*Sum(x_bi) = R - S

Find all sequences length 1...m with sums R + S and R - S
If R + S != R - S: multiply the numbers of each length and sum mod 10**9 + 7
If R + S == R - S: nCr of each length --> choose two and use combinatorics, mod 10**9 + 7

How to do efficiently?

Any subsequence of k elements that does not equal some number n, in order to possibly equal n we must add x_i
such that n - sum(k) == x_i

If x_i could be NEGATIVE, we'd be in trouble! But they're all positive. So any time a subsequence exceeds our target,
we can disregard it.

How to do this:

define function:
F(i,j,s) = # of subsequences composed of first i elements of length j with sum s
=
    0                                   : j  > i
    0                                   : i == 0
    0                                   : j == 0
    0                                   : s - a[i] <= 0
    1 + F(i-1,1,s)                      : j == 1 and s == arr[i]
    F(i-1,j-1,s-a[i]) + F(i-1,j,s)      : j <= i
    
    Calculate all values of F(i,j,s)
    R + S != R - S:
    Return sum[j=1 to m](F(m,j,R+S) * F(m,j,R-S) % 10^9 + 7)
    
    R + S == R - S:
    Return sum[j=1 to m](F(m,j,R+S) choose 2 % 10^9 + 7)
    
"""

import math

mod = 10**9 + 7

def solve():
    m,r,s = map(int,input().strip().split())
    arr = list(map(int,input().strip().split()))
    print(number_of_subsequence_pairs(arr,r,s))

def number_of_subsequence_pairs(arr,r,s):
    target1 = r + s     # know for fact: target1 >= target2
    target2 = r - s
    m = len(arr)
    arr.insert(0,0)     # 1-indexing
    memo = [[[0] * (target1 + 1) for j in range(m + 1)] for i in range(m + 1)]
    for j in range(1,m+1):
        print(j)
        for i in range(j,m + 1):
            for s in range(1,target1 + 1):
                memo[i][j][s] = num_subsequences(i,j,s,arr,memo) % mod
    return combine_subsequence_pairs(target1,target2,memo,m)

def num_subsequences(i,j,s,arr,memo):
    if j == 1:
        if s == arr[i]*2:
            return 1 + get_num_subsequences(i-1,j,s,memo)
        else:
            return get_num_subsequences(i-1,j,s,memo)
    else:
        return get_num_subsequences(i-1,j-1,s-(arr[i]*2),memo) + get_num_subsequences(i-1,j,s,memo)

def get_num_subsequences(i,j,s,memo):
    if i == 0 or j == 0 or s <= 0: return 0
    else:
        return memo[i][j][s]
    
def combine_subsequence_pairs(target1,target2,memo,m):
    if target1 != target2:
        op = lambda x,y: x * y
    else:
        op = lambda x,y: math.factorial(x)//math.factorial(2)//math.factorial(x-2)
    
    result = 0
    for j in range(1,m+1):
        result += (op(memo[m][j][target1],memo[m][j][target2])) % mod
        result %= mod
    return result
    
solve()
