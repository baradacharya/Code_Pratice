"""
0/1 knapsack detailed explanation https://leetcode.com/problems/partition-equal-subset-sum/discuss/90592/01-knapsack-detailed-explanation

find whether there are several numbers in a set which are able to sum to a specific value (sum/2).
Actually, this is a 0/1 knapsack problem, for each number, we can pick it or not.
Let us assume dp[i][j] means whether the specific sum j can be gotten from the first i numbers.
If we can pick such a series of numbers from 0-i whose sum is j, dp[i][j] is true, otherwise it is false.

Base case: dp[0][0] is true; (zero number consists of sum 0 is true)

For each number, if we don't pick it, dp[i][j] = dp[i-1][j],
If we pick nums[i]. dp[i][j] = dp[i-1][j-nums[i]]
dp[i][j] = dp[i-1][j] || dp[i-1][j-nums[i]]

"""
class Solution(object):
    def canPartition(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        sum_ = sum(nums)
        if sum_ & 1 == 1:
            return False #odd sum can't happen

        sum_ /= 2

        n = len(nums)
        dp = [[False] * (sum_+1) for _ in range(n)]

        dp[0][0] = True #base case

        for i in range(1,n+1):
            dp[i][0] = True

        for j in range(1,sum_+1):
            dp[0][j] = False

        for i in range(1,n+1):
            for j in range(1, sum_ + 1):
                if j-nums[i-1] >= 0:
                    dp[i][j] = dp[i-1][j] or dp[i-1][j-nums[i-1]]
                else:
                    dp[i][j] = dp[i - 1][j]

        return dp[n][sum_]
