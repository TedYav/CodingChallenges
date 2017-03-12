"""

    Maximum Subarray with Sum K
    
    SOLUTIONS:
        BF: just examine all possible subarrays. This will take O(n^3) time. One possible start, one possible end. Sum all in between.
        BETTER: Generate them progressively. O(n^2)
        BEST: Recognize that sum of subarray from A[i] to A[j] is really sum(A[0]...A[j]) - sum(A[0]...A[i-1])
              * Calculate all sums from A[0] to A[n-1] of which there are n.
              * Store in HT along with smallest index that produces that sum.
              * As we discover each new sum s, check if k - s is in HT.
              * If so, if current index - HT[k - s] > max_length, update max_length
              * Return max_length
              
              Store lowest index because:
                # add current sum to partial sums, IF it's not in there
                # otherwise we want to keep previous index because it's smaller
                # and they're not able to be differentiated
            
              O(n)

"""
def test_msal():
    sut = Solution()
    f = sut.maxSubArrayLen
    
    assert f([],5) == 0, "TC1"      # PASS
    assert f([5],5) == 1, "TC2"     # PASS
    assert f([1,-1,5,-2,3],3) == 4  # PASS
    assert f([-2,-1,2,1],1) == 1    # PASS
    
    """
        current_sum = 0
        max_length = 0
        partial_sums{
            0   : 0
            -2  : 1
            -3  : 2
            -1  : 3
            0   : 4
        }
    
    """

class Solution(object):
    def maxSubArrayLen(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        partial_sums = {0:0}
        max_length = 0
        current_sum = 0
        for i in range(len(nums)):
            current_sum += nums[i]
            
            if current_sum not in partial_sums:
                partial_sums[current_sum] = i+1
            
            complement = current_sum - k            # we subtract k from the current sum to see what we need to *subtract*, not add.
            if complement in partial_sums:
                if (i+1) - partial_sums[complement] > max_length:
                    max_length = i+1 - partial_sums[complement]
            
        return max_length    
