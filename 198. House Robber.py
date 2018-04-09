class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0: return 0
        if len(nums) == 1: return nums[0]
        DP = [0] * len(nums)
        DP[0] = nums[0]
        for i in range(1,len(nums)):
            DP[i] = max(DP[i-2]+nums[i],DP[i-1])
        return DP[-1]
