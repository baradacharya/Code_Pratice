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
class Solution(object):
    def countSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        ans = 0
        n = len(s)
        if n == 0 : return self.ans
        dp = [[0]*n for _ in range(n)]
        for i in range(n-1,-1,-1):
            for j in range(i,n):
                dp[i][j] = (s[i] ==s[j]) and (j-i <= 2 or dp[i+1][j-1])
                if dp[i][j]:
                    ans += 1
        return ans


"""
public int countSubstrings(String s) {
    int n = s.length();
    int res = 0;
    boolean[][] dp = new boolean[n][n];
    for (int i = n - 1; i >= 0; i--) {
        for (int j = i; j < n; j++) {
            dp[i][j] = s.charAt(i) == s.charAt(j) && (j - i < 3 || dp[i + 1][j - 1]);
            if(dp[i][j]) ++res;
        }
    }
    return res;
}

"""
