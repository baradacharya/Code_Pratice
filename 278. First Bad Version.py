# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution(object):
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        l,r = 1,n
        while l < r:
            m = (l+r)/2
            res = isBadVersion(m)
            if res == 1:
                r = m
            elif res != 1:
                l = m + 1
        return l