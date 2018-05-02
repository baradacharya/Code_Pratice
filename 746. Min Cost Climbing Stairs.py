class Solution(object):
    def minCostClimbingStairs(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        """
        c = []
        c.append(0)
        c.append(0)
        for i in range(2, len(cost)+1):
            temp = min(c[i - 1] + cost[i - 1], c[i - 2] + cost[i - 2])
            c.append(temp)
        return c[i]