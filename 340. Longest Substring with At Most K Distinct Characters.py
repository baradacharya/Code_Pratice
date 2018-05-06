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
            if s[j] not in char_dict and len(char_dict) >= k:  # need to remove least used element
                # find the least recent used char
                min_index = min(char_dict.values())
                for c in char_dict:
                    if char_dict[c] == min_index:
                        key = c
                        break
                i = min_index + 1
                char_dict.pop(key)
            char_dict[s[j]] = j
            max_len = max(max_len, j - i + 1)
        return max_len