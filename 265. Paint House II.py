class Solution(object):
    def minCostII(self, costs):
        """
        :type costs: List[List[int]]
        :rtype: int
        """
        if  len(costs):
            return 0
        num_house,num_color = len(costs),len(costs[0])
        for i in range(1,num_house):
            for j in range(num_color):
                costs[i][j] += self.get_min(costs[i-1],j)  # for red
        return min(costs[-1])

    def get_min(self,row,j):
        import sys
        min_ = sys.maxint
        for i,num in enumerate(row):
            if i == j:
                continue
            min_ = min(min_,num)
        return min_