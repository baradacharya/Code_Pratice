class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        char_dic = {}
        for c in s:
            if c in char_dic: char_dic[c] += 1
            else: char_dic[c] = 1
        for c in t:
            if c in char_dic:
                char_dic[c] -= 1
                if char_dic[c] < 0:
                    return False
            else:
                return False
        for c in char_dic:
            if char_dic[c] != 0:
                return False
        return True
s = Solution()
print s.isAnagram("rat","car")