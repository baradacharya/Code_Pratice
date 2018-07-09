class Solution(object):
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        # print '{:032b}'.format(x),'{:32b}'.format(x),'{:b}'.format(x)
        # print bin(x^y),bin(x),bin(y)
        return bin(x^y).count('1')

s = Solution()
print s.hammingDistance(2,5)