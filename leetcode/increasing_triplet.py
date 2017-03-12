"""

[5,4,3,3,3,3,3,2,1] --> monotonically decreasing, no go
[1,2,2,2,2,2,1,1,1,1,0] --> only one increase. no go.
[1,2,2,2,2,2,1,0,-1,2] --> two increases, but second does not rise above first. No go.
[1,2,2,2,2,2,2,1,2,1,1] --> two increases, but second does not rise above first. No go.
[1,2,2,2,2,1,1,0,1,2,3] --> multiple increases, does rise above first.

SO: look for increasing points. Set i = -1, j = -1, k=-1
First increase, we set i to index, j to index+1.
Subsequent, look at numbers in the increase. If they're smaller than our first set of #'s, then we update i and j. If one is larger, we set k and return True.
If k is still -1 at the end, return False.

"""
tc_num = 0
def test_increasing_triplet():
    sut = Solution()
    def test(nums,expected):
        global tc_num
        assert sut.increasingTriplet(nums) is expected, "TC%d %r %r" % (tc_num, nums, expected)
        print("TC%d passed. %r %r" % (tc_num,nums,expected))
        tc_num += 1
    
    test([],False)              # PASS
    test([1,2],False)           # PASS
    test([1,2,3],True)          # PASS
    test([5,4,3,2,1],False)     # PASS
    test([5,1,5,5,2,5,4],True)  # PASS

class Solution(object):
    def increasingTriplet(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if not nums or len(nums) < 3: return False
        i = j = k = -1
        for index in range(len(nums)-1):
            if nums[index] < nums[index + 1]:
                if (i != j != -1):
                    
                    if nums[index] > nums[i]:
                        j = index
                    
                    if nums[index + 1] > nums[j]:
                        k = index + 1
                        break
                    
                    elif nums[index] < nums[i]:
                       i,j = index,index+1
                else:
                    i,j = index,index+1
                    
        return k != -1
        
# test_increasing_triplet()
        
