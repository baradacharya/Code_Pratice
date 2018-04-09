"""
largest peak following the smallest valley.
minprice  : the smallest valley
maxprofit :maximum difference between selling price and minprice obtained so far respectively.
T: O(n)
S: O(1)
"""
class Solution(object):
    #two variable approach
    def maxProfit(self, prices):
        if(len(prices) == 0 or len(prices) == 1):
            return 0
        max_profit = 0
        min_price = prices[0]
        for i in range(1,len(prices)):
            min_price = min(prices[i], min_price)
            max_profit = max(max_profit,prices[i]- min_price)
        return max_profit