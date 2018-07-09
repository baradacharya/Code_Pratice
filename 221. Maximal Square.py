#https://leetcode.com/problems/maximal-square/solution/
class Solution(object):
    def maximalSquare(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        if not matrix: return 0
        m,n = len(matrix),len(matrix[0])
        dp = [[0] * (n+1) for i in range(m+1)] #mark this m+1 and n+1
        max_len = 0
        for i in range(1,m+1):
            for j in range(1,n+1):
                if matrix[i-1][j-1] == '1':
                    dp[i][j] = min(dp[i-1][j],dp[i][j-1],dp[i-1][j-1]) + 1
                    max_len = max(max_len,dp[i][j])
        return max_len*max_len

s = Solution()
# print s.maximalSquare([["1"]])
print s.maximalSquare([["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]])