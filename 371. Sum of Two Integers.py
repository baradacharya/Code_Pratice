class Solution(object):
    def getSum(self, a, b):
        """
        :type a: int
        :type b: int
        :rtype: int
        """
        if a == 0: return b
        if b == 0 : return a
        if a > 0 and b < 0:
            if b == - 2 **31:
                return -self.subtract(-b,a)
            return self.subtract(a,-b)
        elif a < 0 and b > 0 :
            if a == - 2 **31:
                return -self.subtract(-a,b)
            return self.subtract(b,-a)
        elif a <0 and b < 0:
            return -self.add(-a,-b)
        else:
            return self.add(a,b)

    def add(self,a,b) :
        while b != 0:
            carry  = a & b
            a = a ^ b
            b = carry << 1 #shift the carry
        return a
    def subtract(self,a,b):
        while b != 0 :
            borrow = (~a) & b
            a = a ^ b
            b = borrow << 1
        return a

s = Solution()
print s.getSum(4,6)
print s.getSum(2147483647,-2147483648)