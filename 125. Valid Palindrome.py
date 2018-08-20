#skip space character
class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if len(s)==0: return True
        l,r = 0,len(s)-1
        while l < r:
            while l < r and not s[l].isalnum():#skip space character
                l += 1
            while l < r and not s[r].isalnum():#skip space character
                r -= 1
            if s[l].lower() != s[r].lower():
                return False
            l += 1
            r -= 1
        return True
s = Solution()
print s.isPalindrome("A man, a plan, a canal: Panama")
print s.isPalindrome("0p")