class Solution(object):
    #574s
    # def firstUniqChar(self, s):
    #     """
    #     :type s: str
    #     :rtype: int
    #     """
    #     d = {}
    #     for c in s:
    #         if c in d.keys():
    #             d[c] += 1
    #         else:
    #             d[c] = 1
    #
    #     for i in range(len(s)):
    #         c = s[i]
    #         if d[c]==1:
    #             return i
    #
    #     return -1

    #TLE
    # def firstUniqChar(self, s):
    #     """
    #     :type s: str
    #     :rtype: int
    #     """
    #     for i in range(len(s)):
    #         c = s[i]
    #         if s.count(c)==1:
    #             return i
    #
    #     return -1



    def firstUniqChar(self, s):#104 ms
        """
        :type s: str
        :rtype: int
        """
        char_map = {}
        repeated = set()
        for i, c in enumerate(s):
            if c not in char_map and c not in repeated:
                char_map[c] = i
            elif c not in char_map and c  in repeated:
                continue
            else:
                repeated.add(c)
                char_map.pop(c)
        return min(char_map.values()) if len(char_map) > 0 else -1


s = Solution()
print s.firstUniqChar("loveleetcode")