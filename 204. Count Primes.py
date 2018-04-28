class Solution(object):
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        notprime = [False] * n
        count  = 0
        for i in range(2,n):
            if notprime[i] == False:
                count += 1
                j = 2
                while i*j < n:
                    notprime[i*j] = True
                    j += 1
        return count