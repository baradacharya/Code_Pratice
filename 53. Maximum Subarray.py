class Solution(object):
    def maxSubArray(self, nums):
        #two variable approach
        if not nums:
            return 0
        cur_sum,max_sum = nums[0],nums[0]
        for i in range(1,len(nums)):
            cur_sum = max(nums[i],cur_sum + nums[i])
            max_sum = max(cur_sum,max_sum)
        return max_sum
s = Solution()
s.maxSubArray([-2,1,-3,4,-1,2,1,-5,4])