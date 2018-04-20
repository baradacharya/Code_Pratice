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
        nums.sort()
        #self.DFS(sorted(nums),0,[],res)
        self.Backtrack(nums, 0, [], res)
        return res
    def DFS(self,nums,index,path,res):
        res.append(path)
        for i in range(index,len(nums)):
            self.DFS(nums,i+1,path+[nums[i]],res)
            #kind of backtracking by this step path+[nums[i]], will remove automatically

    def Backtrack(self,nums,index,path,res):
        res.append(list(path)) #to add new list of path
        for i in range(index,len(nums)):
            path.append(nums[i])
            self.Backtrack(nums,i+1,path,res)
            path.pop() #backtrack


s = Solution()
print s.subsets([1,2,3])
