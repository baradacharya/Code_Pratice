class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        1. use two pointers beginning and end of sequence.
        2. update pointers depending on hash map
        """
        """
        :type s: str
        :rtype: int
        """
        chardict = dict()
        i,max_len = 0,0
        for j in range(len(s)):
            if s[j] in chardict and chardict[s[j]]>= i: #check whether char is after the  start pointer and in dictionary
                i = chardict[s[j]] + 1 #move start pointer to the next position of repeating char
            else:
                 max_len = max(max_len,j-i+1)
            chardict[s[j]] = j #store/update current location of char in hashmap
        return max_len
s = Solution()
print s.lengthOfLongestSubstring("tmmzuxt")