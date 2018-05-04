class Solution(object):
    def longestSubstring(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        if len(s) < k: return 0
        max_len  = 0
        c = min(set(s), key=s.count) #ch with lowest fq
        if s.count(c) >= k: #all ch with k freq
            return len(s)
        for t in s.split(c):
            max_len = max(self.longestSubstring(t,k),max_len)
        return max_len 