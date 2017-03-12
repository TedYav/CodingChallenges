"""
    SAM AND SUBSTRINGS
    
    This problem is basically asking me to add all the possible subarrays of a numeric array together, and return result mod 10**9 + 7 (a prime #).
    
    STRATEGY:
    NAIVE:
        Sum up all possible substrings --> there are O(n^2). Takes O(n) time to read each one. O(n^3), not counting addition time, which could be large given that numbers can be up to 10**2000000.
    
    BETTER:
    
    drop_left:  123 --> 23 mod it with 10**len(substring) - 1
    drop_right: 123 --> 12 int divide by 10
        
        Calculate numbers from x_0,0 to x_0,n
        Use to calculate others. Use mod occasionally. Done.
        
    * Start at beginning of number with no digits
    * Add next digit to right (first digit first time)
        * Add this number, then add all numbers formed by removing one digit from left at a time.
    * Return result
    
    * ADDITION: Memoize. Keep track of which results we've stored.
        
"""

def solve():
    n = input().strip()
    print(add_substrings(n))

mod = 10**9 + 7
def add_substrings(n):
    memo = [[0 for i in range(len(n))]for j in range(len(n))]
    length = len(n)
    n = int(n)
    total = 0
    for stop in range(length-1,-1,-1):
        for start in range(stop + 1):
            if start == 0 and stop == length - 1:
                memo[start][stop] = n
            elif start == 0 and stop != length - 1:
                memo[start][stop] = drop_right(memo[start][stop+1])
            else:
                memo[start][stop] = drop_left(memo[start-1][stop])
            total += memo[start][stop]
            total %= mod
    return total

def int_log(n):
    log = 0
    while n > 0:
        n //= 10
        log += 1
    return log - 1

def drop_right(n): return n//10
def drop_left(n): return n % 10**(int_log(n)) if n >= 10 else 0

solve()
