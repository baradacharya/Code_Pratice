"""
0 form by 5 * 2
no of 2 factorial is enough so just count number of 5 in a num
"""
class Solution(object):
    def trailingZeroes(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 0: return 0
        return n/5 + self.trailingZeroes(n/5)
