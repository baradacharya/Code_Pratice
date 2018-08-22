import itertools

"""
  you find the index of each string in dict, conver to an interval, you will get
   
   [[0, 3], [1, 4], [4, 6]]
     aaa     aab      bc
   then combine these intervals
   
   Ater merged, we got [0,6], so we know "aaabbc" needs to be surrounded by tag. 
   
"""
#270 ms
# class Solution(object):
#     def boldWords(self, S, words):
#         N = len(S)
#         mask = [False] * N
#         for i in xrange(N):
#             prefix = S[i:]
#             for word in words:
#                 if prefix.startswith(word):
#                     for j in xrange(i, min(i+len(word), N)):
#                         mask[j] = True
#
#         ans = []
#         for incl, grp in itertools.groupby(zip(S, mask), lambda z: z[1]):#group by mask, all consecutive true values
#             if incl:
#                 ans.append("<b>")
#             ans.append("".join(z[0] for z in grp))
#             if incl:
#                 ans.append("</b>")
#         return "".join(ans)

#44ms
class Solution(object):
    def addBoldTag(self, s, dict):
        """
        :type s: str
        :type dict: List[str]
        :rtype: str
        """
        n = len(s)
        status = [False] * n
        final = ""

        for word in dict:
            start = s.find(word)
            wordLen = len(word)
            while start != -1:  # search the word multiple times
                for i in range(start, start + wordLen):
                    status[i] = True
                start = s.find(word, start + 1)
        i = 0
        while i < n:
            if status[i]:
                final += "<b>"
                while i < len(s) and status[i]:
                    final += s[i]
                    i += 1
                final += "</b>"
            else:
                final += s[i]
                i += 1
        return final


s =Solution()
print s.addBoldTag("abcxyz123",["abc","123"])

