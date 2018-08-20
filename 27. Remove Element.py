class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        if not nums: return 0
        i = 0
        for num in nums:
            if num != val:
                nums[i] = num
                i += 1
        return i

s = Solution()
s.removeElement([3,2,2,3],3)