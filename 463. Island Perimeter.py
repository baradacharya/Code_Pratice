"""
the result is islands * 4 - neighbours * 2
"""
class Solution(object):
    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m = len(grid)
        n = len(grid[0])
        island,neighbour = 0,0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1: #Island
                    island += 1
                    if i >0 and grid[i-1][j] == 1: neighbour += 1
                    if j >0 and grid[i][j-1] == 1: neighbour += 1
        return 4 * island - 2*neighbour #for island 4 side, for neighbour one side will be common for each(won't be perimeter)
