#similar to 10. Regular Expression Matching
#that looks for next * element, it looks for current element
class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        dp = [[False] * (len(p) + 1) for _ in range(len(s) + 1)]
        dp[-1][-1] = True
        for i in range(len(s), -1, -1):  # trick
            for j in range(len(p) - 1, -1, -1):
                first_match = False
                if i < len(s):
                    first_match = p[j] == s[i] or p[j] == '?' or p[j] == '*'
                if p[j] == "*":
                    dp[i][j] = dp[i][j + 1] or (first_match and dp[i + 1][j])
                else:
                    dp[i][j] = first_match and dp[i + 1][j + 1]
        return dp[0][0]
