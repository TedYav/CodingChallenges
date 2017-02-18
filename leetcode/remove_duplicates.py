class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if nums is None or len(nums) == 0: return 0
        else:
            unique = 1
            for i in range(1,len(nums)):
                if nums[i] != nums[i-1]:
                    nums[unique] = nums[i]
                    unique += 1
            return unique