# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):
#looking for first bad
class Solution(object):
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        l,r = 1,n
        while l < r: #l<=r won't work
            m = (l+r)/2
            res = isBadVersion(m)
            if res == 1:
                r = m #all versions after mid can be discarded.
            elif res != 1:
                l = m + 1
        return l