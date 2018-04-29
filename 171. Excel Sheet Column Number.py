class Solution(object):
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        sum  = 0
        ##revese the string
        for i,c in enumerate(reversed(s)):
            sum += (ord(c) - 65 + 1)* (26 ** i)
        return sum
s = Solution()
print s.titleToNumber("AB")