class Solution(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s)
        if n == 0: return 0
        dp = [0] * (n + 1)
        dp[n] = 1
        if s[n - 1] == '0':
            dp[n - 1] = 0
        else:
            dp[n - 1] = 1

        for i in range(n - 2, -1, -1):
            if s[i] == '0':
                continue
            num = s[i:i + 2]
            if int(num) <= 26:
                dp[i] = dp[i + 1] + dp[i + 2]
            else:
                dp[i] = dp[i + 1]
        return dp[0]