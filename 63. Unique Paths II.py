class Solution(object):
    """
    An obstacle and empty space is marked as 1 and 0 respectively in the grid.
    """
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        #need 1 for reachable and 0 for not reachable(convection), so have to revert
        obstacleGrid[0][0] = 1 - obstacleGrid[0][0]  # revert 1st position as it is reachable

        # column wise
        for i in range(1, n):
            if obstacleGrid[0][i]:  # obstacle
                obstacleGrid[0][i] = 0
            else:
                obstacleGrid[0][i] = obstacleGrid[0][i - 1]

        # row wise
        for i in range(1, m):
            if obstacleGrid[i][0]: #obstacle
                obstacleGrid[i][0] = 0
            else:
                obstacleGrid[i][0] = obstacleGrid[i - 1][0]

        for i in range(1,m):
            for j in range(1,n):
                if obstacleGrid[i][j]: #obstacle
                    obstacleGrid[i][j] = 0
                else:
                    obstacleGrid[i][j] = obstacleGrid[i - 1][j] + obstacleGrid[i][j - 1]

        return obstacleGrid[-1][-1]

s = Solution()
s.uniquePathsWithObstacles([[0,0],[0,0]])




