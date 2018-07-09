#row is i , col coresponding possible sum
class Solution(object):
    def findTargetSumWays(self, nums, S):
        """
        :type nums: List[int]
        :type S: int
        :rtype: int
        """
        dp = [[0]*2001  for _  in range(len(nums))]
        dp[0][nums[0]+1000] = 1
        dp[0][-nums[0]+1000] += 1

        for i in range(1,len(nums)):
            for sum in range(-1000,1001):
                if dp[i-1][sum + 1000] > 0:
                    dp[i][sum + nums[i] + 1000] += dp[i - 1][sum + 1000]
                    dp[i][sum - nums[i] + 1000] += dp[i - 1][sum + 1000]
        if S > 1000:
            return 0
        else:
            return dp[len(nums) - 1][S + 1000]

s = Solution()
print s.findTargetSumWays([1, 1, 1, 1, 1],3)

###Bruteforce #TLE
class Solution(object):
    def findTargetSumWays(self, nums, S):
        """
        :type nums: List[int]
        :type S: int
        :rtype: int
        """
        self.count  =0
        self.calculate(nums,0,0,S)
        return self.count

    def calculate(self,nums,i,sum,S):
        if i == len(nums):
            if sum == S:
                self.count += 1
        else:
            self.calculate(nums,i+1,sum+nums[i],S)
            self.calculate(nums,i+1,sum-nums[i], S)



 #2D Dynamic Programming
# public class Solution {
#     public int findTargetSumWays(int[] nums, int S) {
#         int[][] dp = new int[nums.length][2001];
#         dp[0][nums[0] + 1000] = 1;
#         dp[0][-nums[0] + 1000] += 1;
#         for (int i = 1; i < nums.length; i++) {
#             for (int sum = -1000; sum <= 1000; sum++) {
#                 if (dp[i - 1][sum + 1000] > 0) {
#                     dp[i][sum + nums[i] + 1000] += dp[i - 1][sum + 1000];
#                     dp[i][sum - nums[i] + 1000] += dp[i - 1][sum + 1000];
#                 }
#             }
#         }
#         return S > 1000 ? 0 : dp[nums.length - 1][S + 1000];
#     }
# }