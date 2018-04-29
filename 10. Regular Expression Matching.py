#1.Brute force T: O((T+P) 2 ^ T+p/2) #TLE(not accepted) #447 / 447 test cases passed.
# class Solution(object):
#     def isMatch(self, s, p):
#         """
#         :type s: str
#         :type p: str
#         :rtype: bool
#         """
#         #1.Brute force
#         if not p : return not s
#         first_match = bool(s) and p[0] in {s[0],'.'}
#         if len(p) >=2 and p[1] == '*': #ignore first part like *=0 and move to next part
#             return (self.isMatch(s,p[2:]) or first_match and self.isMatch(s[1:],p))
#         else:
#             return first_match and self.isMatch(s[1:],p[1:])

#2.DP, 2D DP
class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        dp  = [[False] *(len(p)+1) for _ in range(len(s)+1)]
        dp[-1][-1] = True
        for i in range(len(s),-1,-1):
            for j in range(len(p)-1,-1,-1):
                first_match = i < len(s) and (p[j] == s[i] or p[j] == '.')
                if j < len(p)-1 and p[j+1] == '*': #if next ch is *, #*=0 or *!=0
                    dp[i][j] = dp[i][j+2] or (first_match and dp[i+1][j])
                else:
                    dp[i][j] = first_match and dp[i+1][j+1]
        return dp[0][0]

s = Solution()
print s.isMatch("aa","a*")
