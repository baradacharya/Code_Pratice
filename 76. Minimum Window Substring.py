class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        import collections
        # no of char we need,pos no -> we need that much ch in our window,neg no we don't need, can remove from window.
        char_dic = collections.Counter(t)
        missing = len(t) #no of char of t missing from window
        l = start = end = 0 #l,r two pointer of window, start,end min windo
        for r, c in enumerate(s,1):#to satisfy i:j terminlogy (j exclusive)
            if char_dic[c] > 0:#we need this char
                missing -= 1 #reduce no of req char
            char_dic[c] -= 1
            if not missing:#all members of t present in window, can reduce window size.
                while l < r and char_dic[s[l]] < 0:#check the leftmost pointer of window
                    char_dic[s[l]] += 1 #remove from window, increase requirement in dic
                    l += 1
                #check for update
                if not end or r - l <= end - start:
                    start, end = l, r
        return s[start:end]
s = Solution()
print s.minWindow("ADOBECODEBANC","ABC")
