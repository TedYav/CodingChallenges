"""

    FACTOR COMBINATIONS:
    1. Examine integers from 2 to n/2 --> if a factor is found, recurse on n/factor, adding all ways to make n/factor
    2. Use memoization to save time
    3. Ensure that all lists of factors are monotonically increasing

"""

from math import sqrt, floor, ceil

def factor_combinations(n,memo={}):
    if n not in memo:
        factors = []
        for i in range(2,int(floor(sqrt(n))) + 1):
            if n%i == 0:
                factor = n//i
                factors.append([i,factor])
                factors.extend([[i] + factoring for factoring in factor_combinations(factor,memo) if i <= factoring[0]])
        memo[n] = factors
    return memo[n]

class Solution(object):
    def getFactors(self, n):
        return factor_combinations(n)
            
