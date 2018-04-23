class Solution(object):
    def getSum(self, a, b):
        """
        :type a: int
        :type b: int
        :rtype: int
        """
        if a == 0: return b
        if b == 0 : return a
        while b != 0:
            a = bin(a) ^ bin(b)
            carry  = a & b
            b = carry << 1
s = Solution()
print s.getSum(1,3)