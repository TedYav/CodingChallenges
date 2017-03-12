"""

    THIS SOLUTION IS A CORRECT APPROACH—IF and ONLY IF the arrays contain unique elements.
    I have not finished fixing bugs because it will break in non unique elements.
    This attempts to partition the arrays by guessing at the median. This actually takes O(log(max(a_m,b_n))
    BETTER TO JUST FIND THE INDICES i and j in each array, SINCE ARRAYS ARE SORTED.
    
    Two Sorted Arrays of size m and n
    Find median of them both in O(log(m+n)) time.
    
    We're going to ignore duplicates for now.
    
    Array a and Array b
    
    CASE 1: sequential
        a_0 < a_m < b_0 < b_n
        OR
        b_0 < b_n < a_0 < a_m
        EASY: just pick (m + n)//2 element if m+n is odd, else average (m+n)//2 (m+n)//2 + 1 elements
    
    CASE 2: overlap
    a_0 = 0, a_1 = 3, b_0 = 2
    nums1 = [1, 3]
    nums2 = [2]
    Since a_0 < b_0 and b_0 < a_m, we know the arrays overlap.
    We could merge them together, merge sort style. This would take O(min(m,n)) time. Then select O(1)
    
    HERE'S WHAT WE CAN DO: we do not know the exact ordering of numbers. BUT GIVEN A SPECIFIC NUMBER,
        we can partition our two arrays in logarithmic time, and determine how large the halves are.
        
        We want to find a number such that the arrays are partitioned into two halves differing by at most one.
    
    STRATEGY:
        Modified binary search.
        low = min(a_0,b_0)
        high = max(a_m,b_n)
        guess = low + (high - low)//2
        a_below = b_below = 0
        a_above = len(a)
        b_above = len(b)
        while abs((a_below + b_below) - (a_above + b_above)) > 1:
            * partition around current guess
            * compare sizes of halves
            * repeat
        return closest value to current num that's present in the arrays.

"""

def test_find_median():
    sut = Solution()
    def test(a,b,expected,tc_num):
        assert sut.findMedianSortedArrays(a,b) == expected, "TC%d FAILED. %r %r %r" % (tc_num,a,b,expected)
        print("TC%d PASSED %r %r %r" % (tc_num,a,b,expected))
    
    test([],[],0,1)             # PASS
    test([1],[],1,2)            # PASS
    test([],[1],1,3)            # PASS
    test([1,2,3],[],2,4)        # PASS
    test([],[2,3],2.5,5)        # PASS
    test([1,3],[2],2,6)         # FAIL

def median(arr):
    if len(arr) % 2 == 0:
        return (arr[len(arr)//2] + arr[(len(arr)//2) - 1])/2.0
    else:
        return arr[len(arr)//2]

"""

return value --> i+1 values are in arr_below len(arr) - i+1 are in arr_above 

[1,2,3] target = 2  i = 1       PASS
[1,2,3] target = 3  i = 2       PASS
[1,2,3] target = 4  i = 2       PASS
[1,2,3] target = 1  i = 0       PASS
[1,2,3] target = 0  i = -1      PASS

"""

def bin_search_lte(arr,target):
    low = 0
    high = len(arr) - 1
    guess = low + (high - low)//2
    while high > low:
        if arr[guess] <= target and (guess + 1 == len(arr) or arr[guess+1] > target):
            return guess
        elif arr[guess] <= target and arr[guess + 1] <= target:
            low = guess + 1
        elif arr[guess] > target:
            high = guess - 1
        guess = low + (high - low)//2
    return low if arr[low] <= target else -1

"""

    GOAL: return first index in arr which is > target. If all values are <= target, return -1
    [1,2,3] target = 2  i = 2       PASS
    [1,2,3] target = 3  i = -1      PASS
    [1,2,3] target = 4  i = -1      PASS
    [1,2,3] target = 1  i = 1       PASS
    [1,2,3] target = 0  i = 0       PASS
    
"""

def bin_search_gte(arr,target):
    low = 0
    high = len(arr) - 1
    guess = low + (high-low)//2
    while high > low:
        if arr[guess] > target and (guess - 1 < 0 or arr[guess - 1] <= target):
            return guess
        elif arr[guess] > target and arr[guess - 1] > target:
            high = guess - 1
        elif arr[guess] <= target:
            low = guess + 1
        guess = low + (high-low)//2
    return low if arr[low] > target else -1
        

# STILL GIVING Wrong Answer
# Moving on to other problems--got the basic idea.

class Solution(object):
    def findMedianSortedArrays(self, a, b):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        if not a and not b: return 0
        elif len(b) == 0: return median(a)
        elif len(a) == 0: return median(b)
        else:
            low = min(a[0],b[0])            # 1
            high = max(a[-1],b[-1])         # 3
            guess = low + (high-low)/2.0    # 2
            target = ((len(a) + abs(len(b)-len(a)))//2) + (len(a)%2 + len(b)%2)%2
            a_below = bin_search_lte(a,guess) + 1
            b_below = bin_search_lte(b,guess) + 1
            
            # praying there aren't duplicates :)
            while target != a_below + b_below:   # 2 - 1 = 1 COULD BE OVERFLOW here. Let it pass for now.
                if a_below + b_below < target:
                    low = guess
                elif a_below + b_below > target:
                    high = guess
                guess = low + (high-low)/2.0
                a_below = bin_search_lte(a,guess) + 1
                b_below = bin_search_lte(b,guess) + 1
            
            # duplicates can screw me here...
            
            def min_non_negative(num1,num2):
                n_min = min(num1,num2)
                n_max = max(num1,num2)
                return n_min if n_min != -1 else n_max
            
            # overflow safe mod check
            if (len(a)%2 + len(b)%2)%2 == 1:
                return max(a[bin_search_lte(a,guess)], b[bin_search_lte(b,guess)])
            else:
                return (max(a[bin_search_lte(a,guess)], b[bin_search_lte(b,guess)]) + min_non_negative(a[bin_search_gte(a,guess)], b[bin_search_gte(b,guess)]))/2.0
            
        
# test_find_median()
