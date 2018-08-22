#T: O(n^2),
#MLE
"""
 we can find the largest segment from the beginning that is a palindrome,
 and we can then easily reverse the remaining segment and append to the beginning.
"""
# class Solution(object):
#     def shortestPalindrome(self, s):
#         """
#         :type s: str
#         :rtype: str
#         """
#         n = len(s)
#         revString = s[::-1]
#         for i in range(n):
#             print s[:n-i],revString[i:]
#             if s[:n-i] == revString[i:]:
#                 return revString[:i] + s
#         return ""


"""
We have seen that the question boils down to finding the largest palindrome substring from the beginning.
KMP:
In Approach #1, we reserved the original string s and stored it as rev. 
We iterate over i from 0 to n-1 and check for s[0:n-i] == rev[i:]. 
Pondering over this statement, had the rev been concatenated to s, 
this statement is just finding the longest prefix that is equal to the suffix.
"""

"""
Algorithm
We use the KMP lookup table generation
Create new_s as s+"#"+reverse(s) and use the string in the lookup-generation algorithm.
The "#" in the middle is required, since without the #, the 2 strings could mix with each ther, producing wrong answer.
Return reversed string after the largest palindrome from beginning length
"""
#T:O(n)
class Solution(object):
    def KMPTable(self,pattern):
        lps = [0] * len(pattern)
        index = 0
        i = 1
        while i  < len(pattern):
            if pattern[i] == pattern[index]:
                lps[i] = index + 1
                index += 1
                i += 1
            else:
                if index != 0:
                    index = lps[index - 1]
                else:
                    lps[i] = 0
                    i += 1
        return lps
    def shortestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        rev_str =  s[::-1]
        temp = s + "#" + rev_str
        n = len(s)
        table = self.KMPTable(temp)
        print temp,table
        print rev_str[:n-table[len(temp)-1]]
        return rev_str[:n-table[2 * n]] + s #temp length: 2*n + 1 , 2n+1-1= 2n

s = Solution()
print s.shortestPalindrome("abcbabcab")