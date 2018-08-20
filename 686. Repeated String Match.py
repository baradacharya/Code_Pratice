"""
Given two strings A and B, find the minimum number of times A has to be repeated such that
B is a substring of it. If no such solution, return -1.
"""
"""
Imagine we wrote S = A+A+A+.... If B is to be a substring of S,
we only need to check whether some S[0:], S[1:], ..., S[len(A) - 1:] starts with B,
as S is long enough to contain B, and S has period at most len(A).

Now, suppose q is the least number for which len(B) <= len(A * q).
We only need to check whether B is a substring of A * q or A * (q+1).
If we try k < q, then B has larger length than A * q and therefore can't be a substring.
When k = q+1, A * k is already big enough to try all positions for B; namely, 

A[i:i+len(B)] == B for i = 0, 1, ..., len(A) - 1.

T: O(N*(N+M))
S: O(M+N)
"""
class Solution(object):
    def repeatedStringMatch(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: int
        """
        import math
        q = int(math.ceil(float(len(B)) / len(A)))
        print (A * (q))
        print (A * (q + 1))
        for i in range(2):
            if B in A * (q+i):
                return q+i
        return -1
s = Solution()
print s.repeatedStringMatch("abcd","cdabcdabc")