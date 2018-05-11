class Solution(object):
    # def canJump(self, nums):T:O(n)
    #     """
    #     :type nums: List[int]
    #     :rtype: bool
    #     """
    #     #74 / 75 test cases passed. TLE
    #     reachable = [False] * len(nums)
    #     reachable[0] = True
    #     for i in range(len(nums)):
    #         if reachable[i]:
    #             for j in reversed(range(1,nums[i]+1)):#last with the largexst one to stop
    #                 if i + j == len(nums) - 1:  ##last reached
    #                     return True
    #                 if i + j < len(nums):
    #                     if reachable[i + j]:break
    #                     else:reachable[i + j] = True
    #     return reachable[-1]

    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        n = len(nums)
        i = 0
        reach = 0
        while i <= reach and i < n:
            if i + nums[i] > reach:
                reach = i + nums[i]
            i += 1
        return i == n


s = Solution()
print s.canJump([2,3,1,1,4])