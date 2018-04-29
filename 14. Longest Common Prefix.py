"""
1. Horizontal scanning, Vertical Scanning T:O(s) where S is the sum of all characters in all strings. S: O(1)
2. Binary Search T: O(s * log n) S: O(1) #search on the length of the string and comapre that length for each string
3. Trie prefered T: O(s),S : O(S)
4.python trick vertical scanning
"""
#python trick vertical scanning
# class Solution(object):
#     def longestCommonPrefix(self, strs):
#         """
#         :type strs: List[str]
#         :rtype: str
#         """
#         if not strs:
#             return None
#         for i,char_list in enumerate(zip(*strs)):
#             c_set = set(char_list)#if all chars are same set will have one char
#             if len(c_set) > 1: #break
#                 return strs[0][:i] #return
#         return i+1 #return the min length

#binary search
class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs:
            return None
        min_len = len(min(strs))
        i,j = 0,min_len
        while i <= j:
            m = (i+j)/2
            if self.isCommonPrefix(strs,m):
                i = m + 1
            else:
                j = m -1
        return strs[0][:(i+j)/2]

    def isCommonPrefix(self,strs,len):
        s = strs[0][:len]
        for str in strs:
            if not str.startswith(s):
                return False
        return True


s  = Solution()
# print s.longestCommonPrefix(["flower","flowers","flower_blue"])
# print s.longestCommonPrefix(["dog","racecar","car"])
# print s.longestCommonPrefix(["a","b"])
print s.longestCommonPrefix(["a"])