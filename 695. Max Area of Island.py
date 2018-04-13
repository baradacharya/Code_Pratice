class Solution(object):

    def maxAreaOfIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        if not grid: return 0
        m,n = len(grid),len(grid[0])
        max_area = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    cur_area = [0]
                    self.DFS(grid,i,j,cur_area)
                    max_area = max(max_area,cur_area[0])
        return max_area

    def DFS(self,grid,i,j,area):
        if i < 0  or i >= len(grid) or j < 0  or j >= len(grid[0]) or grid[i][j] != 1:
            return

        grid[i][j] = 0
        area[0] += 1
        self.DFS(grid,i+1,j,area)
        self.DFS(grid, i-1,j,area)
        self.DFS(grid, i, j+1,area)
        self.DFS(grid, i, j-1,area)


s = Solution()
print s.maxAreaOfIsland([[0]])