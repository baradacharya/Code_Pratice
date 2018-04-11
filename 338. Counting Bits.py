"""
An easy recurrence for this problem is f[i] = f[i / 2] + i % 2.
f[4] = f[2] , (100) , (10)
f[5] = f[2]+ 1, (101), (10) + 1
"""
class Solution(object):
    def countBits(self, num):
        """
        :type num: int
        :rtype: List[int]
        """
        DP  = [0] * (num+1)
        for i in range(1,num+1):
            DP[i] = DP[i>>1] + i%2 #i%2 for detecting odd or even
        return DP
s = Solution()
print s.countBits(2)