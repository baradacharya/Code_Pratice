class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        if len(nums) == 0:
            return 0
        i = 0
        for j in range(len(nums)):
            if(nums[j] != val):
                nums[i] = nums[j]
                i += 1
        return i

s = Solution()
s.removeElement([3,2,2,3],3)