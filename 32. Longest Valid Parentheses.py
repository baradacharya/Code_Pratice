#1. Brute Force (TLE) T:O(n^3)
# consider every possible non-empty even length substring from the given string
# check whether it's a valid string of parentheses or not.

#2.Using Dynamic Programming
#dp array where ith element of dp represents the length of the longest valid substring ending at ith index.
#T:O(n), S:O(n)
class Solution(object):
    # def longestValidParentheses(self, s):
    #     """
    #     :type s: str
    #     :rtype: int
    #     """
    #     ans  = 0
    #     dp = [0]*len(s)
    #     for i in range(1,len(s)):
    #         if s[i] == ')':
    #             if s[i-1] == '(':
    #                 dp[i] = (dp[i-2] if i > 2 else 0) + 2
    #             else:
    #                 if i-1- dp[i-1] >= 0  and s[i-1-dp[i-1]] == '(':
    #                     dp[i] = dp[i-1] + dp[i - 1 - dp[i-1] - 1] + 2 #substr end with dp[i-1], valid before dp[i-dp[i-1]-2]
    #             ans = max(ans,dp[i])
    #     return ans
    #
    #using stack T:O(n) S:O(n)
    #top of the stack  will always contain start index of valid parenthesis.
    #subtracting it from cur index will tell us length of valid parenthesis.
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        ans  = 0
        stack = []
        stack.append(-1)#last valid for removal
        for i in range(len(s)):
            if s[i] == "(":
                stack.append(i)
            else:
                stack.pop()
                if not stack: stack.append(i)
                else: ans = max(ans,i-stack[-1])
        return ans



s = Solution()
print s.longestValidParentheses("(()())")
# print s.longestValidParentheses(")()())")
