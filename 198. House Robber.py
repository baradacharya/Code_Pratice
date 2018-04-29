class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums: return 0
        if len(nums) == 1: return nums[0]
        res = [0] * len(nums)
        res[0] = nums[0]
        for i in range(1,len(nums)):
            #python treating res[-1] as 0 as it is the last elemnet
            res[i] = max(res[i-1], res[i-2]+ nums[i])
        return res[-1]
