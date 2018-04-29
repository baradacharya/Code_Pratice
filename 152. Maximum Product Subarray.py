##in product keep track of max and min simantanously
class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums: return 0
        maximum = max_ = min_ = nums[0]
        for i in range(1,len(nums)):
            max_temp = max(nums[i],max_* nums[i], min_ * nums[i])
            min_temp = min(nums[i],max_* nums[i], min_ * nums[i])

            maximum = max(maximum,max_temp)

            max_ = max_temp
            min_ = min_temp
        return maximum


