#TLE 60/61
class Solution(object):
    def increasingTriplet(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        # if (len(nums) == 0):
        #     return False
        # dp = [1] * len(nums)
        # for i in range(1, len(nums)):
        #     for j in range(i):
        #         if nums[i] > nums[j]:
        #             dp[i] = max(dp[i], dp[j] + 1)
        #             if dp[i] == 3:
        #                 return True
        # return False
        import sys
        c1 = sys.maxint
        c2 = sys.maxint
        for x in nums:
            if x <= c1:
                c1 = x
            elif x <= c2:
                c2 = x
            else:
                return True
        return False
