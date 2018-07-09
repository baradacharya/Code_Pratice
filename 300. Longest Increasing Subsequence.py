class Solution(object):
    def lengthOfLIS(self, nums):
        if(len(nums) == 0):
            return 0
        dp = [1] * len(nums)
        max_len = 1
        for i in range(1,len(nums)):
            for j in range(i):
                if nums[i] > nums[j]:
                    if dp[j] >= dp[i]:
                        dp[i] = dp[j]+1
                    max_len = max(max_len,dp[i])
        return max_len
