class Solution(object):
    def maxVacationDays(self, flights, days):
        """
        :type flights: List[List[int]]
        :type days: List[List[int]]
        :rtype: int
        """
        if len(days) == 0 or len(flights) == 0:
            return 0

        dp = [[0]* (len(days[0])+ 1) for _ in range(len(days))]
        for week in range(len(days[0])-1,-1,-1):
            for cur_city in range(len(days)):
                dp[cur_city][week] = days[cur_city][week]  + dp[cur_city][week+1]
                for dest_city in range(len(days)):
                    if flights[cur_city][dest_city] == 1:
                        # if we stay in the same city, if we move to another city
                        dp[cur_city][week] = max(days[dest_city][week] + dp[dest_city][week+1],
                                                 dp[cur_city][week])
        return dp[0][0]

s = Solution()
print s.maxVacationDays([[0,1,1],[1,0,1],[1,1,0]],[[1,3,1],[6,0,3],[3,3,3]])
