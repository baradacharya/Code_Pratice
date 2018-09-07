#1. Simple check O(n^2) #internal matching algo python KMP
class Solution(object):
    def rotateString(self, A, B):
        return len(A) == len(B) and B in A+A

#1. KMP Search
class Solution(object):
    def rotateString(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: bool
        """
        m, n = len(A), len(B)
        if m != n : return False
        m = m + m
        lps = self.computeTemporaryArray(B)
        #KMP algorithm
        i, j = 0, 0
        A = A + A

        while i < m and j < n:
            if A[i] == B[j]:
                i += 1
                j += 1
            else:
                if j != 0:
                    j = lps[j - 1]
                else:
                    i += 1
        return j == n

    def computeTemporaryArray(self, pattern):
        lps = [0] * len(pattern)
        index = 0
        i = 1
        while i < len(pattern):
            if pattern[i] == pattern[index]:
                lps[i] = index + 1
                index += 1
                i += 1
            else:
                if index != 0:
                    index = lps[index - 1]
                else:
                    lps[i] = 0
                    i += 1
        return lps
s = Solution()
print s.rotateString('abcde','cdeab')
print s.rotateString('aa','a')
