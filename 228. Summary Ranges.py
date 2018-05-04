class Solution(object):
    def summaryRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        res = []
        if not nums: return res
        start = 0
        for end in range(len(nums)):
            if end + 1 < len(nums) and nums[end]+1 == nums[end+1]:
                continue
            if end == start:
                res.append(str(nums[end]))
            else:
                res.append(str(nums[start]) + "->" + str(nums[end]))
            start = end + 1
        return res

s = Solution()
print s.summaryRanges([0,2,3,4,6,8,9])


