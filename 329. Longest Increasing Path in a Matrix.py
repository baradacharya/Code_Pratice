#DP(memorization) + DFS
#T: : O(mn)
class Solution(object):
    def longestIncreasingPath(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: int
        """
        if not matrix: return 0
        dirs = [[0,1],[1,0],[0,-1],[-1,0]]
        m,n = len(matrix),len(matrix[0])
        ans = 0
        dp = [[0] * n for i in range(m)]

        def DFS(i,j):
            if not dp[i][j]:#has n't calculated earlier
                val = matrix[i][j]
                ans = 0
                for x,y in dirs:
                    x += i
                    y += j
                    if 0 <= x < m and 0 <=y < n and val < matrix[x][y]:
                        ans = max(ans,DFS(x,y))#find the longest
                dp[i][j] = 1 + ans
            return dp[i][j]

        for i in range(m):
            for j in range(n):
                ans = max(ans,DFS(i,j))
        return ans

s = Solution()
print s.longestIncreasingPath([[9,9,4],[6,6,8],[2,1,1]])