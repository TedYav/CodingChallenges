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
    values = make_initial_value_set(arr,target1)
    arr.insert(0,0)     # 1-indexing
    memo = [[{} for j in range(m + 1)] for i in range(m + 1)]
    for j in range(1,m+1):
        for i in range(j,m + 1):
            s_range = calculate_sum_range(target1,values,i,j,memo)
            for s in s_range:
                count = count_subsequences(i,j,s,arr,memo)
                if count != 0:
                    memo[i][j][s] = count
    return combine_subsequence_pairs(target1,target2,memo,m)

def make_initial_value_set(arr,target):
    return set([i*2 for i in arr if i*2 <= target])

def calculate_sum_range(target,values,i,j,memo):
    if j == 1:
        return values
    elif len(memo[i][j-1]) > 0:
        return range(min(memo[i][j-1]),target + 1)
    else:
        return range(0)

def count_subsequences(i,j,s,arr,memo):
    if j == 1:
        if s == arr[i]*2:
            count = 1 + get_num_subsequences(i-1,j,s,memo)
        else:
            count = get_num_subsequences(i-1,j,s,memo)
    else:
        count = get_num_subsequences(i-1,j-1,s-(arr[i]*2),memo) + get_num_subsequences(i-1,j,s,memo)
    return count

def get_num_subsequences(i,j,s,memo): return memo[i][j].get(s,0)
    
def combine_subsequence_pairs(target1,target2,memo,m):
    result = 0
    for j in range(1,m+1):
        result += (memo[m][j].get(target1,0) * memo[m][j].get(target2,0)) % mod
        result %= mod
    return result
    
solve()
