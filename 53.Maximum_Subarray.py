"""
keep track of two variables.
T: O(n) S:O(1)
"""
class Solution(object):
    def maxSubArray(self, nums):
        if not nums:
            return 0
        maxSum = curSum = nums[0]
        for num in nums[1:]:
            curSum = max(num,curSum + num)
            maxSum = max(maxSum, curSum)
        return maxSum