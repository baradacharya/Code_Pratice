class Solution(object):
    def repeatedStringMatch(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: int
        """
        import math
        q = int(math.ceil(float(len(B)) / len(A)))
        for i in range(2):
            if B in A * (q+i): return q+i
        return -1
s = Solution()
print s.repeatedStringMatch("abcd","cdabcdab")