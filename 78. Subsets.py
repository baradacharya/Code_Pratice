"""
Subsets, Permutations, Combination Sum, Palindrome Partitioning
"""
class Solution(object):
    #1. using DFS
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        #either DFS or backtrack can use
        self.DFS(sorted(nums),0,[],res)
        # self.Backtrack(nums, 0, [], res)
        return res
    def DFS(self,nums,index,path,res):
        res.append(path)
        for i in range(index,len(nums)):
            self.DFS(nums,i+1,path+[nums[i]],res)
            #kind of backtracking by this step path+[nums[i]], will remove automatically


s = Solution()
print s.subsets([1,2,3])
