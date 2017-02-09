"""

    Move Zeroes:
        Goal: move all zeroes to end of array without making copy of array. Minimize number of operations.
        
        Strategy: keep track of end of non-zero #'s in array. Every time we find non-zero number, swap with trailing 0, increment value
        
        e.g.:
        [0, 1, 0, 3, 12]
         ^ -- non-zero's end at position -1: end = -1
            ^ non-zero #, swap with end + 1, end = 0
        [1, 0, 0, 3, 12]
                  ^ non-zero, swap with end + 1, end = 1
        [1, 3, 0, 0, 12]
                     ^ swap with end + 1, end = 2. done.
                     
        Minimum # of operations because we have to examine all elements in array. And we perform max N swaps.
            We do not swap any elements unnecessarily because we stop swapping once we don't find any more non-zero values.
    
        Runtime: O(n + k) where k == number of zeroes inserted between non-zero elements
"""

# def test_move_zeroes():
#     solution = Solution()
#     mz = solution.moveZeroes
    
#     arr = [0]
#     expected = [0]
#     mz(arr)
#     assert arr == expected, "TC1"       # PASS
    
#     arr = [1]
#     expected = [1]
#     mz(arr)
#     assert arr == expected, "TC2"       # PASS
    
#     arr = [0,1]
#     expected = [1,0]
#     mz(arr)
#     assert arr == expected, "TC3"       # PASS
    
#     arr = [1,2,3,4,5]
#     expected = [1,2,3,4,5]
#     mz(arr)
#     assert arr == expected, "TC4"        # PASS
    
#     arr = [0,0,0,0,1]
#     expected = [1,0,0,0,0]
#     mz(arr)
#     assert arr == expected, "TC5"       # PASS

class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        
        def swap(a,b): nums[a],nums[b]=nums[b],nums[a]
        
        end = -1
        for i in range(len(nums)):
            if nums[i] != 0:
                swap(i,end+1)
                end += 1

# test_move_zeroes()