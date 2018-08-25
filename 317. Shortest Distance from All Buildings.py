"""
Short version: BFS from every building, calculate the distances and find the minimum distance in the end.

Key optimization : we do not go into a land, if it is not accessible by at least one of previous buildings.
"""
class Solution(object):
    class Solution(object):
        def shortestDistance(self, grid):
            """
            :type grid: List[List[int]]
            :rtype: int
            """
            m, n = len(grid), len(grid[0])
            dist = [[0] * n for _ in range(m)] #will store distance from all buildings from that p[oint
            buildings = []

            # initializa building list, accesibilty matrix grid
            for i in range(m):
                for j in range(n):
                    if grid[i][j] == 1:  # building
                        buildings.append((i, j, 0))
                    grid[i][j] = -grid[i][j] #all 0 will be 0 rest will be negative

            # BFS from every building
            for k in range(len(buildings)):
                self.bfs(buildings[k], k, dist, grid, m, n)

            # find minnimum distance
            ans = -1
            for i in range(m):
                for j in range(n):
                    if grid[i][j] == len(buildings) and (ans < 0 or dist[i][j] < ans):  # all buildings are accesible
                        ans = dist[i][j]
            return ans

        def bfs(self, root, k, dist, grid, m, n):
            queue = [root]
            dirs = [[-1, 0], [1, 0], [0, -1], [0, 1]]
            while queue:
                x, y, distance = queue.pop(0)
                dist[x][y] += distance
                for i, j in dirs:
                    x_, y_ = x + i, y + j
                    #if point is reachable from all previous buildings then processes
                    if 0 <= x_ < m and 0 <= y_ < n and grid[x_][y_] == k:
                        grid[x_][y_] = k + 1 #update grid to keep track of number of buildings reachable
                        queue.append((x_, y_, distance + 1))
s = Solution()
print s.shortestDistance([[1,0,2,0,1],[0,0,0,0,0],[0,0,1,0,0]])
