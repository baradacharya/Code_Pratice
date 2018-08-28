#DP
class Solution(object):
    def findLength(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: int
        """
        if not A or not B: return 0
        max_len = 0
        dp = [[0] * (len(B) + 1) for _ in range(len(A) + 1)]
        dp[0][0] = 0
        for i in range(1, len(A) + 1):
            for j in range(1, len(B) + 1):
                if A[i - 1] == B[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                    max_len = max(max_len, dp[i][j])
        return max_len

s = Solution()
print s.findLength([1,2,3,2,1],[3,2,1,4,7])
