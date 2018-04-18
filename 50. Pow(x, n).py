class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        if n < 0 :
            x  = 1/x
            n = -n
        return self.Pow(x,n)
    def Pow(self,x,n):
        if n == 0: return 1
        if n ==1: return x
        half = self.Pow(x,n/2)
        if n%2 == 0: #even
            return half * half
        else:
            return half * half * x