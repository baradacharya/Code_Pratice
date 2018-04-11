class Solution(object):
    """
    dp[i] = dp[i-j*j] + 1 if i-j*j>=0 j>=1
    """
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 0: return 0
        dp = [i for i in range(n+1)]
        for i in range(1,n+1):
            j = 1
            while  i-j*j>=0:
                dp[i] = min(dp[i - j * j] + 1,dp[i])
                j +=1
        return dp[n]
s= Solution()
print s.numSquares(12)

