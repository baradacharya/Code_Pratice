#T: O(m*n)
#S: O(m*n)
#Stack array beats recursion
# class Solution(object):
#
#     def maxAreaOfIsland(self, grid):
#         """
#         :type grid: List[List[int]]
#         :rtype: int
#         """
#         if not grid: return 0
#         m,n = len(grid),len(grid[0])
#         max_area = 0
#         for i in range(m):
#             for j in range(n):
#                 if grid[i][j] == 1:
#                     cur_area = [0]
#                     self.DFS(grid,i,j,cur_area)
#                     max_area = max(max_area,cur_area[0])
#         return max_area
#
#     def DFS(self,grid,i,j,area):
#         if i < 0  or i >= len(grid) or j < 0  or j >= len(grid[0]) or grid[i][j] != 1:
#             return
#
#         grid[i][j] = 0
#         area[0] += 1
#         self.DFS(grid,i+1,j,area)
#         self.DFS(grid, i-1,j,area)
#         self.DFS(grid, i, j+1,area)
#         self.DFS(grid, i, j-1,area)

#100% beat
class Solution(object):
    def maxAreaOfIsland(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        if not grid:
            return 0
        m,n = len(grid),len(grid[0])
        max_area = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    grid[i][j] = 0
                    area = 1
                    stack = [(i, j)]
                    while stack:
                        x, y = stack.pop()
                        if x < m - 1 and grid[x + 1][y] == 1:
                            stack.append((x + 1, y))
                            grid[x + 1][y] = 0
                            area += 1
                        if y < n - 1 and grid[x][y + 1] == 1:
                            stack.append((x, y + 1))
                            grid[x][y + 1] = 0
                            area += 1
                        if x > 0 and grid[x - 1][y] == 1:
                            stack.append((x - 1, y))
                            grid[x - 1][y] = 0
                            area += 1
                        if y > 0 and grid[x][y - 1] == 1:
                            stack.append((x, y - 1))
                            grid[x][y - 1] = 0
                            area += 1
                    max_area = max(max_area, area)
        return max_area

s = Solution()
print s.maxAreaOfIsland([[1,1,0,0,0],[1,1,0,0,0],[0,0,0,1,1],[0,0,0,1,1]])