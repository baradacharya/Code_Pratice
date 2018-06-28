import itertools

"""
  you find the index of each string in dict, conver to an interval, you will get
   
   [[0, 3], [1, 4], [4, 6]]
     aaa     aab      bc
   then combine these intervals
   
   Ater merged, we got [0,6], so we know "aaabbc" needs to be surrounded by tag. 
"""
class Solution(object):
    def boldWords(self, S, words):
        N = len(S)
        mask = [False] * N
        for i in xrange(N):
            prefix = S[i:]
            for word in words:
                if prefix.startswith(word):
                    for j in xrange(i, min(i+len(word), N)):
                        mask[j] = True

        ans = []
        for incl, grp in itertools.groupby(zip(S, mask), lambda z: z[1]):
            if incl:
                ans.append("<b>")
            ans.append("".join(z[0] for z in grp))
            if incl:
                ans.append("</b>")
        return "".join(ans)
s =Solution()
print s.boldWords("abcxyz123",["abc","123"])