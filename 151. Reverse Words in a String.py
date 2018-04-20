class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        if not s: return s
        ans = ""
        for s in reversed(s.split()):
            ans += s
            ans += " "
        return ans.strip()
s = Solution()
print s.reverseWords("the sky is blue")