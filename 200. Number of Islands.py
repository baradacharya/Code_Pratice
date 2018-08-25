#T: O(m*n)
#space O(m*n)

#BFS T:O(m*n), S:O(min(m,n))
##Stack array beats recursion
#75% beat
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

#99% beat, stack better than recursion
class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        if not grid:
            return 0
        count = 0
        m = len(grid)
        n = len(grid[0])
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    grid[i][j] = 0
                    count += 1
                    stack = [(i, j)]
                    while stack:
                        x, y = stack.pop()
                        if x < m - 1 and grid[x + 1][y] == '1':
                            stack.append((x + 1, y))
                            grid[x + 1][y] = 0
                        if y < n - 1 and grid[x][y + 1] == '1':
                            stack.append((x, y + 1))
                            grid[x][y + 1] = 0
                        if x > 0 and grid[x - 1][y] == '1':
                            stack.append((x - 1, y))
                            grid[x - 1][y] = 0

                        if y > 0 and grid[x][y - 1] == '1':
                            stack.append((x, y - 1))
                            grid[x][y - 1] = 0

        return count


