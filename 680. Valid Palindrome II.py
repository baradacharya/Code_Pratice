#1.Brute Force [Time Limit Exceeded]
#2. greedy

#T: O(n)
class Solution(object):
    def validPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        def helper(i,j):
            while i < j:
                if s[i] != s[j]:
                    return False
                i += 1
                j -= 1
            return True

        l,r = 0 ,len(s)-1
        while l < r :
            if s[l] != s[r]:
                return helper(l+1,r) or helper(l,r-1) #two pssibilities
            l += 1
            r -= 1
        return True
s = Solution()
print s.validPalindrome("abca")
