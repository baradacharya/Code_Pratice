"""
dp[i][j]: the longest palindromic subsequence's length of substring(i, j)
State transition:
        dp[i][j] = dp[i+1][j-1] + 2 if s.charAt(i) == s.charAt(j)
        otherwise,
        dp[i][j] = Math.max(dp[i+1][j], dp[i][j-1])

Initialization: dp[i][i] = 1
"""
class Solution(object):
    def longestPalindromeSubseq(self, s):
        """
        :type s: str
        :rtype: int
        """
        n  = len(s)
        dp = [[0]*n for _ in range(n)]
        max_len = 0
        for i in reversed(range(n)):
            dp[i][i] =1
            for j in range(i+1,n):
                if s[i] == s[j]:
                    dp[i][j] = dp[i+1][j-1] + 2
                else:
                    dp[i][j] = max(dp[i+1][j],dp[i][j-1])
        return dp[0][n-1]
s = Solution()
print s.longestPalindromeSubseq("bbbab")