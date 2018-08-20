"""
The key idea here is to realize that for any number n,
doing a bit-wise AND of n and n−1 flips the least-significant 1-bit in n to 0.
"""
class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        return bin(n).count('1')

s = Solution()
print s.hammingWeight(7)

