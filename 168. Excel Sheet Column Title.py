class Solution(object):
    def convertToTitle(self, n):
        """
        :type n: int
        :rtype: str
        """

        str = []
        while n > 0:
            num = (n-1) % 26
            str += chr( num+ ord('A'))
            n = (n-1)/26
        return ''.join(reversed(str))
s = Solution()
print s.convertToTitle(28)
print s.convertToTitle(26)
print s.convertToTitle(1)
