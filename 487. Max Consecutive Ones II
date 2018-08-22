class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count = 0
        ans = 0
        prev = -1
        for num in nums:
            if num == 1:
                count += 1
            else:
                prev = count
                count = 0
            if ans < prev + count + 1:
                ans = prev + count + 1
        return ans