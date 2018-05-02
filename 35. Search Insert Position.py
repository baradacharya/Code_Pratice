class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        # if not nums: return 0
        # for i,num in enumerate(nums):
        #     if num >= target:
        #         return i
        # return len(nums)
        #binary search
        l = 0
        h = len(nums) - 1;
        while l <= h:
            m = (l+h) / 2
            if nums[m] == target:
                return m
            elif nums[m] > target:
                h = m -1
            else:
                l = m + 1
        return l