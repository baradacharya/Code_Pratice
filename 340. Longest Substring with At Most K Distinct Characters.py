#similar to 159
class Solution(object):
    def lengthOfLongestSubstringKDistinct(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        if k == 0: return 0
        i = 0
        char_dict = {}
        max_len = 0
        for j in range(len(s)):
            c = s[j]
            if c not in char_dict and len(char_dict) >= k : #need to remove oldest used element
                min_index = min(char_dict.values())
                i = min_index + 1
                char_dict.pop(s[min_index])
            char_dict[c] = j
            max_len = max(max_len,j-i+1)
        return max_len