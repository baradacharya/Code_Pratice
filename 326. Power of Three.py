#1 Loop Iteration
#3 Mathematics i = log3(n) = log(n)/log(3)
#4 Integer Limitations 3^[log3maxint] = 3^19 = =1162261467
class Solution(object):
    # T: O(log n)
    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n <= 0:
            return False
        while n % 3 == 0:
            n = n / 3
        return n == 1

    def isPowerOfThree(self, n):
        return n > 0 & 1162261467 % n == 0