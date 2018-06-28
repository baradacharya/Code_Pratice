"""
17. Letter Combinations of a Phone Number
"""

class Solution(object):
    def letterCasePermutation(self, S):
        ans = [""]
        for c in S:
            temp_ans = []
            for s in ans:
                if c.isalpha():
                    temp_ans.append(s + c.upper())
                    temp_ans.append(s + c.lower())
                else:
                    temp_ans.append(s+c)
            ans = temp_ans
        return ans
s = Solution()
print s.letterCasePermutation("abc")