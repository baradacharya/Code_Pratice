class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        nums.sort()
        self.DFS(nums,0,[],res)
        return res

    def DFS(self,nums,start,path,res):
        res.append(path)

        for i in range(start,len(nums)):
            if i >start and nums[i] == nums[i-1]:#same number only allowed for first time,i>start(trick)
                continue
            self.DFS(nums,i+1,path+[nums[i]],res)

s = Solution()
print s.subsetsWithDup([1,2,2])