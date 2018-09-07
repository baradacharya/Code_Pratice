#1. Minmax algorithm
class Solution(object):
    def PredictTheWinner(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        return self.winner(nums,0,len(nums)-1,1) >= 0

    def winner(self,nums,start,end,turn):
        if start == end :
            return turn * nums[start]

        a = turn * nums[start] + self.winner(nums, start + 1, end, -turn)
        b = turn * nums[end] + self.winner(nums, start, end - 1, -turn)

        return turn * max(turn * a, turn * b)

# 2. Memorization algorithm
class Solution(object):
    def PredictTheWinner(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        n = len(nums)
        memo = [[0] * n for _ in range(n)]
        return self.winner(nums, 0, len(nums) - 1, memo) >= 0

    def winner(self, nums, start, end, memo):
        if start == end:
            return nums[start]
        if memo[start][end]:
            return memo[start][end]
        a = nums[start] - self.winner(nums, start + 1, end, memo)
        b = nums[end] - self.winner(nums, start, end - 1, memo)
        memo[start][end] = max(a,b)
        return memo[start][end]

#3. Dynamic programming
class Solution(object):
    def PredictTheWinner(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        n = len(nums)
        dp = [[0] * n for _ in range(n)]
        for s in range(n-2,-1,-1):
            for e in range(s+1,n):
                dp[s][e] = max(nums[s] - dp[s+1][e],nums[e] - dp[s][e-1])
        return dp[0][n-1] >= 0