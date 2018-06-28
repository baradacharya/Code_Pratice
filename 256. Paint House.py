"""
Just like : viterbi algorithm DP
The 1st row is the prices for the 1st house, we can change the matrix to present sum of prices from the 2nd row.
i.e, the costs[1][0] represent minimum price to paint the second house red plus the 1st house.
"""

class Solution(object):
    def minCost(self, costs):
        """
        :type costs: List[List[int]]
        :rtype: int
        """
        if not costs:
            return 0

        for i in range(1,len(costs)):
            costs[i][0] += min(costs[i - 1][1], costs[i - 1][2])  # for red
            costs[i][1] += min(costs[i - 1][0], costs[i - 1][2])
            costs[i][2] += min(costs[i - 1][0], costs[i - 1][1])
        return min(costs[-1])
s = Solution()
print s.minCost([[17,2,17],[16,16,5],[14,3,19]])


