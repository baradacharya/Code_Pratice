class Solution(object):
    def repeatedSubstringPattern(self, s):
        """
        :type s: str
        :rtype: bool
        """
        # ss = (s + s)[1:-1]
        # return ss.find(s) != -1

        prefix = self.kmp(s)
        print prefix
        n = len(s);
        length = prefix[n - 1]
        return (length > 0 and n % (n - length) == 0)

    def kmp(self,s):
        length =  len(s)
        lps = [0] * length
        index = 0
        i = 1
        while i < length:
            if s[i] == s[index]:
                lps[i] = index+1
                i += 1
                index += 1
            elif index == 0:
                    i += 1
            else:
                index = lps[index-1]
        return lps
s = Solution()
print s.repeatedSubstringPattern("abcabcabcabc")