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
    * O(n^2)
    

    BEST:
    number digits of n from 0 to n-1
    add up all #'s that end at n[0], n[1], n[2] etc.
    sum(#'s ending with n[0]) = n[0] = s(0)
    let s(i) = sum of numbers ending at position n[i]
    s(i) = (i+1 * n_i) + 10 * s(i-1)

    We want the number sum(s(0),s(1)...s(n-1)) % 10**9 + 7

    Linear time. O(n)
        
"""

def solve():
    n = input().strip()
    print(add_substrings(n))

mod = 10**9 + 7
nums = {
    '0':0,
    '1':1,
    '2':2,
    '3':3,
    '4':4,
    '5':5,
    '6':6,
    '7':7,
    '8':8,
    '9':9
}
def add_substrings(num_string):
    result = nums[num_string[0]]
    prev = result
    for i in range(1,len(num_string)):
        prev = ((10 * prev) + ((i+1) * nums[num_string[i]]))% mod
        result = (prev + result) % mod
    return result

solve()
