
class Solution(object):
    def __init__(self,n):
        self.num = n
    def guess(self,m):
        if m == self.num: return 0
        elif m < self.num : return 1
        else: return -1

    def guessNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        i = 0
        j = n
        while i < j:
            m = (i+j)/2
            if self.guess(m) == 0:
                return m
            elif self.guess(m) == 1:
                i = m + 1
            else:
                j = m
        return i