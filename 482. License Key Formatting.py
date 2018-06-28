class Solution(object):
    def licenseKeyFormatting(self, S, K):
        """
        :type S: str
        :type K: int
        :rtype: str
        """
        res = []
        i = 0
        for c in reversed(S):
            if i == K:
                res.append('-')
                i = 0
            if c != '-':
                res.append(c.upper())
                i += 1

        return ''.join(reversed(res)).lstrip('-')

s = Solution()
print s.licenseKeyFormatting("5F3Z-2e-9-w",4)
print s.licenseKeyFormatting("--a-a-a-a--",2)
