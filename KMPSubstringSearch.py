"""
Do Pattern matching using KMP Search.
T: O(m+n) where m is length text and n is length pattern.
S: O(n)

The purpose of the lookup table is to store the length of the proper prefix of the string that is also a suffix of the string.
"""
class SubstringSearch:

    #Compute temporary array to maintain size of suffix which is same as prefix
    def computeTemporaryArray(self,pattern):
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

    #KMP algorithm of pattern matching.
    def KMP(self,text,pattern):
        lps = self.computeTemporaryArray(pattern)
        print lps
        i,j = 0,0
        m,n = len(text),len(pattern)
        while i < m and j < n:
            if text[i] == pattern[j]:
                i += 1
                j += 1
            else:
                if j!=0 :
                    j = lps[j-1]
                else:
                    i += 1
        return j == n

str = "abcxabcdabcdabcy"
subString = "aaacecaaa"
ss = SubstringSearch()
print ss.KMP(str,subString)
subString = "abcdabca"
print ss.KMP(str,subString)
subString = "aabaabaaa"
print ss.KMP(str,subString)
subString = "abcdabcy"
print ss.KMP(str,subString)
