class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        if not grid: return 0
        m, n = len(grid), len(grid[0])
        count = 0
        for i in range(m):
            for j in range(n):  # start with any point
                if grid[i][j] == "1":
                    self.DFS(grid, i, j)
                    count += 1
        return count

    def DFS(self, grid, i, j):
        if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]) or grid[i][j] != "1":#condition for not valid
            return
        grid[i][j] = "0"
        self.DFS(grid, i + 1, j)
        self.DFS(grid, i - 1, j)
        self.DFS(grid, i, j + 1)
        self.DFS(grid, i, j - 1)



