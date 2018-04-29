#bit manpulation
#no multiply,division,mod operation
#will subtract divisor from dividend, repeatively and maintain count
#we can subtract incrementally, (less time complexity), in this method subtract amount will be doubled(like binary )
class Solution(object):
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        if divisor == 0 :
            raise ValueError

        if dividend == -2**31 and divisor == -1 :
            return 2**31-1

        negative = (dividend < 0) ^ (divisor < 0)
        res = 0
        dividend,divisor = abs(dividend),abs(divisor)
        while divisor <= dividend :
            temp = divisor
            multiple = 1

            while temp <= dividend:
                dividend -= temp
                res += multiple
                multiple <<= 1 #increse the i twice
                temp <<= 1

        if negative:
            res = -res
        return res


s = Solution()
print s.divide(2**31,1)
