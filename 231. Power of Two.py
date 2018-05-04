class Solution(object):
    # def isPowerOfTwo(self, n):
    #     """
    #     :type n: int
    #     :rtype: bool
    #     """
    #     if n < 0: return False
    #     if bin(n).count('1') == 1:
    #         return True
    #     else:
    #         return False

    #T: O(1)
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n < 0: return False
        return  not (n & (n-1))
    #T:O(log n)
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        while n % 2 == 0:
            n = n / 2
        return n == 1
    #math int limitation 2^30 ==
    # return n > 0 & 2^30 % n == 0