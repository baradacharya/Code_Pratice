"""
cash : the maximum profit if we did not have a share of stock
possible in two ways 1. we didn't have share previously (cash)
                     2. we have(hold) but we sell on a given day(hold + prices[i]- fee)
hold :  the maximum profit we could have if we owned a share of stock.
possible in two ways 1. we have share previously (hold)
                     2. we did n't have (cash) but we buy on a given day(cash  - prices[i])
start with cash = 0 #didn't have share, hold = -prices[0] #buy 1st share
use fee either at selling or buying.
"""
class Solution(object):
    def maxProfit(self, prices, fee):
        """
        :type prices: List[int]
        :type fee: int
        :rtype: int
        """
        if not prices: return 0
        hold,cash = -prices[0],0
        for i in range(1,len(prices)):
            hold = max(hold,cash-prices[i])
            cash = max(cash,hold+prices[i]-fee)
        return cash