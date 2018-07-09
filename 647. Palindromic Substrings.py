#1: Expand Around Center
"""
start from each index and try to extend palindrome for both odd and even length.
"""
class Solution(object):
    def countSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        self.ans = 0
        if len(s) == 0 : return self.ans

        for i in xrange(len(s)):
            self.extendPalindrome(s,i,i) #odd
            self.extendPalindrome(s, i, i+1)  #even
        return self.ans

    def extendPalindrome(self,s,left,right):
        while left >= 0 and right < len(s) and s[left] == s[right]:
            self.ans += 1
            left -= 1
            right += 1
s = Solution()
print s.countSubstrings("aaa")

#2. DP just like longest palindrome
# #dp is used for knowing if palindrome or not, not getting count
class Solution(object):
    def countSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        ans = 0
        n = len(s)
        if n == 0: return ans
        dp = [[0] * n for _ in range(n)]
        for l in range(n - 1, -1, -1):
            for r in range(l, n):
                dp[l][r] = (s[l] == s[r]) and (r - l + 1 <= 3 or dp[l + 1][r - 1])
                if dp[l][r]:
                    ans += 1
        return ans
