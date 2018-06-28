class Solution(object):
    def maxKilledEnemies(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        if not grid:
            return 0
        m, n = len(grid), len(grid[0])
        res = 0
        rowhits = 0
        colhits = [0] * n
        for i in range(m):
            for j in range(n):
                # search in this row and remember
                if not j or grid[i][j - 1] == 'W':  # only search if previous one is wall otherwise alreday visited
                    rowhits = 0
                    for k in range(j, n):
                        if grid[i][k] != 'W':
                            rowhits += grid[i][k] == 'E'
                        else:
                            break
                # search in this column and remember
                if not i or grid[i - 1][j] == 'W':
                    colhits[j] = 0
                    for k in range(i, m):
                        if grid[k][j] != 'W':
                            colhits[j] += grid[k][j] == 'E'
                        else:
                            break
                if grid[i][j] == '0':
                    res = max(res, rowhits + colhits[j])
        return res

s = Solution()
print s.maxKilledEnemies([["0","E","0","0"],["E","0","W","E"],["0","E","0","0"]])


