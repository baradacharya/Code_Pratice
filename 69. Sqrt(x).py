"""
#binary search
T: O(logn)

Look for the critical point: i * i <= x and (i+1)(i+1)>x

A little trick is using i <= x / i for comparison, instead of i * i <= x, to avoid exceeding integer upper limit.
overflow of (m * m) causes overflow of indices, thus cause infinite loop indirectly.
"""
class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x == 0 or x == 1:
            return x
        l = 1
        r  = x
        while l <= r:
            m  = (l + r)/2
            if m > x/m:
                r = m - 1
            else:#mid <= x/mid
                if (m+1)> x/(m+1):
                    return m
                l = m + 1
s = Solution()
print s.mySqrt(8)