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

    #177s
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        char_map = {}
        for i, c in enumerate(s):
            if c in char_map:
                char_map[c].append(i)
            else:
                char_map[c] = list()
                char_map[c].append(i)
        low_index = len(s)
        flag = False
        #search over 26 characters
        for c in char_map:
            if len(char_map[c]) == 1:
                flag = True
                low_index = min(low_index, char_map[c][0])
        return low_index if flag else -1

    # def firstUniqChar(self, s):#198 ms
    #     """
    #     :type s: str
    #     :rtype: int
    #     """
    #     char_map = {}
    #     repeated = set()
    #     index_list  = set()
    #     for i, c in enumerate(s):
    #         if c not in char_map and c not in repeated:
    #             char_map[c] = i
    #             index_list.add(i)
    #         elif c not in char_map and c  in repeated:
    #             continue
    #         else:
    #             repeated.add(c)
    #             index_list.remove(char_map[c])
    #             char_map.pop(c)
    #
    #     return min(index_list) if len(index_list) > 0 else -1


s = Solution()
print s.firstUniqChar("loveleetcode")