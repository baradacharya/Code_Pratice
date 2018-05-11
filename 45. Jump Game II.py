"""
BFS problem, where nodes in level i are all the nodes that can be reached in i-1th jump. for example. 2 3 1 1 4 , is
2||
3 1||
1 4 ||
"""
#BFS Approach
class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) < 2: return 0
        level,start,curmax,nextmax = 0,0,0,0
        while curmax - start +1 :#no of node in this level
            level += 1
            while start <= curmax:
                if nums[start]+start > nextmax:
                    nextmax = nums[start]+start
                if nextmax >= len(nums)-1:
                    return level;
                start += 1
            curmax = nextmax
        return 0
s = Solution()
print s.jump([2,3,1,1,4])