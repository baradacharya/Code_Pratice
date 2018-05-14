"""
dp[i][j] = max profit we can make upto  prices[j] and at most i transaction.
         = max(dp[i][j-1] #won't make any transaction
                #will make transaction (mainly sell) #buy at k and sell at j
                @assume we have bought at k, find k for which max profit. i-1 transaction
                for k in range[0,j-1]:
                    prices[j] - prices[k] + dp[i-1][k])
         = max(dp[i][j-1], prices[j] + max(dp[i-1][k]-prices[k])
dp[0][j] = 0 transactions 0 profit
dp[k][0] = 0 , one price can't make transactions.
"""
#Transaction includes both buy and sell.
class Solution(object):
    def maxProfit(self, k, prices):
        """
        :type k: int
        :type prices: List[int]
        :rtype: int
        """
        if not prices or len(prices) == 1:
            return 0
        n = len(prices)
        if k >= n / 2:  # we can make as many of transactions.
            max_profit = 0
            for i in range(1, len(prices)):
                if prices[i] > prices[i - 1]:
                    max_profit += prices[i] - prices[i - 1]
            return max_profit

        dp = [[0] * n for _ in range(k + 1)]  # transaction * prices
        for i in range(1, k + 1):
            temp_max = - prices[0]  # dp[i-1][0] - prices[0], dp[i-1][0] is always 0
            for j in range(1, n):
                temp_max = max(temp_max, dp[i - 1][j] - prices[j])
                dp[i][j] = max(temp_max + prices[j], dp[i][j - 1])
        return dp[k][n - 1]



