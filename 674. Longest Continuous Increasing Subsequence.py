class Solution(object):
    def findLengthOfLCIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        i,j = 0,0
        max_len = 0
        while j < len(nums):
            if j < len(nums) -1 and nums[j] < nums[j+1]:
                j += 1
                continue
            else:
                max_len = max(max_len,j-i+1)
                i = j + 1
                j += 1
        return max_len