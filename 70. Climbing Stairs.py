class Solution(object):
    #1D DP
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if(n==0):
            return 0
        DP = []
        DP.append(1)
        DP.append(2)
        for i in range(2,n):
            DP.append(DP[i - 1] +  DP[i - 2]) #can reach i from both i-1 and i-2 step
        return DP[n-1]
s =Solution()
print s.climbStairs(2)
