class Solution(object):
    def minDistance(self, word1, word2):
        #2-d DP problem
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        m = len(word1)
        n = len(word2)
        #Trick n+1 and m+1
        DP = [[0 for i in range(n + 1)] for j in range(m + 1)]

        #either one string present
        for i in range(1,m+1):
            DP[i][0] = i
        for i in range(1,n+1):
            DP[0][i] = i

        for i in range(1,m+1):
            for j in range(1,n+1):
                if word1[i-1] == word2[j-1]:
                    DP[i][j] = DP[i-1][j-1]
                else:
                    #dp[i-1][j-1] replacement
                    #dp[i-1][j] delete
                    #dp[i][j-1] insert
                    DP[i][j] = min(DP[i-1][j - 1],DP[i][j - 1],DP[i-1][j]) + 1
        return DP[-1][-1]
s = Solution()
s.minDistance("barada","annada")