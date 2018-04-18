class Solution(object):
    def groupAnagrams(self, strs):
        import collections
        ans = collections.defaultdict(list) #use default dic when using list,don't need to intialisze list for unknown keys
        for s in strs:
            ans[tuple(sorted(s))].append(s)
        return ans.values()

s = Solution()
print s.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"])