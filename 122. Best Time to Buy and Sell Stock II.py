"""
cash : the maximum profit if we did not have a share of stock
possible in two ways 1. we didn't have share previously (cash)
                     2. we have(hold) but we sell on a given day(hold + prices[i])
hold :  the maximum profit we could have if we owned a share of stock.
possible in two ways 1. we have share previously (hold)
                     2. we did n't have (cash) but we buy on a given day(cash  - prices[i])
start with cash = 0 #didn't have share, hold = -prices[0] #buy 1st share
"""
#You may complete as many transactions as you like
class Solution(object):
    def maxProfit(self, prices):

        if(len(prices)==0):
            return 0
        cash, hold  = 0, -prices[0]
        for  i in range(1,len(prices)):
            cash = max(cash,    hold + prices[i])
            hold = max(hold,    cash - prices[i])
        return cash

    #peak followed by valley
    def maxProfit(self, prices):
        maxProfit  = 0
        for i in range(1,len(prices)):
            if prices[i] > prices[i-1]:
                maxProfit  += prices[i]- prices[i-1]
        return maxProfit

