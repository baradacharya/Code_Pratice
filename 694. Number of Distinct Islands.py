##Hash By Local Coordinates

# 1: Hash By Path Signature
class Solution(object):
    def numDistinctIslands(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m,n = len(grid),len(grid[0])
        def DFS(i,j,direction =0):
            if 0 <= i < m and 0 <= j < n and grid[i][j]:
                grid[i][j] = 0
                shape.append(direction)
                DFS(i+1,j,1)
                DFS(i-1,j,2)
                DFS(i,j+1,3)
                DFS(i,j-1,4)
                shape.append(0) #add 0 at beg and end of shape
        shapes = set()
        for i in range(m):
            for j in range(n):
                if grid[i][j]:
                    shape =[]
                    DFS(i,j)
                    if shape: shapes.add(tuple(shape))
        return len(shapes)
s = Solution()
grid = [[1,1,0,1,1],[1,0,0,0,0],[0,0,0,0,1],[1,1,0,1,1]]
print s.numDistinctIslands(grid)
