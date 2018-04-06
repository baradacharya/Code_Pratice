"""
largest peak following the smallest valley.
minprice  : the smallest valley
maxprofit :maximum difference between selling price and minprice obtained so far respectively.
T: O(n)
S: O(1)
"""
class Solution(object):
    def maxProfit(self, prices):
        if(len(prices) == 0 or len(prices) == 1):
            return 0
        max_profit = 0
        min_ = prices[0]
        for i in range(1,len(prices)):
            min_ = min(prices[i], min_)
            max_profit = max(max_profit,prices[i]- min_)

        return max_profit