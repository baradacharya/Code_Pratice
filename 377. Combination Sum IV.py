#the no of combinations of target, comb[target] = sum(comb[target - nums[i]]), where 0 <= i < nums.length, and target >= nums[i].
#comb[4] = comb[4-1] + comb[4-2] + comb[4-3] = comb[3] + comb[2] + comb[1].

#Recursive
# class Solution(object):
#     def combinationSum4(self, nums, target):
#         """
#         :type nums: List[int]
#         :type target: int
#         :rtype: int
#         """
#         if target == 0:
#             return 1
#         res = 0
#         for i in range(len(nums)):
#             if (target >= nums[i]):
#                 res += self.combinationSum4(nums, target - nums[i])
#
#         return res

#DP
class Solution(object):
    def combinationSum4(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if target == 0:
            return 1
        dp = [0] * (target+1)
        dp[0] = 1
        for i in range(1,target+1):
            for j in range(len(nums)):
                if i >= nums[j]:
                    dp[i] += dp[i-nums[j]]
        return dp[target]

s =Solution()
print s.combinationSum4([1,2,3],4)