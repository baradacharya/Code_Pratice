#keep sys.maxint to keep track of visited one
class Solution(object):
    def arrayNesting(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        import sys
        res = 0
        for i in range(len(nums)):
            if nums[i] != sys.maxint:
                start = nums[i]
                count = 0
                while (nums[start] != sys.maxint):
                    temp = start
                    start = nums[start]
                    count += 1
                    nums[temp] = sys.maxint
                res = max(res, count)
        return res