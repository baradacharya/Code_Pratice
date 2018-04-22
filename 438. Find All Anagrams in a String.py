class Solution(object):

    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        import collections
        counter_p = collections.Counter(p)
        w = len(p)
        counter_s = collections.Counter(s[:w-1])
        res =[]
        for i in range(len(s)-w+1):
            j = i + w -1
            counter_s[s[j]] += 1
            if counter_p == counter_s:
                res.append(i)
            counter_s[s[i]] -= 1
            if counter_s[s[i]] == 0:
                del counter_s[s[i]]
        return res

s = Solution()
# print s.findAnagrams("cbaebabacd","abc")
print s.findAnagrams("abab","ab")

