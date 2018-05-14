#complete at most two transactions.
#look 188 for generalize k transactions
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if not prices or len(prices) == 1:
            return 0
        n = len(prices)
        k = 2
        dp = [[0]*n for _ in range(k+1)] #transaction * prices
        for i in range(1,k+1):
            temp_max = - prices[0] #dp[i-1][0] - prices[0], dp[i-1][0] is always 0
            for j in range(1,n):
                temp_max = max(temp_max,dp[i-1][j] - prices[j])
                dp[i][j] = max(temp_max+prices[j],dp[i][j-1])
        return dp[k][n-1]