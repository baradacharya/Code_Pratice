class Solution(object):
    def nextGreaterElement(self, findNums, nums):
        """
        :type findNums: List[int]
        :type nums: List[int]
        :rtype: List[int]
        """
        stack = []
        indexMap = {} #number,next large number
        res = []
        for i in range(len(nums)):
            while stack and nums[i] > stack[-1]:
                indexMap[stack.pop()] = nums[i]
            stack.append(nums[i])

        while stack:
            indexMap[stack.pop()] = -1
        for num in findNums:
            res.append(indexMap[num])
        return res
