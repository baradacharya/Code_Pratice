class Solution(object):
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        print bin(x)
        print bin(x^y)
        return bin(x^y).count('1')

s = Solution()
print s.hammingDistance(2,5)